#reading the file 
f=open('numbers.txt','r')
print(f.read())

#counting the frequency of values
f=open('numbers.txt','r')
num1=f.read()
num2=num1.replace('\n',',').split(',')
num3=[int(i) for i in num2]
num3.sort
freq={}
for number in num3:
    if number in freq:
        freq[number]+=1
    else:
         freq[number]=1
freq1=dict(sorted(freq.items()))
print(freq1)

#storing as a json file
import json
dictionary={
    0: 9,
    1: 14,
    2: 19,
    3: 20,
    4: 22,
    5: 10,
    6: 26,
    7: 17,
    8: 13,
    9: 24,
    10: 14
    }
with open ("your_json_file","w") as outfile:
    json.dump(dictionary, outfile)