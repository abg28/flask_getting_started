from flask import Flask, jsonify, request
import math

app = Flask(__name__)


@app.route("/name", methods=["GET"])
def getName():
    """
    Returns the string "Hello, world" to the caller
    """
    name = {
        "name": "Alex Guevara"
    }
    return jsonify(name)


@app.route("/hello/<name>", methods=["GET"])
def getData(name):
    """
    Returns the data dictionary below to the caller as JSON
    """
    data = {
        "message": "Hello there, %s" % name
    }
    return jsonify(data)


@app.route("/distance", methods=["POST"])
def setDistance():
    """
    Returns the data dictionary below to the caller as JSON
    """
    points = {
        "a": [2, 4],
        "b": [5, 6]
    }
    distance = math.sqrt(math.pow(points["a"][2]-points["b"][2], 2) +
                         math.pow(points["a"][1]-points["b"][1], 2))
    data = {
        "distance": distance,
        "a": points["a"],
        "b": points["b"]
    }
    return jsonify(data)
