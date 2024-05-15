import React, { useEffect, useState } from 'react'
import {StyleSheet,View, Text, TouchableOpacity, Image, ScrollView, StatusBar, TextInput } from 'react-native'
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { Fontisto } from '@expo/vector-icons';
import { Picker } from '@react-native-picker/picker';
import DateTimePicker from '@react-native-community/datetimepicker';
import { endpoints } from '../../config/Apis';



export default Home = ({route, navigation}) => {
  const [date, setDate] = useState(new Date());
  const [showPicker, setShowPicker] = useState(false);

  const onChange = (event, selectedDate) => {
    const currentDate = selectedDate || date;
    setShowPicker(false);
    setDate(currentDate);
  };

  const showDateTimePicker = () => {
    setShowPicker(true);
  };

  const [seats, setSeats] = useState(1);

  const [pointGo, setPointGo] = useState(null);
  const [pointUp, setPointUp] = useState(null);

  const pointGoId = route.params?.pointGo
  const pointUpId = route.params?.pointUp

  useEffect(() => {
    const loadPointGo = async () => {
      if (pointGoId !== undefined && pointGoId !== "") {
        const res = await Apis.get(endpoints['bStationDetail'](pointGoId));
        setPointGo(res.data)
      }
    }
    const loadPointUp = async () => {
      if (pointUpId !== undefined && pointUpId !== "") {
        const res = await Apis.get(endpoints['bStationDetail'](pointUpId));
        setPointUp(res.data)
      }
    }
    loadPointGo()
    loadPointUp();
  }, [pointUpId]);

  const handleSeatChange = (value) => {
    setSeats(value);
  };

  const data = [
    {
        image: require('./Image/CV.jpg')
    },
    {
        image: require('./Image/hinhCV.jpg')
    },
    {
        image: require('./Image/hinhCV1.jpg')
    },
];

const goToSearch = (index) => {
  navigation.navigate("Search", {"index": index})
}


  return(
        <View style={{flex:1}}>
         <StatusBar barStyle="light-content" />
            {/* khung tim kiem */}
        <View style={{flex: 2, backgroundColor: '#1E90FF', position: 'relative'}}>
          <View style={{padding: 10, paddingTop: 15}}>
            <View style={{flexDirection: 'row', alignItems: 'center', justifyContent: 'center'}}>
            
            <Text style={{color: 'white', fontSize: 20, fontWeight: '700'}}>BUS APP 5 SAO - TIỆN ÍCH ĐỈNH CAO</Text>
            </View>
          </View>
        </View>
        {/* #F0F0F0 */}
        <View style={{flex: 8, backgroundColor: '#F0F0F0'}}>
        </View>
        

        <View style={styles.ItemSreach}>
          <View  style={{width:'95%', height:'95%'}}>

            <View style={{margin:10}}>
              <Text style={{fontSize: 18}}>Từ</Text>
              <View style={{flexDirection: 'row'}}>
                <MaterialCommunityIcons name="car-arrow-left" size={24} color="#0000FF" style={{marginRight: 5}} />
                <TouchableOpacity
                  style={styles.InputText}
                  onPress={()=>goToSearch(1)}>
                  {pointGo===null?<Text style={{ color: '#808080' }} >Thành phố, khu vực, điểm lên xe</Text>:
                  <Text style={{ color: '#808080' }} >{pointGo.name}</Text>}
                </TouchableOpacity>
              </View>
            </View>

            <View style={{margin:10}}>
              <Text style={{fontSize: 18}}>Đến</Text>
              <View style={{flexDirection: 'row'}}>
                <MaterialCommunityIcons name="car-arrow-right" size={24} color="#0000FF" style={{marginRight: 5}} />
                <TouchableOpacity
                  style={styles.InputText}
                  onPress={()=>goToSearch(2)}>
                   {pointUp===null?<Text style={{ color: '#808080' }} >Thành phố, khu vực, điểm lên xe</Text>:
                  <Text style={{ color: '#808080' }} >{pointUp.name}</Text>}
                </TouchableOpacity>
              </View>
            </View>

            <View style={{ margin: 10 }}>
              <Text style={{ fontSize: 18 }}>Ngày khởi hành</Text>
              <View style={{ flexDirection: 'row' }}>
                <TouchableOpacity onPress={showDateTimePicker}>
                  <Fontisto name="date" size={24} color="#0000FF" style={{ marginRight: 10 }} />
                </TouchableOpacity>
                <TextInput
                  style={styles.InputText}
                  placeholder="Ngày khởi hành"
                  value={date.toDateString()} // Hiển thị ngày được chọn
                  editable={false}
                />
              </View>
              {showPicker && (
                <DateTimePicker
                  value={date}
                  mode="date"
                  display="default"
                  onChange={onChange}
                />
              )}
            </View>
           
            <View style={styles.container}>
              <Text style={styles.title}>Ghế</Text>
              <View style={styles.inputContainer}>
                <MaterialCommunityIcons name="seat-passenger" size={24} color="#808080" style={styles.icon} />
                <Picker
                  selectedValue={seats}
                  style={styles.picker}
                  onValueChange={handleSeatChange}
                >
                  <Picker.Item label="1 ghế" value={1} />
                  <Picker.Item label="2 ghế" value={2} />
                  <Picker.Item label="3 ghế" value={3} />
                  <Picker.Item label="4 ghế" value={4} />
                </Picker>
              </View>
            </View>


            <TouchableOpacity  style={styles.buttonSreach} onPress={() => navigation.navigate("Busses", {'pointGo': pointGoId, 'pointUp': pointUpId, 'date': date, 'seat': seats})}>
              <Text style={{fontSize: 20, color: 'white', textAlign: 'center', fontWeight: '600'}}>Tìm kiếm</Text>
            </TouchableOpacity>
          </View>
        
      </View>
      </View>
  )
}

const styles = StyleSheet.create({
  ItemSreach: {
        top: 60,
        left: 18,
        right: 18,
        width: '91%',
        height: '60%',
        backgroundColor: 'white',
        position: 'absolute',
        zIndex: 9,
        borderWidth: 1,
        borderColor: '#DCDCDC',
        borderRadius: 25,
        justifyContent: 'space-between',
        alignItems: 'center'
  },

  buttonSreach: {
    width: '100%',
    backgroundColor: '#3333CC', 
    height: '11%',
    borderRadius: 5, 
    padding: 7,
    marginTop: 20
  },
  
  InputText: {
    borderColor: '#C0C0C0',
    borderBottomWidth: 1,
    width: '90%'
  },

  placeholder: {
    position: 'absolute',
    top: 20,
    left: 10,
    fontSize: 14,
    color: '#aaa',
    borderColor: '#C0C0C0',
    borderBottomWidth: 1,
    width: '100%',
  },

  container: {
    margin: 10,
  },
  title: {
    fontSize: 18,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 10,
    borderColor: '#808080',
    borderWidth: 1,
    borderRadius: 5,
    paddingHorizontal: 10,
  },
  icon: {
    marginRight: 10,
  },
  picker: {
    flex: 1,
    height: 50,
  },



})