import React, { useEffect, useState } from 'react'
import { StyleSheet, Text, View, Image, TouchableOpacity, FlatList } from 'react-native'
import Apis, { authApi, endpoints } from '../../config/Apis'
import { SelectList } from 'react-native-dropdown-select-list'
import { ActivityIndicator, Button } from 'react-native-paper'
import AsyncStorage from '@react-native-async-storage/async-storage'



export default ProfileView = () => {
  const data = [
    { id: 1, image: 'https://img.icons8.com/color/70/000000/cottage.png', title: 'Order' },
    {
      id: 2,
      image: 'https://img.icons8.com/color/70/000000/administrator-male.png',
      title: 'Like',
    },
    { id: 3, image: 'https://img.icons8.com/color/70/000000/filled-like.png', title: 'Comment' },
    { id: 4, image: 'https://img.icons8.com/color/70/000000/facebook-like.png', title: 'Download' },
    { id: 5, image: 'https://img.icons8.com/color/70/000000/shutdown.png', title: 'Edit' },
  ]


  const [options, setOptions] = useState(data)
  const [trips, setTrip] = useState(null)
  const [chairs, setChair] = useState(null)


  useEffect(() => {
    const loadTripDetail = async () => {
      let trip = await Apis.get(endpoints['tripDetail'](1));
      setTrip(trip.data)

    }

    const loadChair = async () => {
      let chair = await Apis.get(endpoints['chair'](1))
      setChair(chair.data)
      console.info(chairs.data)
    }
    loadTripDetail();
    loadChair();
  }, []);
  console.info(trips)
  const ticket_onl = async (chair) => {
    let invoice = await Apis.post(endpoints['invoice'], {
      "amout": 0
    });
    console.info(invoice.data)
    const access_token = await AsyncStorage.getItem('access-token');
    let ticket = await authApi(access_token).post(endpoints['bookTicket_onl'](1), {
      "invoice": invoice.id,
      "chair": chair
    });
    console.info(ticket.data)
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <View style={styles.headerContent}>
          <Image
            style={styles.avatar}
            source={{ uri: 'https://bootdey.com/img/Content/avatar/avatar3.png' }}
          />
          <Text style={styles.name}>Jane Doe</Text>
        </View>
      </View>
      {trips === null ? <ActivityIndicator /> : <>
        <Text key={trips.id}>{trips.dateGo}</Text>
        {chairs === null ? <ActivityIndicator /> : <>
          <View>
            {chairs.map(c => <TouchableOpacity key={c.id} onPress={() => ticket_onl(c.id)}>
              <View style={styles.box}>
                <Image style={styles.icon} source={{ uri: 'https://img.icons8.com/color/70/000000/cottage.png' }} />
                <Text style={styles.title} >{c.name}</Text>
                <Image
                  style={styles.btn}
                  source={{ uri: 'https://img.icons8.com/customer/office/40' }}
                />
              </View>
            </TouchableOpacity>
            )}
          </View>
        </>}
      </>}
    </View>
  )
}

const styles = StyleSheet.create({
  header: {
    backgroundColor: '#EE82EE',
  },
  headerContent: {
    padding: 30,
    alignItems: 'center',
  },
  avatar: {
    width: 130,
    height: 130,
    borderRadius: 63,
    borderWidth: 4,
    borderColor: '#FF6347',
    marginBottom: 10,
  },
  icon: {
    width: 40,
    height: 40,
  },
  title: {
    fontSize: 18,
    color: '#EE82EE',
    marginLeft: 4,
  },
  btn: {
    marginLeft: 'auto',
    width: 40,
    height: 40,
  },
  body: {
    backgroundColor: '#E6E6FA',
  },
  box: {
    padding: 5,
    marginBottom: 2,
    backgroundColor: '#FFFFFF',
    flexDirection: 'row',
    alignItems: 'center',
  },
  username: {
    color: '#20B2AA',
    fontSize: 22,
    alignSelf: 'center',
    marginLeft: 10,
  },
})
