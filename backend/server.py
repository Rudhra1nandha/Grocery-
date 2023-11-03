from flask import Flask, request, jsonify
import product_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods = ['GET'])
def get_Products():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Orginal', '*')
    return response

if __name__ == "__main__":
    print("starting the server for our application")
    app.run(port=5002)

