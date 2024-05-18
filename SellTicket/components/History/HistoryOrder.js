import React, { useEffect, useReducer, useState } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";
import MyUserReducer from "../../reducer/MyUserReducer";
import Apis, { endpoints } from "../../config/Apis";


export default HistoryOrder = ({ route, navigation }) => {
    const [user, dispatch] = useReducer(MyUserReducer, null);
    const [ticket, setTicket] = useState(null)
    const [tripCar, setTripCar] = useState(null)
    const [trip, setTrip] = useState(null)
    const [buse, setBuse] = useState(null)
    const [customer, setCustomer] = useState(null)

    useEffect(() => {
        const loadCustomer = async () => {
            const res = await Apis.get(endpoints['customers'], {
                params: {
                    "user": user.id
                }
            });
            setCustomer(res.data);
        }
        loadCustomer();
    }, []);

    useEffect(() => {
        if (customer != null) {
            const loadTicket = async () => {
                const res = await Apis.get(endpoints['ticketCustomer'](customer.Id));
                setTicket(res.data)
            }
            loadTicket();
        }
    });
    const load = async (tripCarId) => {
        const res = await Apis.get(endpoints['tripCarDetail'](tripCarId));
        setTripCar(res.data)

        if (tripCar != null) {
            const loadTrip = async () => {
                const res = await Apis.get(endpoints['tripDetail'](tripCar.trip));
                setTrip(res.data)
            }
            loadTrip();
        }
        if (trip != null) {
            constloadBuse = async () => {
                const res = await Apis.get(endpoints['buesDetail'](trip.bues));
                setBuse(res.data)
            }
            loadBuse();
        }
    }
    const goToReposes = (tripCar) => {
        navigation.navigate("Reposes", { "tripCar": tripCar })
    }
    const mess = ()=>{
        Alert.alert(
            'Thông báo',
            'Chuyến xe chưa chạy không thể phản hồi',
            [
              { text: 'OK', onPress: () => console.log('OK pressed') }
            ],
            { cancelable: false }
          );
    }
    return (
        <MyContext.Provider value={[user, dispatch]}>
            {ticket === null ? <Text></Text> : <>
                {ticket.map(t => {
                    load(t.trip);
                    <View style={{ flex: 1 }}>
                        <View style={styles.Item}>
                            <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
                                <Text style={{ fontSize: 16, fontWeight: '600' }}>user.last_name</Text>
                                <Text style={{ fontSize: 16, fontWeight: '600', color: '#FF4500' }}>{buse.departure} - {buse.destination}</Text>
                            </View>

                            <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginTop: 5 }}>
                                <Text style={{ fontSize: 15 }}>Số ghế đã đặt: {t.quantity}</Text>
                                <Text style={{ fontSize: 15 }}>Giá tiền: {t.quantity * tripCar.price} VNĐ</Text>
                            </View>

                            <Text style={{ fontSize: 15, marginTop: 5 }}>Ngày giờ khởi hành: {trip.dateGo} {trip.timeGo}</Text>
                            <Text style={{ fontSize: 15, marginTop: 5 }}>Ngày đặt vé: {ticket.created_date}</Text>

                            <View style={{ flexDirection: 'row', marginTop: 8, justifyContent: 'space-around' }}>
                                {/* {trip.complete === true ? <><View style={styles.state}>
                                    <Text style={{ fontSize: 15, color: 'green', fontWeight: '600', textAlign: 'center' }}>Hoàn thành</Text>
                                </View>
                                    <TouchableOpacity style={styles.reponse} onPress={goToReposes(t.trip)}>
                                        <Text style={{ textAlign: 'center', color: 'red' }}>Phản hồi về chuyến đi</Text>
                                    </TouchableOpacity></> :
                                    <><View style={styles.state}>
                                        <Text style={{ fontSize: 15, color: 'green', fontWeight: '600', textAlign: 'center' }}>Chưa Hoàn thành</Text>
                                    </View>
                                        <TouchableOpacity style={styles.reponse} onPress={mess()}>
                                            <Text style={{ textAlign: 'center', color: 'red' }}>Phản hồi về chuyến đi</Text>
                                        </TouchableOpacity>
                                    </>
                                } */}
                            </View>
                        </View>
                    </View>
                })}</>}
        </MyContext.Provider>
    )
};

const styles = StyleSheet.create({
    Item: {
        backgroundColor: 'white',
        height: 165,
        width: '94%',
        padding: 10,
        marginTop: 15,
        marginLeft: 15,
        marginRight: 15,
        borderRadius: 10,
        borderColor: '#DCDCDC',
        borderWidth: 1,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.8,
        shadowRadius: 5,
        elevation: 5, // Áp dụng cho Android
    },

    state: {
        borderColor: 'green',
        borderWidth: 1,
        borderRadius: 5,
        height: 35,
        width: '30%',
        padding: 5
    },

    reponse: {
        borderColor: 'red',
        borderWidth: 1,
        borderRadius: 5,
        height: 35,
        width: '53%',
        padding: 5
    }
});