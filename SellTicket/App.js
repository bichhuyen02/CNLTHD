import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import React, { useReducer, useState } from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import Login from './components/User/Login';
import Account from './components/User/Account';
import MyContext from './MyContext';
import MyUserReducer from './MyUserReducer'
import Apis from './Apis';

const [cates, setCates] = useState()
useEffect(() => {
const loadCates = async () => {
let res = await API.get(endpoints["categories"])
setCates(res.data)
}
loadCates()
}, [])

const HomeScreen = () => {
    return <View style = {styles.container}>
     {cates.map(it => <li>{it.name}</li>)}
    </View>
};

const SettingsScreen = () => {
  return <View style = {styles.container}>
    <Text>tab 2</Text>
  </View>
};

const Tab = createBottomTabNavigator();

export default  App = () => {

  const [user, dispatch] = useReducer(MyUserReducer, null);

  return (
    <MyContext.Provider value={[user , dispatch]}>
    <NavigationContainer>
    <Tab.Navigator>
      <Tab.Screen name="Trang chủ" component={HomeScreen} />
      <Tab.Screen name="Lịch sử" component={SettingsScreen} />
      <Tab.Screen name="Tài khoản" component={Login} />
      <Tab.Screen name="acc" component={Account} />
    </Tab.Navigator>
  </NavigationContainer>
  </MyContext.Provider>
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
