import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, View, Platform, Text } from 'react-native';
import Menu from './components/Menu';
import { windowHeight } from './Constants';


export default function App() {
/*    return (
      <View style={styles.container}>
        <Text style={{fontSize: 90, fontFamily: 'bold', color: 'red'}}>VEGYEL TELOT!!</Text>
      <StatusBar hidden={true} style="light"/>
    </View>
    )
*/
  return (
    <>
      <Menu/>
      <StatusBar hidden={true} style="light"/>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: 'grey',
    height: '100%'
  }
});
