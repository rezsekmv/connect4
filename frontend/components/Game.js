import React, {useState} from 'react';
import { StyleSheet, View, Platform } from 'react-native';
import Disc from './Disc';
import { windowWidth, windowHeight, COLNUM, ROWNUM, webWidth, webHeigth} from '../Constants.js';


export default class Game extends React.Component {  
  
  constructor(props) {
    super(props);

    this.state = { board: [
      [ [], [], [], [], [], [], [] ],
      [ [], [], [], [], [], [], [] ],
      [ [], [], [], [], [], [], [] ],
      [ [], [], [], [], [], [], [] ],
      [ [], [], [], [], [], [], [] ],
      [ [], [], [], [], [], [], [] ],
    ]};
  }

  renderRow(row, index) {
    return ( 
    <View key={index} style={styles.row}>
      {row.map( (d, i) => {
        return (
        <View style={styles.grid} key={i}>
          <Disc/>  
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
  