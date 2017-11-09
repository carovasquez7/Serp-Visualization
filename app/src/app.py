from flask import Flask, jsonify, abort, make_response, request, json, Response, render_template
#from model import db

#from model import CreateDB
#from model import app as application
#import simplejson as json
#from sqlalchemy.exc import IntegrityError
#from sqlalchemy.sql.expression import func, select

from flask_cors import CORS

from core import *
from FeatureExtraction import *
from time import time
from datetime import datetime
import random
import os
import json

NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'
lista = []


app = Flask(__name__)
CORS(app)


#template vista htlm
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/getMyJson')
def getMyJson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "jsonCircles.json")
    data = json.load(open(json_url))
    response = Response(response=data, status=200, mimetype="application/json")
    return(response)


#Cargar (subir) archivo JSON, que corresponde a la lista de SERPs de un motor de busqueda.
@app.route('/api/v1.0/uploadjson', methods=['GET'])
def loadJsonInToDic():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "internalJsonGoogle.json")
    data = json.load(open(json_url))

    lista.append(jsonToDictionary(json_url))
    return jsonify({'Sucess': True})


#Mostrar/Leer/cargar el archivo JSON con la lista de SERPs.
@app.route('/api/v1.0/loadjson', methods=['GET'])
def getSerps():
    return jsonify({'dic': lista[0]})


#Muestra Los atributos que posee todos los serps
@app.route('/api/v1.0/getAttributes', methods=['GET'])
def getAttributes():
    return jsonify({'List of Attributes': obtainAttributesFromJson(lista[0])})


#Obtiene los valores de un atributo en particupar, ejemplo "getValues?name=description"
@app.route('/api/v1.0/getValues', methods=['GET'])
def getValueinDicToAttribute():
    if 'name' in request.args:
        name = request.args.get('name')
        return jsonify({'List Of Value':getValueinDic(lista[0], name)}) 
    else:
        abort(400)


#"Plugin" Cuenta las palabras del atributo DESCRIPTION
#Para ejecutar se debe entregar el nombre del Nuevo atributo (numberWord) "wordCountDescrip?newname=numberword&query=snipet"
@app.route('/api/v1.0/wordCountDescrip', methods=['GET'])
def wordCountDescription():

    newnameattribute = request.args.get('newname')
    queryname = request.args.get('query')


    return jsonify({'Number of description': countWordDescription(lista[0], newnameattribute, queryname)})


#Exporta el diccionario en un achivo JSON
@app.route('/api/v1.0/exportJson', methods=['GET'])
def exportJson():
    namefile = request.args.get('filename')
    DictionaryToJson(lista[0], namefile)
    return jsonify({'Sucess': True})







#APARTE


items = [
    {
        'id': 1,
        'name': 'laptop',
        'value': 1000
    },
    {
        'id': 2,
        'name': 'chair',
        'value': 300,
    },
    {
        'id': 3,
        'name': 'book',
        'value': 20,
    },
]


def _get_item(id):
    return [item for item in items if item['id'] == id]


def is_record_exists(name):
    return [item for item in items if item["name"] == name]



@app.route('/api/v1.0/items', methods=['GET', 'POST'])
def get_items():
    if request.method == 'GET':
        return jsonify({'items': items})
    else:
        if not request.json or 'name' not in request.json or 'value' not in request.json:
            abort(400)
        item_id = items[-1].get("id") + 1
        name = request.json.get('name')
        if is_record_exists(name):
            abort(400)
        value = request.json.get('value')
        if type(value) is not int:
            abort(400)
        item = {"id": item_id, "name": name, "value": value}
        items.append(item)
        return jsonify({'item': item}), 201


@app.route('/api/v1.0/items/<int:id>', methods=['GET'])
def get_item(id):
    item = _get_item(id)
    if not item:
        abort(404)
    return jsonify({'items': item})


@app.route('/api/v1.0/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json or 'value' not in request.json:
        abort(400)
    item_id = items[-1].get("id") + 1
    name = request.json.get('name')
    if is_record_exists(name):
        abort(400)
    value = request.json.get('value')
    if type(value) is not int:
        abort(400)
    item = {"id": item_id, "name": name, "value": value}
    items.append(item)
    return jsonify({'item': item}), 201


@app.route('/api/v1.0/testingpost', methods=['POST'])
def testing_post():
    if 'name' in request.args and 'edad' in request.args:
        name = request.args.get("name")
        edad = request.args.get("edad")
        return jsonify({'name': name, 'edad': edad})
    else:
        abort(400)


@app.route('/api/v1.0/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = _get_item(id)
    if len(item) == 0:
        abort(404)
    if not request.json:
        abort(400)
    name = request.json.get('name', item[0]['name'])
    value = request.json.get('value', item[0]['value'])
    if type(value) is not int:
        abort(400)
    item[0]['name'] = name
    item[0]['value'] = value
    return jsonify({'item': item[0]}), 200


@app.route('/api/v1.0/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = _get_item(id)
    if len(item) == 0:
        abort(404)
    items.remove(item[0])
    return jsonify({}), 204


@app.route('/api/v1.0')
def api_root():
    return 'Welcome'


@app.route('/api/v1.0/status')
def app_status():
    return json.dumps({
        'server_info':
        application.config['SQLALCHEMY_DATABASE_URI']
    })


@app.route('/api/v1.0/createtbl')
def create_tables():
    try:
        db.create_all()
        return json.dumps({'status': True})
    except IntegrityError:
        return json.dumps({'status': False})


@app.route('/api/v1.0/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'


@app.route('/api/v1.0/hellostatus', methods=['GET'])
def api_hello_status():
    data = {'hello': 'world', 'number': 3}
    js = json.dumps(data)

    resp = jsonify(data)
    resp.status_code = 200
    resp.headers['Link'] = 'http://luisrei.com'
    return resp


@app.route('/api/v1.0/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


@app.route('/api/v1.0/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"


@app.route('/api/v1.0/users/<userid>', methods=['GET'])
def api_users(userid):
    users = {'1': 'john', '2': 'steve', '3': 'bill'}
    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True, threaded=True)
