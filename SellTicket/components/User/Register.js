import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ImageBackground, ScrollView, Image } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { AntDesign, Feather } from '@expo/vector-icons'; // Import icon từ thư viện Expo
import * as ImagePicker from 'expo-image-picker';
import Apis, { endpoints } from '../../config/Apis';


const Register = () => {

  const [user, setUser] = useState({
    'last_name': "",
    'email': "",
    'phone': "",
    'username': "",
    'password': "",
    'cofim_password': "",
    'avatar': ""
  });

  const [loading, setLoading] = useState();

  const change = (field, value) => {
    setUser(current => {
      return { ...current, [field]: value }
    })
  }

  const picker = async () => {
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== "granted") {
      alert("Permission denied!");
    } else {
      const res = await ImagePicker.launchImageLibraryAsync();
      if (!res.canceled) {
        change('avatar', res.assets[0]);
      }
    }
  }

  const handleRegister = async () => {
    setLoading(true);

    try {
      if (user.password === user.cofim_password) {

        let form = new FormData();

        for (key in user) {

          if (key === 'avatar') {

            form.append(key, {
              uri: user[key].uri,
              name: user[key].fileName,
              type: user[key].type
            })
          } else
            form.append(key, user[key]);
        }
        console.info(user.avatar)
        const res = await Apis.post(endpoints['register'], form, {
          headers: {
            "Content-Type": 'multipart/formdata'
          }
        })
        console.info(res.data);
      }
      else {
        alert("2 pass không khớp!!")
      }
    } catch (error) {
      console.error(error);i
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
              onChangeText={t=>change('last_name',t)}
            />
          </View>
          {/* sdt */}
          <View style={styles.inputView}>
            <AntDesign name="phone" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="SĐT"
              placeholderTextColor="#fff"
              onChangeText={t=>change('phone',t)}
            />
          </View>
          {/* mail */}
          <View style={styles.inputView}>
            <AntDesign name="mail" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="Email"
              placeholderTextColor="#fff"
              onChangeText={t=>change('email',t)}
            />
          </View> 
          {/* username  */}
          <View style={styles.inputView}>
            <AntDesign name="user" size={24} color="#fff" style={styles.icon} />
            <TextInput
              style={styles.inputText}
              placeholder="Tên đăng nhập"
              placeholderTextColor="#fff"
              onChangeText={t=>change('username',t)}
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
              onChangeText={t=>change('password',t)}
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
              onChangeText={t=>change('cofim_password',t)}
            />
          </View>
          {/* ava  */}
          <TouchableOpacity style={styles.inputView} onPress={picker}>
            <Feather name="file" size={24} color="#fff" style={styles.icon} />
            <Text style={[styles.inputText, { marginTop: 30 }]}>Tải ảnh đại diện</Text>
          </TouchableOpacity>

          {user.avatar!==""?<Image source={{uri: user.avatar.uri}} style={{width: 100, height: 100, margin: 10}}>
          </Image>:""}
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
