from flask import Flask, jsonify, request
import math

app = Flask(__name__)


@app.route("/name", methods=["GET"])
def getName():
    """
    Returns my name to the caller as JSON
    """
    name = {
        "name": "Alex Guevara"
    }
    return jsonify(name)


@app.route("/hello/<name>", methods=["GET"])
def getData(name):
    """
    Returns the name parameter to the caller as JSON
    """
    data = {
        "message": "Hello there, %s" % name
    }
    return jsonify(data)


@app.route("/distance", methods=["POST"])
def setDistance():
    """
    Posts the data dictionary below to the server as JSON
    """
    points = request.get_json()
    distance = math.sqrt(math.pow(points["a"][1]-points["b"][1], 2) +
                         math.pow(points["a"][0]-points["b"][0], 2))
    data = {
        "distance": distance,
        "a": points["a"],
        "b": points["b"]
    }
    return jsonify(data)
