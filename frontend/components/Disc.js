import React from 'react';
import {StyleSheet, View, Platform} from 'react-native';
import { windowWidth, windowHeight, COLNUM, ROWNUM } from '../Constants.js';

export default class Disc extends React.Component {
    
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <View style={this.styles.dot}/>
        )
    }


    radius = windowWidth/COLNUM > windowHeight/ROWNUM ? windowHeight/ROWNUM-7 : windowWidth/COLNUM-7;

    styles = StyleSheet.create(
        {
            dot: {
                //responsive to srceen pixels
                width: this.radius,
                height: this.radius,
                borderRadius: this.radius/2,

                backgroundColor: 'grey',
                
            }
        }
    )
}
