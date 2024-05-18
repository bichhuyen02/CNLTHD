import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, TextInput, ScrollView, TouchableOpacity, } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import Apis, { endpoints } from '../../config/Apis';


export default Search = ({ route, navigation }) => {

    const [province, setProvince] = useState(null);

    const provinceGoId = route.params?.provinceGo

    useEffect(() => {
        const loadProvince = async () => {
            const res = await Apis.get(endpoints['province']);
            setProvince(res.data)
        }
        loadProvince();
    }, [])

    const goToHome = (province) => {
        const { index } = route.params
        if (index === 1) {
            navigation.navigate("Home", { "provinceGo": province })
        }
        else
            navigation.navigate("Home", { "provinceUp": province, "provinceGo": provinceGoId })
    }

    return (<>{province === null ? <View style={styles.searchContainer}>
        <View style={styles.inputWrapper}>
            <AntDesign name="search1" size={24} color="black" style={styles.searchIcon} />
            <TextInput style={styles.inputText} placeholder="Chọn thành phố, khu vực, điểm lên xe ..." />
        </View><Text>Không có dữ liệu</Text></View> :
        <View style={styles.searchContainer}>
            <View style={styles.inputWrapper}>
                <AntDesign name="search1" size={24} color="black" style={styles.searchIcon} />
                <TextInput style={styles.inputText} placeholder="Chọn thành phố, khu vực, điểm lên xe ..." />
            </View>
            <View style={{ marginTop: '5%' }}>
                <View style={styles.ItemSearch}>
                <ScrollView>
                        {province.map(p => (
                            
                            <TouchableOpacity key={p.id} onPress={()=>{goToHome(p.id)}}>
                                <View style={styles.Text}>
                                    <Text style={{ fontSize: 16, fontWeight: 600, marginTop: '5%', marginLeft: '2%' }}>{p.name}</Text>
                                    <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969', marginLeft: '2%' }}> Tất cả các địa điểm lên xe của {p.name}</Text>
                                </View>
                            </TouchableOpacity>
                        ))}
                   </ScrollView>
                </View>
            </View>
        </View>
    }</>
    )
}

const styles = StyleSheet.create({
    searchContainer: {
        margin: 20,
    },
    inputWrapper: {
        flexDirection: 'row',
        alignItems: 'center',
        borderColor: 'blue',
        borderWidth: 1,
        borderRadius: 5,
        paddingLeft: 10,
        backgroundColor: 'white',
    },
    searchIcon: {
        marginRight: 10,
    },
    inputText: {
        flex: 1,
        height: 40,
        paddingLeft: 10,
    },

    ItemSearch: {
        backgroundColor: 'white',
        width: '100%',
        height: 560,
    },
    Text: {
        borderColor: '#C0C0C0',
        borderBottomWidth: 1,
        width: '100%',
        lineHeight: 1.5,
        marginBottom: 9,
    }
})
