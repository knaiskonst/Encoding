import sys
import os
user_input = input("Drag file here ")
directory = os.path.dirname(user_input)
new_file_path = os.path.join(directory, "decoded.txt")
print(new_file_path)

import time
time.sleep(5)