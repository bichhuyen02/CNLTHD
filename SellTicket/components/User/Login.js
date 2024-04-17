import React, { useState } from 'react';
import { View, Text, Image, TextInput, TouchableOpacity, ActivityIndicator } from 'react-native';
import Apis, { authApi, endpoints } from '../../Apis';
import MyContext from '../../MyContext';

export default Login = ({navigation}) => {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    const [user, dispatch] = useState(MyContext);
    const [loading, setLoading] = useState();

    const login =  async () => {
      setLoading(true);
      try {
          let res = await Apis.post(endpoints['login'], {
              'client_id': 'giKPdDSiFGtLG0JfzhgxZ0MHwubYmLVFqXte33Dd',
              'client_secret': 'YGpXRhe2qS8d41hLXwaHgtQ3LTxqEeS3M2Lo50Wo3zG3hZzmQmeTY7Gta39aUUj2TwN8oDMBuXNZZy5K4pWplruEDBVeH0c7NOozQ3kC0ibwA7WOJQcHmiW2245IGUmW',
              'username': username,
              'password': password,
              'grant_type': 'password'
          })
          console.info(res.data)
          await AsyncStorage.setItem('token-access', res.data.access_token)
          let user = await authApi(res.data.access_token).get(endpoints['current_user']);
          console.info(user.data)
          dispatch({
                      'type': 'login',
                      'payload': {
                          'username': user.data.username
                      }
                  })
          navigation.navigate("Login");
      } catch (error) {
          console.error(error);
      } finally{
          setLoading(false);
      }
      // if(username==="admin"&&password==="123"){
      //     dispatch({
      //         'type': 'login',
      //         'payload': {
      //             'username': 'admin'
      //         }
      //     })
      //     alert("Đăng nhập thanh công!");
      // }else
      //     alert("Đăng nhập không thanh công!");
  }


  return (
    <View style={styles.container}>
      <Image
        source={{uri: 'https://www.bootdey.com/image/280x280/20B2AA/20B2AA'}}
        style={styles.background}
      />
      <View style={styles.logoContainer}>
        <Image
          source={{uri: 'https://www.bootdey.com/img/Content/avatar/avatar7.png'}}
          style={styles.logo}
        />
      </View>
      <View style={styles.formContainer}>
        <Text style={styles.title}>Login</Text>
        <View style={styles.card}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Username</Text>
            <TextInput
              style={styles.input}
              value={username}
              onChangeText={setUsername}
              placeholder="username"
              placeholderTextColor="#999"
            />
          </View>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Password</Text>
            <TextInput
              style={styles.input}
              value={password}
              onChangeText={setPassword}
              placeholder="Password"
              placeholderTextColor="#999"
              secureTextEntry
            />
          </View>
          {loading===true?<ActivityIndicator/>:<>
          <TouchableOpacity style={styles.button} onPress={login}>
            <Text style={styles.buttonText}>Login</Text>
          </TouchableOpacity>
          </>}
        </View>
      </View>
    </View>
  );
};

const styles = {
  container: {
    flex: 1,
  },
  background: {
    width: '100%',
    height: '100%',
    position: 'absolute',
  },
  logoContainer: {
    alignItems: 'center',
    marginTop: 50,
  },
  logo: {
    width: 120,
    height: 120,
    borderRadius:60,
    resizeMode: 'contain',
  },

    formContainer: {
      justifyContent: 'center',
      alignItems: 'center',
    },
    title: {
      fontSize: 24,
      color: '#fff',
      marginBottom: 20,
      marginTop: 20,
    },
    card: {
      width: '80%',
      backgroundColor: '#fff',
      borderRadius: 4,
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.2,
      shadowRadius: 2,
      padding: 20,
      marginBottom: 20,
    },
    inputContainer: {
      marginBottom: 20,
    },
    label: {
      fontSize: 16,
      color: '#333',
    },
    input: {
      height: 40,
      borderRadius:6,
      borderWidth: 1,
      borderColor: '#ddd',
      color: '#333',
      paddingLeft:10,
    },
    button: {
      width: '100%',
      height: 40,
      backgroundColor: '#00BFFF',
      alignItems: 'center',
      justifyContent: 'center',
      borderRadius: 4,
    },
    buttonText: {
      color: '#fff',
      fontSize: 16,
    },
  };