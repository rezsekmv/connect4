import React from 'react';
import { StyleSheet, View, Text, Button, ImageBackground, TouchableOpacity} from 'react-native';

import PlayerPicker from './PlayerPicker';
import { playerValues, padding } from '../Constants';

export default class Menu extends React.Component {  

    constructor(props) {
        super(props)
        this.state = {
            player1: playerValues[0],
            player2: playerValues[0]
        }
    }

    handlePlayerState(player, state) {
        this.setState({[player]: state});
    }

    handleStart() {                    
        
        this.props.navigation.push('Game', {
            player1: this.state.player1,
            player2: this.state.player2
          })
    }

    //    <ImageBackground source={require('../assets/images/c4_background.jpg')} style={styles.image} >

    render() {
        return (
            <View style={styles.base}>
                <Text style={styles.title}>Connect 4 Game</Text>
                
                <View style={styles.playerContainer}>
                    <View style={styles.player}>
                        <Text style={styles.playerText}>Player One</Text>
                        <PlayerPicker player={'player1'} picker={(p, s) => this.handlePlayerState(p, s)}/>
                    </View>
                    <View style={styles.player}>
                        <Text style={styles.playerText}>Player Two</Text>
                        <PlayerPicker player={'player2'} picker={(p, s) => this.handlePlayerState(p, s)}/>
                    </View>
                </View>
                <View style={styles.startContainer}>
                    <TouchableOpacity style={styles.start} onPress={() => this.handleStart()}>
                        <Text style={styles.startText}>Start Game</Text>
                    </TouchableOpacity>
                </View>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    base: {
        flex: 1,
        height: '100%',
        backgroundColor: 'lightgreen'
    },
    image: {
        flex: 1,
        width: '100%',
        height: '100%',
        justifyContent: "center"
    },
    title: {
        fontSize: 50,
        fontWeight: 'bold',
        color: 'blue',
        textAlign: 'center',
        marginTop: '3%'
    },
    playerContainer: {
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'center',
        flexWrap: 'wrap',
        padding: '5%'
    },
    player: {
        flex:1,
        paddingBottom: '10%',
        alignItems: 'center'
    },
    playerText: {
        fontSize: 20,
        marginBottom: 10,
        fontWeight: 'bold'
    },
    startContainer: {
        justifyContent: 'center',
        alignItems: 'center',
    },
    start: {
        backgroundColor: 'grey',
        ...padding(5, 10, 5, 10),
        marginBottom: '1%',
        alignItems: 'center',
        borderRadius: 20
    },
    startText: {
        color: 'white',
        fontSize: 20,
        fontWeight: 'bold',
    }
});