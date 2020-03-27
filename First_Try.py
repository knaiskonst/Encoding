import json
import os
import codecs
#Set file
input_path = input("Drag badly encoded file here ")
input_file = codecs.open(input_path,'r','utf-8')

#Create file
output_name = input("Type the name and format of the file. e.g. example.json: ")
print("The decoded file is saved at the directory of the bad file")

directory = os.path.dirname(input_path) #Have the path to file to create the new file
new_path = os.path.join(directory, output_name)
new_output = codecs.open(new_path,'w','utf-8')

#Get file as array
lines = input_file.readlines()

#Print everything
#for i in range(0,len(lines)):
#    print(lines[i])

#Find people names
ppl_num = 0
people = []
for i in range(0,len(lines)):
    if 'name' in lines[i]:
        people.append(1) #make space
        people[ppl_num] = lines[i]
        ppl_num += 1
    if 'messages' in lines[i]:
        break
#Format "name": "Name" to
#print("Participants: ")
for i in range(0,len(people)):
    people[i] = people[i].replace("name", "")
    people[i] = people[i].replace(":","")
    people[i] = people[i].replace('"','')
    #print(people[i])
print("Decoding: ")
for i in range(0,len(lines)):
    to_write = lines[i]
    if 'content' in lines[i]:
        #I want the format r'String'
        test = '"'+lines[i][18:-3]+'"'
        #print(test)
        decoded = json.loads(test).encode('latin1').decode('utf-8')
        #print(decoded)
        to_write = '      "content": "'+decoded+'",\n'
    new_output.write(to_write)

#obj=json.loads(data)
#decoded = json.loads(obj).encode('latin1').decode('utf8')
input_file.close()
new_output.close()