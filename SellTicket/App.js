import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { StatusBar } from 'expo-status-bar';
import React, { useEffect, useReducer, useState } from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import Signin from './components/User/Signin';
import Welcome from './components/User/Welcome';
import Home from './components/Home/Home';
import RegisterAccount from './components/User/RegisterAccount';
import MyContext from './config/MyContext'
import MyUserReducer from'./reducer/MyUserReducer'
import ProfileView from './components/User/Account'
import Apis, { endpoints } from './config/Apis';
import Account from './components/User/Account';
import Trip from './components/Trip/Trip';
import { Ionicons } from '@expo/vector-icons';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Ticket from './components/Ticket/Ticket';
import { HeaderTitle } from '@react-navigation/elements';
import Busses from './components/Ticket/Busses';

const HomeScreen = () => {
  const [categories, setCategories] = useState([]);

  useEffect(()=>{
    const loadCategory = async ()=>{
      const res = await Apis.get(endpoints['categories']);
      setCategories(res.data)
    }
    loadCategory();
    },[])

  return<View style = {styles.container}>
     {categories.map(c=><Text key={c.id}>{c.name}</Text>)}
    </View>
};

const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

function TrangChu() {
  return (
      <Tab.Navigator initialRouteName="Home" screenOptions={({ route }) => ({
          tabBarIcon: ({ color, size }) => {
              let iconName;

              if (route.name === 'Home') {
                  iconName = 'home';
              } else if (route.name === 'Ticket') {
                  iconName = 'person';
              } else if (route.name === 'Trip') {
                  iconName = 'clipboard';
              }

              return <Ionicons name={iconName} size={size} color={color} />;
          },

          tabBarActiveTintColor: 'green',
          tabBarInactiveTintColor: 'black',
          headerShown: false,
      })}>
          <Tab.Screen name="Home" component={Home}/>
          <Tab.Screen name="Trip" component={Trip} options={{ title: 'Chuyen di' }} />
      </Tab.Navigator>
  );
}

export default  App = () => {

  const [user, dispatch] = useReducer(MyUserReducer, null);
  return (
    <MyContext.Provider value={[user , dispatch]}>
    <NavigationContainer>
    <Stack.Navigator initialRouteName="Ticket" options={{ headerShown: false }}>
      <Stack.Screen name="TrangChu" component={TrangChu } options={{ headerShown: false }}/>
      <Stack.Screen name="Signin" component={Signin} options={{ headerShown: false }} />
      <Stack.Screen name="RegisterAccount" component={RegisterAccount} options={{ headerShown: false }} />
      <Stack.Screen name="Welcome" component={Welcome} options={{ headerShown: false }} />
      <Stack.Screen name="Ticket" component={Ticket} options={{ 
        headerShown: true, 
        headerTitle:'',
        // headerBackground:() =>(
        //   <Image  source={require('./components/Ticket/car.jpg')}
        //   style={{ width: '100%', height: '100%' }} />
        // ),
        // headerStyle: {
        //   height: 200, // Tùy chỉnh chiều cao của header
        // },

      //   headerTitle: props => (
      //     <HeaderTitle {...props}>
      //         <Image
      //             source={require('./components/Ticket/car.jpg')}
      //             style={{ width: 300, height: 200, resizeMode: 'cover' }}
      //         />
      //     </HeaderTitle>
      // ),
       }} />
      <Stack.Screen name="Busses" component={Busses} options={{ headerShown: true, headerTitle: 'Tuyến xe' }} />
    </Stack.Navigator>
  </NavigationContainer>
  </MyContext.Provider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    color: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  }
});