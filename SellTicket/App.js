import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import Login from './components/User/Login';
import Account from './components/User/Account';



const HomeScreen = () => {
    return <View style = {styles.container}>
     <Text> tab 1</Text>
    </View>
};

const SettingsScreen = () => {
  return <View style = {styles.container}>
    <Text>tab 2</Text>
  </View>
};

const Tab = createBottomTabNavigator();

export default  App = () => {
  return (
    <NavigationContainer>
    <Tab.Navigator>
      <Tab.Screen name="Trang chủ" component={HomeScreen} />
      <Tab.Screen name="Lịch sử" component={SettingsScreen} />
      <Tab.Screen name="Tài khoản" component={Login} />
      <Tab.Screen name="acc" component={Account} />
    </Tab.Navigator>
  </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  background: {
    backgroundColor: 'rgb(32 178 170)',
  },
  container: {
    flex: 1,
    backgroundColor: 'rgb(32 178 170)',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
