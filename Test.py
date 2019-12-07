import json
import codecs

#Create file
#new_file = open(r'C:\Users\Konstantinos\Desktop\KonstantinaTsimpita_9b0FdyXvUA\TestDecoded.txt', 'x')
#Set file
file = codecs.open(r'C:\Users\Konstantinos\Desktop\KonstantinaTsimpita_9b0FdyXvUA\Test.json', 'r','utf-8')
u = file.read()


#Get file as array
with u as myfile:
    lines = myfile.readlines()

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
#Format "name": "Name" to Name
for i in range(0,len(people)):
    people[i] = people[i].replace("name", "")
    people[i] = people[i].replace(":","")
    people[i] = people[i].replace('"','')
    #print(people[i])

for i in range(0,len(lines)):
    if 'content' in lines[i]:
        #I want the format r'String'
        test = "r'"+lines[i][:-1]+"'"
        print(test)
        decoded = json.loads(test).encode('latin1').decode('utf-8')
        print(decoded)
        break

#obj=json.loads(data)
#decoded = json.loads(obj).encode('latin1').decode('utf8')
file.write(decoded)
#file.close()
#myfile.close()