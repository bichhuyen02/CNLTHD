import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ImageBackground, ScrollView, Image } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { AntDesign, Feather } from '@expo/vector-icons'; // Import icon từ thư viện Expo
import Apis, { endpoints } from '../../config/Apis';


const Register = () => {

  const [last_name, setLast_name] = useState(null)
  const [email, setEmail] = useState(null)
  const [phone, setPhone] = useState(null)
  const [username, setUsername] = useState(null)
  const [password, setPass] = useState(null)
  const [cofim_password, setConf] = useState(null)

  const [loading, setLoading] = useState();


  const handleRegister = async () => {
    setLoading(true);

    try {
      if (password === cofim_password) {
        const res = await Apis.post(endpoints['register'], {
          "last_name": last_name,
          "email": email, 
          "phone": phone,
          "username": username,
          "password": password
        })
        console.info(res.data);
      }
      else {
        alert("2 pass không khớp!!")
      }
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <LinearGradient colors={['#2D99AE', '#764ba2']} style={styles.container}>
      <View style={styles.formContainer}>
        <Text style={styles.title}>Đăng ký tài khoản</Text>
        <ScrollView>
          {/* tên */}
          <View style={styles.inputView}>
            <AntDesign name="user" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="Họ tên"
              placeholderTextColor="#fff"
              onChangeText={(t)=>{setLast_name(t)}}
            />
          </View>
          {/* sdt */}
          <View style={styles.inputView}>
            <AntDesign name="phone" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="SĐT"
              placeholderTextColor="#fff"
              onChangeText={(t)=>{setPhone(t)}}
            />
          </View>
          {/* mail */}
          <View style={styles.inputView}>
            <AntDesign name="mail" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="Email"
              placeholderTextColor="#fff"
              onChangeText={(t)=>{setEmail(t)}}
            />
          </View> 
          {/* username  */}
          <View style={styles.inputView}>
            <AntDesign name="user" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="Tên đăng nhập"
              placeholderTextColor="#fff"
              onChangeText={(t)=>{setUsername(t)}}
            />
          </View>
          {/* pass  */}
          <View style={styles.inputView}>
            <AntDesign name="lock" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="Mật khẩu"
              placeholderTextColor="#fff"
              secureTextEntry={true}
              onChangeText={(t)=>{setPass(t)}}
            />
          </View>
          {/* comfi */}
          <View style={styles.inputView}>
            <AntDesign name="lock" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="Nhập lại mật khẩu"
              placeholderTextColor="#fff"
              secureTextEntry={true}
              onChangeText={(t)=>{setConf(t)}}
            />
          </View>

          {/* but  */}
          <TouchableOpacity style={styles.registerButton} onPress={handleRegister}>
            <Text style={styles.registerButtonText}>Đăng ký</Text>
          </TouchableOpacity>
        </ScrollView>
      </View>

    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  formContainer: {
    width: '80%',
    borderWidth: 2,
    borderRadius: 25,
    padding: 20,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingHorizontal: 20,
    paddingTop: 40,
    borderColor: '#fff',
    borderStyle: 'solid',
  },
  title: {
    fontSize: 24,
    color: '#fff',
    textAlign: 'center',
    marginBottom: 20,
  },
  inputView: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.3)',
    borderRadius: 25,
    height: 50,
    marginBottom: 20,
    paddingHorizontal: 20,
  },
  inputText: {
    flex: 1,
    height: 50,
    color: '#fff',
  },
  avatarButton: {
    backgroundColor: '#fff',
    borderRadius: 25,
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 20,
  },
  avatarButtonText: {
    color: '#764ba2',
    fontSize: 16,
  },
  registerButton: {
    backgroundColor: '#fff',
    borderRadius: 25,
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
  },
  registerButtonText: {
    color: '#764ba2',
    fontSize: 18,
  },
  icon: {
    marginRight: 10,
  },
});

export default Register;
