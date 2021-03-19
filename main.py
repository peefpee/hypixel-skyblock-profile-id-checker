import requests
import json
print ('welcome to the profile id checker by bear bear team *for hypixel skyblock')
name = input('what is your ign?')
profile = input('what is your profile name?')

response = requests.get('https://sky.shiiyu.moe/api/v2/coins/'+ name + '/' + profile)
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



dictionary =  (response.json())
  

json_object = json.dumps(dictionary, indent = 4) 
  

with open("api.json", "w") as outfile: 
    outfile.write(json_object) 


    f = open('api.json',) 
  

data = json.load(f) 
  

for i in data['profile_id']: 
    print(i) 
  

f = open("output.txt", "a")
f.write(i)
f.close()
