import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import React, { useEffect, useReducer, useState } from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import Login from './components/User/Login';
import Account from './components/User/Account';
import MyContext from './MyContext';
import MyUserReducer from './MyUserReducer'
import Apis, { endpoints } from './Apis';
import Logout from './components/User/Logout';
import Register from './components/User/Register';
import Signin from './components/User/Signin';
import Welcome from './components/User/Welcome';
import Home from './components/Home/Home';
import RegisterAccount from './components/User/RegisterAccount';

const HomeScreen = (props) => {
  // const [categories, setCategories] = useState([]);

  // useEffect(()=>{
  //   const loadCategory = async ()=>{
  //     const res = await Apis.get(endpoints['categories']);
  //     setCategories(res.data)
  //   }
  //   loadCategory();
  //   }, [])

  return <View>
    <Text>tab 1</Text>
  </View>
  // <View {...props} style = {styles.container}>
  //    {categories.map(c=><Text key={c.id}>{c.name}</Text>)}
  //   </View>
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
      <Tab.Screen name="Xin Chào" component={Welcome} />
      <Tab.Screen name="Trang chủ" component={Home} />
        <Tab.Screen name="Tài khoản" component={Login} />
      <Tab.Screen name="Đăng nhập" component={Signin} />
      <Tab.Screen name="Đăng ký tài khoản" component={RegisterAccount} />
      
    </Tab.Navigator>
  </NavigationContainer>
  </MyContext.Provider>
  );
}

const styles = StyleSheet.create({
  // background: {
  //   backgroundColor: 'rgb(32 178 170)',
  // },
  container: {
    flex: 1,
    // backgroundColor: 'rgb(32 178 170)',
    color: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  }
});