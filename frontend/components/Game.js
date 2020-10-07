import React, {useState} from 'react';
import { StyleSheet, View, Platform, TouchableOpacity } from 'react-native';
import Disc from './Disc';
import { windowWidth, windowHeight, COLNUM, ROWNUM, webWidth, webHeigth} from '../Constants.js';


export default class Game extends React.Component {  
  
  constructor(props) {
    super(props);

    this.state = { board: [
      [ 0, 0, 0, 0, 0, 0, 0 ],
      [ 0, 0, 0, 0, 0, 0, 0 ],
      [ 0, 0, 0, 0, 0, 0, 0 ],
      [ 0, 0, 0, 0, 0, 0, 0 ],
      [ 0, 0, 0, 0, 0, 0, 0 ],
      [ 0, 0, 0, 0, 0, 0, 0 ],
    ]};
  }



  getBoardFromApi = async (col) => {
    return await fetch('http://localhost:5000/move', {
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
      .then( (json) => this.setState({board: json.board}))
      .catch((error) => {
        console.error(error);
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
    let row = this.getRow(col);
    let newboard = this.state.board;

    console.log('row: ' + row + ' col: ' + col);
    if (row === -1)
      return;
    newboard[row][col] = 1;
    this.setState({ board: newboard });
    await this.getBoardFromApi(col);
  }

  renderRow(row, index) {
    return ( 
    <View key={index} style={styles.row}>
      {row.map( (d, i) => {
        return (
        <View style={styles.grid} key={i}>
          <TouchableOpacity onPress={() => this.handleMoveClick(i)}>
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
    //responsive to srceen pixels
    width: windowWidth/COLNUM,
    height: windowHeight/ROWNUM,

    //center horizontal
    alignItems: 'center',
    //center vertical
    justifyContent: 'center',

    backgroundColor: "blue",
    
    borderLeftWidth: 1,
    borderRightWidth: 1
  }

});
  