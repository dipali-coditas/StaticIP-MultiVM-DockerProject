# from flask import Flask, jsonify
# from flask_cors import CORS
# from pymongo import MongoClient

# app = Flask(__name__)
# CORS(app)

# # for manual container deployement tyr this 
# # client = MongoClient("mongodb://localhost:27017")

# client = MongoClient("mongodb://root:root@192.0.0.5:27017")


# db = client["shopping"]
# collection = db["products"]

# @app.route('/get_data', methods=['GET'])
# def get_data():
#     # Fetch data from MongoDB
#     cursor = collection.find({})
#     data = list(cursor)

#     # Convert ObjectId to str for JSON serialization
#     for item in data:
#         item['_id'] = str(item['_id'])
#     print(data)
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=8000)

from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    host="34.93.33.112",
    port="5432"
)

# Create a cursor
cursor = conn.cursor()

@app.route('/get_data', methods=['GET'])
def get_data():
    conn.open()
    # Fetch data from PostgreSQL
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    # Convert data to a list of dictionaries
    keys = ["pid", "name", "price", "description", "image_url"]
    data_list = [dict(zip(keys, row)) for row in data]
    conn.close()

    return jsonify(data_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)

