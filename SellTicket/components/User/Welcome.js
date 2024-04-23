import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ImageBackground } from 'react-native';

const Welcome = ({ navigation }) => {
  const handleLogin = () => {
    // Xử lý khi nhấn nút Đăng nhập
    navigation.navigate('Đăng nhập'); // Chuyển đến màn hình đăng nhập
  };

  const handleRegister = () => {
    // Xử lý khi nhấn nút Đăng ký
    navigation.navigate('Signup'); // Chuyển đến màn hình đăng ký
  };

  return (
    <ImageBackground source={{uri: 'https://res.cloudinary.com/dgsii3nt1/image/upload/v1713677765/xinchao_k8lrre.jpg'}} style={styles.background}>
      <View style={styles.overlay}>
        <View style={styles.container}>
             <TouchableOpacity style={styles.button} onPress={handleLogin}>
            <Text style={styles.buttonText}>Đăng nhập</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={handleRegister}>
            <Text style={styles.buttonText}>Đăng ký</Text>
          </TouchableOpacity>
        </View>
      </View>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  background: {
    flex: 1,
    resizeMode: 'cover',
    justifyContent: 'center',
   
  },
  overlay: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: 'rgba(0, 0, 0, 0.25)', // Màu mờ (màu đen có độ mờ 50%)
  },
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  button: {
    backgroundColor: '#fff',
    paddingVertical: 15,
    paddingHorizontal: 40,
    borderRadius: 25,
    bottom:130,
    marginBottom:10,
    width: 300,
  },
  buttonText: {
    color: '#764ba2',
    fontSize: 18,
    textAlign:'center',
  },
});

export default Welcome;
