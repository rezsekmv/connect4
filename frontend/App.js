import 'react-native-gesture-handler';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, View, Platform, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Menu from './components/Menu';
import Game  from './components/Game';



export default function App() {
/*    return (
      <View style={styles.container}>
        <Text style={{fontSize: 90, fontFamily: 'bold', color: 'red'}}>VEGYEL TELOT!!</Text>
      <StatusBar hidden={true} style="light"/>
    </View>
    )
*/

  const Stack = createStackNavigator();

  return (
    <NavigationContainer>
      <StatusBar hidden={true} style="light"/>
      <Stack.Navigator>
        <Stack.Screen
        name="Menu"
        component={Menu}
        options={{ headerShown: false }}
        />
        <Stack.Screen
        name="Game"
        component={Game}
        options={{ headerShown: false }}
        />
      </Stack.Navigator>
    </NavigationContainer>
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
