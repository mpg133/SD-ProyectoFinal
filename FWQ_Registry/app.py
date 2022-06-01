#!/usr/bin/python3

from flask import Flask, jsonify
from dotenv import dotenv_values

from controller import *

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def reg():
    #register(name, password)
    data={
            'ok' : True,
            'id' : '1',
            'name' : 'asd',
            'msg' : 'de puta mare lokoooh'
            }

    return jsonify(data)


if __name__ == '__main__':
    config = dotenv_values(".env")
    app.run(host=config['REGISTRY_API_IP'], port=int(config['REGISTRY_API_PORT']))
