import google.cloud
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

ref = db.collection(u'person')


try:
    docs = ref.get()
    for doc in docs:
        print(u'Doc Data:{}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')
    
ref = db.collection(u'test')
ref.add({u'name': u'test', u'added': u'just now'})