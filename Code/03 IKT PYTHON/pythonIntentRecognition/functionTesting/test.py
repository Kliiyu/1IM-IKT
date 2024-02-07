import pickle
import json
from PIL import Image

# usefull links = https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled
# 

addresses = []

def bytes_to_json(b: bytes) -> json:
    decoded = b.decode('latin-1')
    return json.dumps(decoded)

def json_to_bytes(j: json) -> bytes:
    json_dict = json.loads(j)
    decoded_string = str(json_dict)
    return decoded_string.encode('latin-1')

def open_img():
    with Image.open("Anime Girl Base.jpg") as im:
        im.show()


pickled_function = pickle.dumps(open_img)

print("run (r) or write (w)")
inp = input("# ").lower()
match inp:
    case 'r':
        with open('functionTesting/test.json', 'r') as file:
            data = json.load(file)

        bstring = json_to_bytes(data["intents"]["function"])
        unpickled_function = pickle.loads(bstring)
        unpickled_function()
    case 'w':
        with open('functionTesting/test.json', 'r') as file:
            data = json.load(file)

        data["intents"]["function"] = bytes_to_json(pickled_function)

        with open('functionTesting/test.json', 'w') as file:
            json.dump(data, file, indent=4)