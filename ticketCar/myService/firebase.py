from pyrebase import pyrebase

config = {
    "apiKey": "AIzaSyAQWpcDDr76-TT6YsQj7-82PVbD0By7h9s",
    "authDomain": "ticket-20c1a.firebaseapp.com",
    "projectId": "ticket-20c1a",
    "storageBucket": "ticket-20c1a.appspot.com",
    "messagingSenderId": "512425840550",
    "appId": "1:512425840550:web:14db2451415639cc2d8967",
    "measurementI": "G-2P44PS097C",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
auth = firebase.auth()
