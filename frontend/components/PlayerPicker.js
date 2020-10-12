import React, { useState } from 'react';
import {Picker, View, StyleSheet} from 'react-native';
import { playerValues } from '../Constants';

export default function PlayerPicker() {
    const [selected, setSelected] = useState(playerValues[0])

    return (
        <View style={styles.view}>
            <Picker
                selectedValue={selected}
                style={styles.picker}
                onValueChange={(itemValue) => setSelected(itemValue)}>
                
                {playerValues.map( (v, k) => {
                    return (<Picker.Item key={k} label={v} values={v}></Picker.Item>)
                })}
            </Picker>
        </View>
    )
}

const styles = StyleSheet.create({ 
    view: {
        borderWidth: 1,
        borderColor: 'black',
        borderRadius: 4,
        backgroundColor: 'lightblue'
    },
    picker: {
        height: 30,
        width: 150, 
        color: 'darkblue' 
    }
})