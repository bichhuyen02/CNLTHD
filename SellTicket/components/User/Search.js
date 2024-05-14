 
import React from 'react';
import { View, Text, StyleSheet, TextInput, ScrollView } from 'react-native';
import { AntDesign } from '@expo/vector-icons';



export default Search = ({ navigation }) => {
    return (
        <View style={styles.searchContainer} onPress={() => navigation.navigate("Search")}>
            <View style={styles.inputWrapper}>
                    <AntDesign name="search1" size={24} color="black" style={styles.searchIcon} />
                    <TextInput style={styles.inputText} placeholder="Chọn thành phố, khu vực, điểm lên xe ..." />
            </View>

            <View style={{ marginTop: '5%' }}>
                <View style={styles.ItemSearch}>
                    <View>
                        <View style={styles.Text}>
                            <Text style={{ fontSize: 16, fontWeight: 600, marginTop:'5%', marginLeft:'2%' }}> Thành Phố Hồ Chí Minh </Text>
                            <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969',marginLeft:'2%' }}> Tất cả các địa điểm lên xe của thành phố Hồ Chí Minh</Text>
                        </View>

                        <View style={styles.Text}>
                            <Text style={{ fontSize: 16, fontWeight: 600, marginTop:'5%', marginLeft:'2%' }}> Thành Phố Đồng Nai </Text>
                            <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969',marginLeft:'2%' }}> Tất cả các địa điểm lên xe của thành phố Đồng Nai</Text>
                        </View>

                        <View style={styles.Text}>
                            <Text style={{ fontSize: 16, fontWeight: 600, marginTop:'5%', marginLeft:'2%' }}> Thành Phố Đồng Nai </Text>
                            <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969',marginLeft:'2%' }}> Tất cả các địa điểm lên xe của thành phố Đồng Nai</Text>
                        </View>

                        <View style={styles.Text}>
                            <Text style={{ fontSize: 16, fontWeight: 600, marginTop:'5%', marginLeft:'2%' }}> Thành Phố Đồng Nai </Text>
                            <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969',marginLeft:'2%' }}> Tất cả các địa điểm lên xe của thành phố Đồng Nai</Text>
                        </View>

                        <View style={styles.Text}>
                            <Text style={{ fontSize: 16, fontWeight: 600, marginTop:'5%', marginLeft:'2%' }}> Thành Phố Đồng Nai </Text>
                            <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969',marginLeft:'2%' }}> Tất cả các địa điểm lên xe của thành phố Đồng Nai</Text>
                        </View>

                       
                            <Text style={{ fontSize: 16, fontWeight: 600, marginTop:'5%', marginLeft:'2%' }}> Thành Phố Đồng Nai </Text>
                            <Text style={{ marginBottom: 8, marginTop: 5, color: '#696969',marginLeft:'2%' }}> Tất cả các địa điểm lên xe của thành phố Đồng Nai</Text>
                     

                    
                    </View>
                </View>
            </View>
         </View>

       


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
