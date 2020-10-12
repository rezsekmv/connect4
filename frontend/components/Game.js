import React from 'react';
import { StyleSheet, View, Platform, TouchableOpacity, Text } from 'react-native';
import Disc from './Disc';
import { windowWidth, windowHeight, COLNUM, ROWNUM, URLmove} from '../Constants.js';


export default class Game extends React.Component {  

  constructor(props) {
    super(props);

    this.state = {
      board: [
        [ 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0 ],
      ],
      inputDisabled: false,
      wonBy: -1
    };
  }

  getMoveFromApi = async (col) => {
    return await fetch(URLmove, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        human: 1,
        ai: 2,
        column: col,
        board: this.state.board
      })
    })
      .then((response) => response.json())
      .then( (json) => { return json; } )
      .catch((error) => {
        console.error('Can not reach backend');
      });
    };

  getRow(col) {
    let rowNum = -1;
    this.state.board.map( (r, i) => {
      r.map( (d, j) => {
        if (col === j && d === 0)
          rowNum = i
      });
    })
    return rowNum
  }

  async handleMoveClick(col) {
    this.setState({ inputDisabled: true })
    let row = this.getRow(col);
    let newboard = this.state.board;

    //if the column is full
    if (row === -1)
      return;

    //local move (on phone)
    newboard[row][col] = 1;
    this.setState({ board: newboard });
    
    //remote move (by the ai)
    let json = await this.getMoveFromApi(col);
    if (typeof json === 'undefined')
      return;
    this.setState({ board: json.board, wonBy: json.wonBy})    

    //checks if the game is over
    if (this.state.wonBy === -1) {
      this.setState({ inputDisabled: false })
    }

  }

  renderRow(row, index) {
    return ( 
    <View key={index} style={styles.row}>
      {row.map( (d, i) => {
        return (
        <View style={styles.grid} key={i}>
          <TouchableOpacity onPress={() => this.handleMoveClick(i)} disabled={this.state.inputDisabled}>
            <Disc value={d}/>
          </TouchableOpacity>  
        </View>)
      })}
    </View>
    )
  }

  render() {
    return (
      <View style={styles.board}>
        {this.state.board.map( (e, i) => {
          return this.renderRow(e, i)
        })}
        { this.state.wonBy !== -1 &&
          <Text style={styles.gameover}>Game Over!</Text>
        }
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
    width: Platform.OS === 'ios' ? windowHeight/COLNUM : windowWidth/COLNUM,
    height: Platform.OS === 'ios' ? windowWidth/ROWNUM : windowHeight/ROWNUM,

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
    textAlign: 'center',
    color: 'lightgreen',
    fontWeight: 'bold',
    fontSize: 70
  }

});
  