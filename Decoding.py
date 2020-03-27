import re
from functools import partial
import json
import os

input_file = input("Drag file here ")   #User drags file to cmd
output_name = input("Type the name and format of the file. e.g. example.json")
directory = os.path.dirname(input_file) #Have the path to file to create the new file
new_file_path = os.path.join(directory, output_name)
print("Decoding...")

fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub,
    lambda m: bytes.fromhex(m.group(1).decode()))

with open(input_file, 'rb') as binary_data:
    repaired = fix_mojibake_escapes(binary_data.read())
data = json.loads(repaired.decode('utf8'))

with open(new_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)

