# from flask import Flask, jsonify
# from flask_cors import CORS
# from pymongo import MongoClient

# app = Flask(__name__)
# CORS(app)

# client = MongoClient("mongodb://localhost:27017")


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

# ---------------------------with sample data----------------------------------------------
# from flask import Flask, jsonify, request, render_template
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)
# data = [
#     {"pid": 101, "name": 'Smart TV', "price": 25000, "desc": "Best TV in the world...!", "img": "images/tv.jpg"},
#     {"pid": 102, "name": 'Smart Phone', "price": 15000, "desc": "Best Phone in the world...!", "img": "images/phone.jpg"},
#     {"pid": 103, "name": 'Smart Watch', "price": 5000, "desc": "Best Watch in the world...!", "img": "images/smartwatch.jpg"},
#     {"pid": 104, "name": 'Laptop', "price": 50000, "desc": "Best Laptop in the world...!", "img": "images/laptop.jpg"}
# ]
        
# @app.route('/get_data', methods=['POST', 'GET'])
# def get_data():
#     response = jsonify(data)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# if __name__ == "__main__":
#     app.run(host="0.0.0.0",debug=True, port=8000)
