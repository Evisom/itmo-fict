#[+] Создание транзакции и запись в БД
#[+] Просмотривать все транзакции
#[ ] Просматривать транзакции по дате и категории
#[ ] Просматривать транзакции отсортированные
#[+] Удалять транзакции из БД

from db import *
import os.path
from flask import Flask, Response, jsonify, request
app = Flask(__name__)

def getFile(filename):
    try:
        src = os.path.join('./www', filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route("/")
def responseRoot():
    return Response(getFile('index.html'))

@app.route('/<path:path>')
def serveStatic(path):
    ext = path.split('.')[-1]
    print(ext)
    if ext == 'html':
        type='text/html'
    elif ext == 'css':
        type='text/css'
    elif ext == 'js':
        type='text/javascript'
    else:
        type=''
    content = getFile(path)
    return Response(content, mimetype=type)

@app.route('/getAllTransactions', methods = ['GET'])
def getAllTransations():
    r = db_readAll()
    # print(r)
    if r:
        return jsonify(r)
    else:
        return jsonify({'status':'server_error'})

@app.route('/getCategories', methods = ['GET'])
def getCategories():
    r = db_getCategories()
    if r:
        return jsonify(r)
    else:
        return jsonify({'status':'bad_request'})

@app.route('/getByCategory' , methods = ['GET'])
def getByCategory():
    args = request.args
    if 'category' in args.keys():
        r = db_getByCategory(args['category'])
        return jsonify(r)
    else:
        return jsonify({'status':'bad_request'})        
    

@app.route('/getByDate' , methods = ['GET'])
def getByDate():
    args = request.args
    if 'startDate' in args.keys() and 'endDate' in args.keys():
        r = db_getByDate(args['startDate'], args['endDate'])
        print(r)
        return jsonify(r)
    else:
        return jsonify({'status':'bad_request'})       


@app.route('/createTransaction', methods = ['POST'])
def createTransaction():
    data = request.json
    if db_write(data):
        return jsonify({'status':'ok'})
    else:
        return jsonify({'status':'bad_request'})

@app.route('/deleteTransaction', methods = ['POST'])
def deleteTransaction():
    print(request)
    data = request.json
    if db_delete(data):
        return jsonify({'status':'ok'})
    else:
        return jsonify({'status':'bad_request'})