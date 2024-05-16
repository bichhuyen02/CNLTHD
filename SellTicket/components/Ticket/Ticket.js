import { AntDesign, Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import { createMaterialTopTabNavigator } from "@react-navigation/material-top-tabs";
import React, { useEffect } from "react";
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { FontAwesome } from '@expo/vector-icons';
import Apis, { endpoints } from '../../config/Apis';



export default Ticket = ({ route, navigation }) => {
    const { tripCarId } = route.params
    const { carId } = route.params
    const { seat } = route.params
    const [ticket, setTicket] = useState(null);
    const [invoice, setInvoice] = useState(null);
    const [tripCar, setTripCar] = useState(null);
    const [trip, setTrip] = useState(null);
    const [bues, setBues] = useState(null);
    const [car, setCar] = useState(null);
    const [category, setCategory] = useState(null);

    const Tab = createMaterialTopTabNavigator();

    useEffect(() => {
        const loadCar = async () => {
            if (carId !== undefined && carId !== "") {
                const res = await Apis.get(endpoints['carDetail'](carId));
                setCar(res.data)
            }
        }
        const loadTripCar = async () => {
            if (tripCarId !== undefined && tripCarId !== "") {
                const res = await Apis.get(endpoints['tripCarDetail'](tripCarId));
                setTripCar(res.data)
            }
        }
        loadCar();
        loadTripCar();
    }, [tripCarId]);

    useEffect(()=>{
        const loadCategory = async () => {
            if (car !== null) {
                const res = await Apis.get(endpoints['categoryDetail'](car.category));
                setCategory(res.data)
            }
        }

        const loadTrip = async () => {
            if (tripCar !== null) {
                const res = await Apis.get(endpoints['tripDetail'](tripCar.trip));
                setTrip(res.data)
            }
        }

        const loadBues = async () => {
            if (trip !== null) {
                const res = await Apis.get(endpoints['buesDetail'](trip.bues));
                setBues(res.data)
            }
        }
        loadCategory();
        loadTrip();
        loadBues();
    });

    function DacTrung() {
        return (
            <ScrollView style={{ flex: 1, backgroundColor: '#F0F0F0' }}>
                <View style={styles.ItemDT} onPress={() => navigation.navigate("Ticket")}>
                    <View style={{ margin: '4%', }}>
                        <View style={styles.InputText}>
                            <Text style={{ fontSize: 16, fontWeight: 600 }}> {category.name} </Text>
                            <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969' }}> Ghế ngồi {car.quantity} chỗ</Text>
                        </View>

                        <View style={styles.InputText}>
                            <Text style={{ fontSize: 16, fontWeight: 600 }}> Thông tin xe </Text>
                            <View style={{ marginBottom: 8, marginTop: 5, marginLeft: '2%', color: '#696969' }}>
                                <Text>Kiểu ghế ngồi 1-1 </Text>
                                <Text>Sức chứa của xe</Text>
                            </View>
                        </View>

                        <View style={styles.InputText}>
                            <Text style={{ fontSize: 16, fontWeight: 600 }}> Tiện ích </Text>
                            <View style={{ flexDirection: 'row', marginBottom: 8, marginTop: 15, justifyContent: 'space-evenly' }}>
                                <AntDesign name="customerservice" size={20} color="green" />
                                <Ionicons name="wifi" size={20} color="black" />
                                <MaterialCommunityIcons name="usb-port" size={20} color="black" />
                                <MaterialCommunityIcons name="battery-charging" size={20} color="black" />
                                <MaterialCommunityIcons name="presentation-play" size={20} color="black" />
                            </View>
                        </View>

                        <View>
                            <Text style={{ fontSize: 16, fontWeight: 600 }}> Chính sách đổi hoàn trả </Text>
                            <Text style={styles.Text}> Không áp dụng đổi lịch trình</Text>
                        </View>
                    </View>

                </View>

                <View style={{ marginTop: '5%' }}>
                    <View style={styles.ItemDT2}>
                        <View>
                            <Text style={{ marginTop: '2%', marginLeft: '3%' }}>Đánh giá của hành khách</Text>

                            <View style={{ flexDirection: 'row' }}>
                                <Text style={styles.Text2}>4.3/5</Text>
                                <Text style={{ left: 168, color: '#696969' }}>Lái xe</Text>
                                <Text style={{ left: 184, color: '#1E90FF' }}>4.3/5</Text>
                                <Text style={{ top: 20, left: 97, color: '#696969' }}>Tiện ích</Text>
                                <Text style={{ top: 20, left: 103, color: '#1E90FF' }}>4.3/5</Text>
                                <Text style={{ top: 40, left: 16, color: '#696969' }}>Dịch vụ</Text>
                                <Text style={{ top: 40, left: 24, color: '#1E90FF' }}>4.3/5</Text>
                            </View>
                        </View>
                    </View>
                </View>
            </ScrollView>

        )
    }
    /*ve*/
    function Ve() {
        return (
            <View>
                <Text style={{ fontSize: 14, marginTop: 10, marginLeft: '5%', color: 'blue' }}>Thông tin quan trọng</Text>
                <View style={styles.ItemVe}>
                    <Text style={{ fontSize: 18, fontWeight: 600, marginTop: '2%', left: '5%' }}>Điều khoản và điều kiện</Text>
                    <View style={{ fontSize: 20, marginTop: 10, marginLeft: '5%' }}>
                        <View style={styles.text1}>
                            <Text>• Vé khởi hành trong giai đoạn Cuối năm và Tết Nguyên đán có thể không được hoàn, đổi lịch.</Text>
                            <Text>•	Yêu cầu đeo khẩu trang khi lên xe </Text>
                            <Text>•	Có mặt tại văn phòng/quầy vé/bến xe trước 15 phút để làm thủ tục lên xe </Text>
                            <Text>• Không mang đồ ăn, thức ăn có mùi lên xe </Text>
                            <Text>•	Không hút thuốc, uống rượu, sử dụng chất kích thích trên xe </Text>
                            <Text>•	Không mang các vật dễ cháy nổ lên xe </Text>
                            <Text>•	Không vứt rác trên xe </Text>
                        </View>
                    </View>


                </View>
            </View>
        )
    }

    function TuyenDuong() {
        return (
            <View>
                <Text style={{ fontSize: 20, marginTop: 10, marginLeft: '5%' }}>Lịch trình</Text>
                <View style={styles.Item}>
                    <View style={{ marginTop: 10, marginLeft: 5, marginBottom: 10 }}>
                        <View style={{ flexDirection: 'row', width: '100%' }}>
                            <Text style={{ width: '13%', textAlign: 'center' }}>04:30</Text>
                            <FontAwesome name="circle-o" size={24} color="#00CCFF" style={{ width: '10%' }} />
                            <Text style={{ width: '70%' }}>{tripCar.pointGo}</Text>
                        </View>

                        <View style={{ flexDirection: 'row' }}>
                            <Ionicons name="ellipsis-vertical-outline" size={24} color="black" style={{ marginLeft: '12.5%' }} />
                        </View>

                        <View style={{ flexDirection: 'row', width: '100%' }}>
                            <Text style={{ width: '13%', textAlign: 'center' }}>06:30</Text>
                            <FontAwesome name="circle" size={24} color="#00CCFF" style={{ width: '10%' }} />
                            <Text style={{ width: '70%' }}>{tripCar.pointUp}</Text>
                        </View>
                    </View>

                    <View style={styles.icon}>
                        <AntDesign name="customerservice" size={18} color="black" />
                        <Ionicons name="wifi" size={18} color="black" />
                        <MaterialCommunityIcons name="usb-port" size={18} color="black" />
                        <MaterialCommunityIcons name="battery-charging" size={18} color="black" />
                        <MaterialCommunityIcons name="presentation-play" size={18} color="black" />
                    </View>
                </View>
                <Text style={{ fontSize: 20, marginTop: 10, marginLeft: '5%' }}>Tuyến đường</Text>
                <View style={styles.ItemTD}>
                    <Text>{bues.departure} - {bues.destination}</Text>
                </View>
            </View>
        )
    }

    return (
        <View style={{ flex: 1 }}>
            <Tab.Navigator>
                <Tab.Screen name="DacTrung" component={DacTrung} options={{ title: 'Đặc trưng' }} />
                <Tab.Screen name="Ve" component={Ve} options={{ title: 'Vé' }} />
                <Tab.Screen name="TuyenDuong" component={TuyenDuong} options={{ title: 'Tuyến đường' }} />
            </Tab.Navigator>

            <View style={{ flex: 0.1, padding: 10, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', backgroundColor: 'white', borderTopWidth: 1, borderColor: '#C0C0C0' }}>
                <Text style={{ fontSize: 20, fontWeight: '700', color: '#3366CC' }}>150.000 VNĐ
                    <Text style={{ fontSize: 16, fontWeight: '400', color: '#808080' }}>/chỗ</Text>
                </Text>
                <TouchableOpacity style={{ backgroundColor: '#1E90FF', paddingTop: 10, paddingBottom: 10, paddingLeft: 30, paddingRight: 30, borderRadius: 5 }}
                    onPress={() => navigation.navigate("Pay",{"seat":seat, "tripCarId": tripCarId, "ticket": ticket, "invoice": invoice, 
                        "departure": bues.departure, "destination": bues.destination, "date": trip.dateGo, "time": trip.timeGo, 
                        "pointGo": tripCar.pointGo, "pointUp": tripCar.pointUp, "price": tripCar.price, "quantity": trip.quantity
                    })}>
                    <Text style={{ color: 'white', fontSize: 18 }}>Chọn</Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}
const styles = StyleSheet.create({
    ItemDT: {
        top: 18,
        left: 18,
        right: 18,
        backgroundColor: 'white',
        width: '91%',
        height: 400,
    },

    InputText: {
        borderColor: '#C0C0C0',
        borderBottomWidth: 1,
        width: '100%',
        lineHeight: 1.5,
        marginBottom: 15,

    },

    Text: {
        width: '60%',
        backgroundColor: '#696969',
        borderRadius: 5,
        marginBottom: 8,
        marginTop: 8,
        color: '#fff',
        padding: 2,
    },

    ItemDT2: {
        top: 18,
        left: 18,
        right: 18,
        backgroundColor: 'white',
        width: '91%',
        height: 120,
    },

    Text2: {
        color: '#1E90FF',
        fontSize: 22,
        marginBottom: '2%',
        marginLeft: '3%',
    },

    ItemVe: {
        top: 18,
        backgroundColor: 'white',
        width: '100%',
        height: '70%',

    },

    Item: {
        backgroundColor: 'white',
        borderRadius: 5,
        margin: 10,
        width: '90%',
        height: 150,
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
    },

    ItemTD: {
        backgroundColor: 'white',
        borderRadius: 5,
        width: '90%',
        height: 60,
        padding: 10,
    },

    text1: {
        fontSize: 18,
        lineHeight: 1.5,
        marginBottom: 19,
    }

})