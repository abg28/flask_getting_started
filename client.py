import requests

# Tests POST /distance endpoint
r = requests.post("http://vcm-7291.vm.duke.edu:5000/distance",
                  json={"a": [2, 4],
                        "b": [5, 6]})
print(r.json())

# Tests GET /name endpoint
r = requests.get("http://vcm-7291.vm.duke.edu:5000/name")
print(r.json())

# Tests GET /hello/<name> endpoint
r = requests.get("http://vcm-7291.vm.duke.edu:5000/hello/Alex")
print(r.json())
