import React, { useEffect, useReducer, useState } from "react";
import { StyleSheet, Text, TextInput, TouchableOpacity, View } from "react-native";
import MyUserReducer from "../../reducer/MyUserReducer";
import MyContext from "../../config/MyContext";
import Apis, { endpoints } from "../../config/Apis";

export default ReposeUser = ({route, navigation}) => {
    const {content, setContent} = useState(null)
    const {tripCar} = route.params
    const [user, dispatch] = useReducer(MyUserReducer, null);
    const [inputValue, setInputValue] = useState(null);

    useEffect(()=>{
        const loadComplain = async () =>{
            const res = await Apis.get(endpoints["complain"],{
                params:{
                    "trip": tripCar,
                    "customer": user.id
                }
            })
            setContent(res.data)
        }
        loadComplain();
    },[tripCar])
    const handleInputChange = (text) => {
        setInputValue(text);
    };

    const add = async()=>{
        if(tripCar!=undefined&&tripCar!=""){
        await Apis.post(endpoints['complainT'](tripCar),{
            "content": inputValue
        });}
        navigation.navigate("HistoryOrder", {"title": "thêm thành công"})
    } 

    const update = async()=>{
        if(tripCar!=undefined&&tripCar!=""){
        await Apis.patch(endpoints['complainDetail'](content.id),{
            "content": inputValue
        });}
        navigation.navigate("HistoryOrder", {"title": "sửa thành công"})
    } 
    return (
        <MyContext.Provider value={[user, dispatch]}>
            {content===null?
            <View style={{ flex: 1 }}>
                <TextInput
                    style={styles.Input}
                    placeholder="Nội dung phản hồi giúp nhà xe có sự cải thiện trong công tác chuẩn bị... Cảm ơn quý khách"
                    multiline={true} // Cho phép nhiều dòng
                    numberOfLines={10} // Số dòng hiển thị ban đầu
                    onChangeText={handleInputChange}
                />

                <TouchableOpacity style={styles.button} onPress={update}>
                    <Text style={{ color: 'white', fontSize: 20, textAlign: 'center', fontWeight: '700' }}>Phản hồi ý kiến</Text>
                </TouchableOpacity>
            </View>: 
            <View style={{ flex: 1 }}>
                <TextInput
                    style={styles.Input}
                    placeholder={content.content}
                    multiline={true} // Cho phép nhiều dòng
                    numberOfLines={10} // Số dòng hiển thị ban đầu
                    onChangeText={handleInputChange}
                />

                <TouchableOpacity style={styles.button} onPress={add}>
                    <Text style={{ color: 'white', fontSize: 20, textAlign: 'center', fontWeight: '700' }}>Phản hồi ý kiến</Text>
                </TouchableOpacity>
            </View>
}
        </MyContext.Provider>
    )
}

const styles = StyleSheet.create({
    Input: {
        width: '95%',
        backgroundColor: 'white',
        fontSize: 16,
        padding: 10,
        borderRadius: 10,
        margin: 10,
        height: 300, // Chiều cao của TextInput
        textAlignVertical: 'top', // Căn lề đầu dòng lên trên
    },

    button: {
        width: '95%',
        height: 50,
        margin: 10,
        borderRadius: 30,
        padding: 10,
        backgroundColor: '#3333CC'
    }
})