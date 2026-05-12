from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Donea Fernando-Emanuel: 226/2024"

'''
This method expects a json content.
Use header: 'Content-Type: application/json'
'''
@app.route('/post', methods=['POST'])
def post_method():
    print("Got from user: ", request.get_json())
    print(request.get_json()['value']*2)
    return jsonify({'got_it': 'yes'})



@app.route('/id', methods=['POST'])
def itemId():
    print("Got from user: ", request.get_json())
    print(request.get_json()['value']*2)
    raspuns=str(request.get_json()['value'])

    return jsonify({'item_id': raspuns})



import socket
@app.route('/idContainer')
def idContainer():
    host=socket.gethostname()
    ip=socket.gethostbyname(host)
    return jsonify({'ip': ip})






import math
@app.route('/submaskmin',methods=['POST'])
def subnetMinimal():
    ip=request.get_json()['ip']
    noduri=request.get_json()['noduri']

    # nr de biti pentru noduri
    biti=math.ceil(math.log2(noduri))


    mask=(0xFFFFFFFF<<biti)&0xFFFFFFFF

    #convertim masca din nr intreg in strnig
    a=mask//(256**3)
    b=(mask//(256**2))%256
    c=(mask//256)%256
    d=mask%256

    raspuns=f"{a}.{b}.{c}.{d}"

    return raspuns

    





@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)


