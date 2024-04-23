import React, { useEffect, useState } from 'react'
import { StyleSheet, Text, View, Image, TouchableOpacity, FlatList } from 'react-native'
import Apis, { endpoints } from '../../config/Apis'
import { SelectList } from 'react-native-dropdown-select-list'

export default ProfileView = (props) => {
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
  
  const [selected, setSelected] = useState("");
  const [options, setOptions] = useState(data)
  const [bStation, setBStation] = useState(null)
  const [buses, setBuses] = useState(null);
  const [trip, setTrip] = useState(null)

  useEffect(()=>{
    const loadBStation = async()=>{
      let bStation = await Apis.get(endpoints['bStation'])
      console.info(bStation.data);
      setBStation(bStation.data)
    };

    const loadBuses = async()=>{
      let buses = await Apis.get(endpoints['buses'], 
                       {params:{destination: bs_id, departure: bs_id}});
      console.info(buses.data)
      setBuses(buses.data);
    };

    const loadtrip = async()=>{
      let trips = await Apis.get(endpoints['trip'], 
                              {params: { car: car_id, buses: bus_id }});
            console.info(trips.data)
            setTrip(trips.data);
    };

    loadBStation();
    loadBuses();
    loadtrip();
  }, []);

  console.info(selected);
  return (
    <View {...props}style={styles.container}>
      <View>
      <SelectList 
        setSelected={(val) => setSelected(val)} 
        data={bStation.map(b=>[{key:b.id, value: b.name}])}
        save="key"
    />
      </View>
      <View style={styles.header}>
        <View style={styles.headerContent}>
          <Image
            style={styles.avatar}
            source={{ uri: 'https://bootdey.com/img/Content/avatar/avatar3.png' }}
          />
          <Text style={styles.name}>Jane Doe</Text>
        </View>
      </View>

      <View style={styles.body}>
        <FlatList
          style={styles.container}
          enableEmptySections={true}
          data={options}
          keyExtractor={item => item.id}
          renderItem={({ item }) => {
            return (
              <TouchableOpacity>
                <View style={styles.box}>
                  <Image style={styles.icon} source={{ uri: item.image }} />
                  <Text style={styles.title}>{item.title}</Text>
                  <Image
                    style={styles.btn}
                    source={{ uri: 'https://img.icons8.com/customer/office/40' }}
                  />
                </View>
              </TouchableOpacity>
            )
          }}
        />
      </View>
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
    alignItems:'center',
  },
  username: {
    color: '#20B2AA',
    fontSize: 22,
    alignSelf: 'center',
    marginLeft: 10,
  },
})
