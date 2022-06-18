import json
import requests
from flask import Flask, jsonify,request
from dotenv import dotenv_values

config = dotenv_values(".env")

API_URL = config['API_URL']

def registrarVisitanteAPI(name,password):
    data = {'name' : name, 'password' : password}
    response = requests.post(API_URL+"/user",data)
    ret=json.loads(response.text)
    return ret["ok"], ret["msg"]
def editarVisitanteAPI(name,password,newName,newPassword):
    data = {'name' : name, 'password' : password,'newName':newName , 'newPassword' : newPassword}
    response = requests.put(API_URL+"/user",data)
    ret=json.loads(response.text)
    return ret["ok"], ret["msg"]
