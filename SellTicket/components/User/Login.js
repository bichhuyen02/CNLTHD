import AsyncStorage from "@react-native-async-storage/async-storage";
import React, { useContext, useState } from 'react';
import { View, Text, Image, TextInput, TouchableOpacity, ActivityIndicator } from 'react-native';
import Apis, { authApi, endpoints } from '../../Apis';
import MyContext from '../../MyContext';
import Styles from "./Styles";


export default Login = ({navigation}) => {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    const [user, dispatch] = useContext(MyContext);
    const [loading, setLoading] = useState();



    const login =  async () => {
      setLoading(true);
      try {
          let res = await Apis.post(endpoints['login'], {
            "username": username, 
            "password": password,
            "client_id": "Lhh7xLgBYQXag5ch7oUoGJBM6B6YlCy1vDTiMht8",
            "client_secret": "OXD3Ba9YweJFdGCbdD1Le1N9yDfo5mXfP1ucNMrqGaZM1ZO7cc7vA7K6rILkZGPTyqnAZRCzRXcxavVcN9RTKCpcuJiwsB5dlD71aiHj72a5fJnw56O6P0AEiN7EBXgL",
            "grant_type": "password"
          });

          console.info(res.data)

          await AsyncStorage.setItem('access-token', res.data.access_token)
          let user = await authApi(res.data.access_token).get(endpoints['current_user']);
          console.info(user.data)
          dispatch({
                      'type': 'login',
                      'payload': {
                          'username': user.data.username
                      }
                  })
          alert("Đăng nhập thanh công!");
      } catch (error) {
          console.error(error);
      } finally{
          setLoading(false);
      }
  }


  return (
    <View style={Styles.container}>
      <Image
        source={{uri: 'https://www.bootdey.com/image/280x280/20B2AA/20B2AA'}}
        style={Styles.background}
      />
      <View style={Styles.logoContainer}>
        <Image
          source={{uri: 'https://www.bootdey.com/img/Content/avatar/avatar7.png'}}
          style={Styles.logo}
        />
      </View>
      <View style={Styles.formContainer}>
        <Text style={Styles.title}>Login</Text>
        <View style={Styles.card}>
{/* username */}
          <View style={Styles.inputContainer}>
            <Text style={Styles.label}>Username</Text>
            <TextInput
              style={Styles.input}
              value={username}
              onChangeText={t=>setUsername(t)}
              placeholder="username"
              placeholderTextColor="#999"
            />
          </View>
{/* pass */}
          <View style={Styles.inputContainer}>
            <Text style={Styles.label}>Password</Text>
            <TextInput
              style={Styles.input}
              value={password}
              onChangeText={t=>setPassword(t)}
              placeholder="Password"
              placeholderTextColor="#999"
              secureTextEntry
            />
          </View>
{/* button */}
          {loading===true?<ActivityIndicator/>:<>
          <TouchableOpacity style={Styles.button} onPress={login}>
            <Text style={Styles.buttonText}>Login</Text>
          </TouchableOpacity>
          </>}
          
        </View>
      </View>
    </View>
  );
};

const styles = {
  };