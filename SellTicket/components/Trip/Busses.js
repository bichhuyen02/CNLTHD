import { AntDesign, FontAwesome, Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import React, { useEffect, useState } from "react";
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import Apis, { endpoints } from '../../config/Apis';

export default Busses = ({ route, navigation }) => {
    const [car, setCar] = useState(null);
    const [carId, setCarId] = useState(null);
    const [trip, setTrip] = useState(null);
    const { pointGo } = route.params
    const { pointUp } = route.params
    const { date } = route.params
    const { seat } = route.params
    useEffect(() => {
        const loadTrip = async () => {
            if (date !== undefined && date !== "") {
                const res = await Apis.get(endpoints['trip'], {
                    params: {
                        'dateGo': date
                    }
                });
                setTrip(res.data)
            }
        }
        loadTrip();  
    }, [pointUp]);
    
    useEffect(()=>{
        const loadTripCar = async () => {
            if (trip !== null) {
                if (pointGo !== undefined && pointGo !== "") {
                    if (pointUp !== undefined && pointUp !== "") {
                        const tripCarArray = [];
                        trip.map(async (t) => {
                            const res = await Apis.get(endpoints['tripCar'], {
                                params: {
                                    'trip': t.id
                                }
                            });
                            tripCarArray.push(res.data);
                        })
                        setTripCar(tripCarArray)
                    }
                }
            }
        }
        const loadCar = async () => {
            if (trip !== null) {
                const carArray = [null];
                trip.map(async (t) => {
                    const res = await Apis.get(endpoints['carDetail'](t.car));
                    carArray.push(res.data);
                })
                setCar(carArray)
            }
        }
        loadTripCar()
        loadCar();
    })
    return (<>
        {tripCar === null ? <Text>Không có dữ liệu</Text> : <>
            {tripCar.map(t => {
                <ScrollView style={{ flex: 1, backgroundColor: '#F0F0F0' }}>
                <TouchableOpacity style={styles.Item} onPress={() => navigation.navigate("Ticket", { "tripCarId": t.id, "seat": seat, "carId": carId })} >
                    <View style={{ flexDirection: 'row', justifyContent: 'space-between', padding: 12 }}>
                        <Text style={{ fontSize: 16, fontWeight: '700' }}>{trip.map(tc => {
                            car.map(c => {
                                if (tc.id == t.trip) { if (tc.car == c.id) { setCarId(c.id);
                                    return c.name } }
                            })
                        })}</Text>
                        <Text style={{ fontSize: 16, fontWeight: '700', color: '#3366CC' }}>{t.price} VNĐ
                            <Text style={{ fontSize: 14, fontWeight: '400', color: '#808080' }}>/chỗ</Text>
                        </Text>
                    </View>

                    <Text style={{ marginLeft: 10, marginTop: 5, marginBottom: 10 }}>Số ghế trống: {trip.map(tc => {
                        if (tc.id == t.trip) { return tc.quantity }
                    })}
                        <Text style={{ fontSize: 14, fontWeight: '400', color: 'red' }}>/{trip.map(tc => {
                            car.map(c => {
                                if (tc.id == t.trip) { if (tc.car == c.id) { return c.quantity } }
                            })
                        })}</Text>
                    </Text>

                    <View style={{ marginTop: 10, marginLeft: 5, marginBottom: 10 }}>
                        <View style={{ flexDirection: 'row', width: '100%' }}>
                            <Text style={{ width: '13%', textAlign: 'center' }}>04:30</Text>
                            <FontAwesome name="circle-o" size={24} color="black" style={{ width: '10%' }} />
                            <Text style={{ width: '70%' }}>{t.pointGo}</Text>
                        </View>

                        <View style={{ flexDirection: 'row' }}>
                            <Ionicons name="ellipsis-vertical-outline" size={24} color="black" style={{ marginLeft: '12.5%' }} />
                        </View>

                        <View style={{ flexDirection: 'row', width: '100%' }}>
                            <Text style={{ width: '13%', textAlign: 'center' }}>06:30</Text>
                            <FontAwesome name="circle" size={24} color="black" style={{ width: '10%' }} />
                            <Text style={{ width: '70%' }}>{t.pointUp}</Text>
                        </View>
                    </View>

                    <View style={styles.icon}>
                        <AntDesign name="customerservice" size={18} color="black" />
                        <Ionicons name="wifi" size={18} color="black" />
                        <MaterialCommunityIcons name="usb-port" size={18} color="black" />
                        <MaterialCommunityIcons name="battery-charging" size={18} color="black" />
                        <MaterialCommunityIcons name="presentation-play" size={18} color="black" />
                    </View>
                </TouchableOpacity>
            </ScrollView>
            })}</>
        }
    </>)
}

const styles = StyleSheet.create({
    Item: {
        backgroundColor: 'white',
        borderRadius: 5,
        margin: 10,
        width: '95%',
        height: 230,
        padding: 10,
        margin: 10
    },

    icon: {
        flexDirection: 'row',
        borderWidth: 1,
        borderColor: '#C0C0C0',
        borderRadius: 10,
        padding: 5,
        width: 120,
        justifyContent: 'space-evenly',
        marginTop: 3,
        marginLeft: 10
    }
})