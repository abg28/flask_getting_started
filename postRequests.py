import requests

r = requests.post("http://127.0.0.1:5000/distance",
                  json={"a": [2, 4],
                        "b": [5, 6]})
print(r.json())
