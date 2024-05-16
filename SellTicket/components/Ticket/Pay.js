import { AntDesign, FontAwesome, FontAwesome5, FontAwesome6, Ionicons, MaterialCommunityIcons, MaterialIcons, Octicons } from '@expo/vector-icons';
import React, { useReducer, useState } from "react";
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import MyUserReducer from '../../reducer/MyUserReducer';

export default Pay = ({ route, navigation }) => {
    const [user, dispatch] = useReducer(MyUserReducer, null);
    const { seat } = route.params
    const { tripCarId } = route.params
    const { ticket } = route.params
    const { invoice } = route.params
    const {departure}= route.params
    const {destination} = route.params
    const {date} = route.params
    const {time} = route.params 
    const {pointGo} = route.params
    const {pointUp} = route.params
    const {price} = route.params
    const {quantity} = route.params
    const [count, setCount] = useState(seat);
    const [unitPrice, setUnitPrice] = useState(price); //cho so mac dinh tien ve ở day
    const [selectedOption, setSelectedOption] = useState(null);

    const increaseCount = () => {
        if (count <= quantity && count <= 5) {
            setCount(count + 1);
        }
    };

    const decreaseCount = () => {
        if (count > 0) {
            setCount(count - 1);
        }
    };

    const totalPrice = count * unitPrice;

    const formatCurrency = (value) => {
        // Lấy phần nguyên của giá trị
        const intValue = parseInt(value);

        // Định dạng số tiền với dấu phân cách hàng nghìn
        return intValue.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    };

    const handleOptionSelect = (option) => {
        setSelectedOption(option);
    };

const goToHome = ()=>{
    navigation.navigate("TrangChu",{"title": "Đặt thành công"})
}

    return (
        <MyContext.Provider value={[user, dispatch]}>
            <ScrollView>
                <View style={{ flex: 1 }}>
                    {/* thong tin nguoi dat ve xe */}
                    <View style={styles.ItemUser}>
                        <Text style={{ fontSize: 16, fontWeight: '700', marginBottom: 5 }}>Thông tin người đặt vé</Text>
                        <View style={{ flexDirection: 'row', marginTop: 5 }}>
                            <Ionicons name="person" size={24} color="black" />
                            <Text style={{ marginLeft: 5, fontSize: 15 }} >{user.last_name}</Text>
                        </View>

                        <View style={{ flexDirection: 'row', marginTop: 10 }}>
                            <Ionicons name="call" size={24} color="black" />
                            <Text style={{ marginLeft: 5, fontSize: 15 }} >{user.phone}</Text>
                        </View>

                    </View>

                    {/* thong tin chuyen xe + so luong ve dat */}
                    <View style={styles.ItemBuss}>
                        <Text style={{ fontSize: 16, fontWeight: '700', marginBottom: 5 }}>Thông tin vé xe</Text>
                        <View style={{ flexDirection: 'row', marginTop: 5 }}>
                            <MaterialCommunityIcons name="car-estate" size={24} color="black" />
                            <Text style={{ marginLeft: 5, fontSize: 15 }} >{departure} đến {destination}</Text>
                        </View>

                        <View style={{ flexDirection: 'row', marginTop: 10 }}>
                            <MaterialCommunityIcons name="clock-time-three" size={24} color="black" />
                            <Text style={{ marginLeft: 5, fontSize: 15 }} >Ngày giờ khởi hành: {date} {time}</Text>
                        </View>

                        <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginTop: 15 }}>
                            <View style={{ flexDirection: 'row' }}>
                                <FontAwesome6 name="location-dot" size={24} color="red" />
                                <Text style={{ marginLeft: 5, fontSize: 15 }} >{pointGo}</Text>
                            </View>

                            <Octicons name="arrow-right" size={24} color="black" />

                            <View style={{ flexDirection: 'row' }}>
                                <FontAwesome6 name="location-dot" size={24} color="red" />
                                <Text style={{ marginLeft: 5, fontSize: 15 }} >{pointUp}</Text>
                            </View>

                        </View>

                        <View style={{ flexDirection: 'row', marginTop: 15 }}>
                            <FontAwesome5 name="money-bill-wave" size={24} color="black" />
                            <Text style={{ marginLeft: 5, fontSize: 15 }} >Giá vé: {formatCurrency(price)}VNĐ</Text>
                        </View>

                        <View style={{ flexDirection: 'row', marginTop: 15, justifyContent: 'space-between' }}>
                            <View style={{ flexDirection: 'row' }}>
                                <MaterialIcons name="confirmation-number" size={24} color="black" />
                                <Text style={{ marginLeft: 5, fontSize: 15 }} >Số lượng: </Text>
                            </View>

                            <View style={{ flexDirection: 'row', marginRight: 20 }}>
                                <TouchableOpacity onPress={decreaseCount}>
                                    <AntDesign name="minus" size={20} color="black" />
                                </TouchableOpacity>

                                <Text style={{ fontSize: 17, marginRight: 15, marginLeft: 15 }}>{count}</Text>

                                <TouchableOpacity onPress={increaseCount}>
                                    <FontAwesome5 name="plus" size={19} color="black" />
                                </TouchableOpacity>
                            </View>

                        </View>

                        <View style={{ flexDirection: 'row', marginTop: 15, justifyContent: 'space-between' }}>
                            <View style={{ flexDirection: 'row' }}>
                                <MaterialIcons name="confirmation-number" size={24} color="black" />
                                <Text style={{ marginLeft: 5, fontSize: 15 }} >Tổng tiền: </Text>
                            </View>

                            <View style={{ flexDirection: 'row', marginRight: 20 }}>
                                <Text style={{ marginLeft: 5, fontSize: 17, color: 'red' }} >{formatCurrency(totalPrice)}</Text>
                                <Text style={{ fontSize: 17, marginLeft: 5 }} >VNĐ</Text>
                            </View>

                        </View>
                    </View>

                    {/* phuong thuc thanh toan */}
                    {/* <FontAwesome name="circle" size={24} color="black" /> dấu tròn đã tô */}
                    <View style={styles.ItemPay}>
                        <Text style={{ fontSize: 16, fontWeight: '700', marginBottom: 5 }}>Chọn phương thức thanh toán</Text>

                        <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginTop: 5 }}>
                            <View style={{ flexDirection: 'row' }}>
                                <FontAwesome5 name="money-bill-wave" size={24} color="black" />
                                <Text style={{ marginLeft: 5, fontSize: 15 }}>Thanh toán trực tiếp tại quầy</Text>
                            </View>

                            <TouchableOpacity onPress={() => handleOptionSelect('option1')}>
                                {selectedOption === 'option1' ? (
                                    <MaterialCommunityIcons name="circle-slice-8" size={24} color="black" />
                                ) : (
                                    <FontAwesome name="circle-o" size={24} color="black" />
                                )}
                            </TouchableOpacity>
                        </View>

                        <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginTop: 10 }}>
                            <View style={{ flexDirection: 'row' }}>
                                <AntDesign name="creditcard" size={24} color="black" />
                                <Text style={{ marginLeft: 5, fontSize: 15 }}>Thanh toán bằng Ngân Hàng</Text>
                            </View>

                            <TouchableOpacity onPress={() => handleOptionSelect('option2')}>
                                {selectedOption === 'option2' ? (
                                    <MaterialCommunityIcons name="circle-slice-8" size={24} color="black" />
                                ) : (
                                    <FontAwesome name="circle-o" size={24} color="black" />
                                )}
                            </TouchableOpacity>
                        </View>
                    </View>
                    {selectedOption === 'option1'?             
                    <TouchableOpacity style={styles.ButtonPay} onPress={goToHome}>
                        <Text style={{ color: 'white', fontSize: 18, textAlign: 'center' }}>Đặt vé</Text>
                    </TouchableOpacity>:<TouchableOpacity style={styles.ButtonPay}>
                        <Text style={{ color: 'white', fontSize: 18, textAlign: 'center' }}>Đặt vé</Text>
                    </TouchableOpacity>
                    }
                </View>
            </ScrollView>
        </MyContext.Provider>
    )
}

const styles = StyleSheet.create({
    ItemUser: {
        backgroundColor: 'white',
        width: '94%',
        padding: 12,
        height: 120,
        margin: 10,
        borderRadius: 5,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.8,
        shadowRadius: 5,
        elevation: 5, // Áp dụng cho Android
    },

    ItemBuss: {
        backgroundColor: 'white',
        width: '94%',
        padding: 12,
        height: 300,
        margin: 10,
        borderRadius: 5,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.8,
        shadowRadius: 5,
        elevation: 5, // Áp dụng cho Android
    },

    ItemPay: {
        backgroundColor: 'white',
        width: '94%',
        padding: 12,
        height: 130,
        margin: 10,
        borderRadius: 5,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.8,
        shadowRadius: 5,
        elevation: 5, // Áp dụng cho Android
    },

    ButtonPay: {
        backgroundColor: '#1E90FF',
        padding: 10,
        height: 50,
        margin: 10,
        borderRadius: 50
    }
})