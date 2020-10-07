import React from 'react';
import {StyleSheet, View} from 'react-native';
import { windowWidth, windowHeight, COLNUM, ROWNUM } from '../Constants.js';

export default class Disc extends React.Component {
    
    constructor(props) {
        super(props)
    }

    render() {
        let disc;
        if (this.props.value === 1)
            disc = <View style={[this.styles.dot, this.styles.red]}/>;
        else if (this.props.value === 2) 
            disc = <View style={[this.styles.dot, this.styles.yellow]}/>;
        else
            disc = <View style={[this.styles.dot, this.styles.empty]}/>;
    
        return (
            disc
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
            },
            empty: {
                backgroundColor: 'grey'
            },
            red: {
                backgroundColor: 'red'
            },
            yellow : {
                backgroundColor: 'yellow'
            }
        }
    )
}
