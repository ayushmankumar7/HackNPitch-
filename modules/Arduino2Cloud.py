import serial
import firebase_admin
import time
import datetime
import ast
from firebase_admin import firestore
from firebase_admin import credentials

if (not len(firebase_admin._apps)):
    
    cred = credentials.Certificate("measure-distance-ac87a-firebase-adminsdk-7fb2c-36a9368d56.json")

    default_app = firebase_admin.initialize_app(cred,
        {'projectID': 'measure-distance-ac87a'
        })

db = firestore.client()

ref = db.collection(u'data')


arduino = serial.Serial('COM3', 9600, timeout=.1)
count = False
count2 = False

for i in range(10):
    print(i)
    
    data = arduino.readline()[:-2].decode("utf-8").split()
    print(data[1])
    
    ref.document(str(i)).set({u'distance':data[1]})