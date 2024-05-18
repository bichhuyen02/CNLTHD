import { Ionicons } from '@expo/vector-icons';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import React, {useReducer, useState } from 'react';
import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import Home from './components/Home/Home';
import Busses from './components/Trip/Busses';
import Pay from './components/Pay/Pay';
import Ticket from './components/Ticket/Ticket';
import Account from './components/User/Account';
import HistoryOrder from './components/History/HistoryOrder';
import Register from './components/User/Register';
import Reposes from './components/Complain/Reposes';
import Signin from './components/User/Signin';
import Welcome from './components/Home/Welcome';
import MyContext from './config/MyContext';
import MyUserReducer from './reducer/MyUserReducer';
import Search from './components/Trip/Search';




const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

function TrangChu() {
  return (
    <Tab.Navigator initialRouteName="Home" screenOptions={({ route }) => ({
      tabBarIcon: ({ color, size }) => {
        let iconName;

        if (route.name === 'Home') {
          iconName = 'home';
        } else if (route.name === 'Account') {
          iconName = 'person';
        } 

        return <Ionicons name={iconName} size={size} color={color} />;
      },

      tabBarActiveTintColor: '#003399',
      tabBarInactiveTintColor: 'black',
      headerShown: false,
    })}>
      <Tab.Screen name="Home" component={Home} options={{ title: 'Trang chủ' }}/>
      <Tab.Screen name="Account" component={Account} options={{ title: 'Tài khoản' }} />
    </Tab.Navigator>
  );
}

const ImageHeader = ({ navigation }) => {
  const handleGoBack = () => {
    navigation.goBack('Busses');
  };

  return (
    <View style={{ height: 150, flexDirection: 'row', alignItems: 'center' }}>
      <TouchableOpacity onPress={handleGoBack} style={{ position: 'absolute', zIndex: 9 }}>
        <Ionicons name="arrow-back" size={24} color="black" />
      </TouchableOpacity>

      <Image
        source={require('./components/Ticket/car.jpg')}
        style={{ flex: 1, height: '100%', resizeMode: 'stretch' }}
      />
    </View>
  );
};

export default App = () => {
  const [user, dispatch] = useReducer(MyUserReducer, null);

  return (
    <MyContext.Provider value={[user, dispatch]}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Welcome" options={{ headerShown: false }}>
          <Stack.Screen name="TrangChu" component={TrangChu} options={{ headerShown: false }} />
          <Stack.Screen name="Signin" component={Signin} options={{ headerShown: false }} />
          <Stack.Screen name="Register" component={Register} options={{ headerShown: false }} />
          <Stack.Screen name="Welcome" component={Welcome} options={{ headerShown: false }} />
          <Stack.Screen name="Ticket" component={Ticket} options={{
            headerShown: true,
            headerTitle: '',
            header: ({ navigation }) => <ImageHeader navigation={navigation} />,
          }} />
          <Stack.Screen name="Busses" component={Busses} options={{ headerShown: true, headerTitle: 'Tuyến xe' }} />
          <Stack.Screen name="HistoryOrder" component={HistoryOrder} options={{ headerShown: true, headerTitle: 'Lịch sử đặt vé' }} />
          <Stack.Screen name="Reposes" component={Reposes} options={{ headerShown: true, headerTitle: 'Phản hồi ý kiến' }} />
          <Stack.Screen name="Pay" component={Pay} options={{ headerShown: true, headerTitle: 'Thanh toán' }} />
          <Stack.Screen name="Search" component={Search} options={{ headerShown: false }} />
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