import React from 'react';
import { StyleSheet, View, Platform, TouchableOpacity, Text } from 'react-native';
import Disc from './Disc';
import { windowWidth, windowHeight, COLNUM, ROWNUM, URLminmax, URLneatai, URLcheckwin, padding } from '../Constants.js';
import { checkWinFromApi, getMoveFromApi } from '../services/move-service';

export default class Game extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      board: [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
      ],
      player1: this.props.route.params.player1,
      player2: this.props.route.params.player2,
      next_player: 1,
      wonBy: -1,
      inputDisabled: false,
    };

    this.startGame()
  }

  startGame() {
    //2 ai-s against each other START it immediately
    if (this.state.player1 !== 'human' && this.state.player2 !== 'human') {
      this.aiGame()
    }
    else if (this.state.player1 !== 'human') {
      this.aiMove()
    }
  }

  getRow(col) {
    let rowNum = -1;
    this.state.board.map((r, i) => {
      r.map((d, j) => {
        if (col === j && d === 0)
          rowNum = i
      });
    })
    return rowNum
  }

  async humanMove(col) {
    let row = this.getRow(col);
    let newboard = this.state.board;

    //if the column is full
    if (row === -1)
      return;

    //local move (on phone)
    newboard[row][col] = this.state.next_player;

    this.setState({ board: newboard });

    let json = await checkWinFromApi(URLcheckwin, this.state.board);
    this.setState({ wonBy: json.wonBy });

    this.state.next_player === 1 ? this.setState({ next_player: 2 }) : this.setState({ next_player: 1 })
  }

  async aiMove() {
    let json = undefined;
    //remote move (by the ai)
    if (this.state.next_player === 1) {
      if (this.state.player1 === 'minmax')
        json = await getMoveFromApi(URLminmax, this.state.board, this.state.next_player);
      if (this.state.player1 === 'neatai')
        json = await getMoveFromApi(URLneatai, this.state.board, this.state.next_player);
    }
    if (this.state.next_player === 2) {
      if (this.state.player2 === 'minmax')
        json = await getMoveFromApi(URLminmax, this.state.board, this.state.next_player);
      if (this.state.player2 === 'neatai')
        json = await getMoveFromApi(URLneatai, this.state.board, this.state.next_player);
    }
    if (typeof json === 'undefined')
      return;
    this.setState({ board: json.board, wonBy: json.wonBy, next_player: json.next_player })
  }

  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  async aiGame() {
    await this.sleep(1500)
    await this.aiMove()
    if (this.state.wonBy === -1) {
      this.aiGame()
    }
  }

  async humanVsAi(col) {
    //next_player is player1 
    if (this.state.next_player === 1) {
      //player1 is human
      if (this.state.player1 === 'human') {
        await this.humanMove(col)
        this.aiMove()
      }
    }
    else {
      if (this.state.player2 === 'human') {
        await this.humanMove(col)
        this.aiMove()
      }
    }
  }


  async handleMoveClick(col) {
    this.setState({ inputDisabled: true })

    //2 human against each other  
    /*if (this.state.player1 === 'human' && this.state.player2 === 'human') {
      this.humanMove(col)
    }*/
    await this.humanMove(col)
    await this.aiMove()

    /*if ((this.state.player1 === 'human' && this.state.player2 !== 'human')
      || (this.state.player1 !== 'human' && this.state.player2 === 'human')) {
      this.humanVsAi(col)
    }*/

    //checks if the game is over
    if (this.state.wonBy === -1) {
      this.setState({ inputDisabled: false })
    }
  }

  goToMenu() {
    this.props.navigation.push('Menu');
  }

  renderRow(row, index) {
    return (
      <View key={index} style={styles.row}>
        {row.map((d, i) => {
          return (
            <View style={styles.grid} key={i}>
              <TouchableOpacity onPress={() => this.handleMoveClick(i)} disabled={this.state.inputDisabled}>
                <Disc value={d} />
              </TouchableOpacity>
            </View>)
        })}
      </View>
    )
  }

  render() {
    return (
      <View style={styles.board}>
        {this.state.board.map((e, i) => {
          return this.renderRow(e, i)
        })}
        {this.state.wonBy === 1 &&
          <Text style={styles.gameover}>Player1 (RED) won!</Text>
        }
        {this.state.wonBy === 2 &&
          <Text style={styles.gameover}>Player2 (YELLOW) won!</Text>
        }
        {/*this.state.wonBy !== -1 &&
          <TouchableOpacity style={styles.reset} onPress={() => this.goToMenu()}>
            <Text style={styles.resetText}>Go to Menu</Text>
          </TouchableOpacity>
        */}
      </View>
    );
  }
}


const styles = StyleSheet.create({
  board: {
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1,
  },
  row: {
    flexDirection: 'row'
  },
  grid: {
    //responsive to srceen pixels (on ios width and height switched)
    width: Platform.OS === 'ios' ? windowHeight / COLNUM : windowWidth / COLNUM,
    height: Platform.OS === 'ios' ? windowWidth / ROWNUM : windowHeight / ROWNUM,

    //center horizontal
    alignItems: 'center',
    //center vertical
    justifyContent: 'center',

    backgroundColor: "blue",

    borderLeftWidth: 1,
    borderRightWidth: 1
  },
  gameover: {
    position: 'absolute',
    top: windowHeight/4,
    textAlign: 'center',
    color: 'lightgreen',
    fontWeight: 'bold',
    fontSize: 70
  },
  reset: {
    position: 'absolute',
    top: windowHeight/3*2,
    backgroundColor: 'brown',
    ...padding(5, 10, 5, 10),
    marginBottom: '1%',
    alignItems: 'center',
    borderRadius: 20
  },
  resetText: {
    color: 'yellow',
    fontSize: 20,
    fontWeight: 'bold',
    margin: 5
  }

});
