#index=5
#print("{0}*{1}={2}",{5,index,5*index})


index=1
for index in range (1,11):
    print("{0}*{1}={2}".format(index,5,index*5))
    print(index)

for i in range (1,11,3):
    print(i)

def print_your_progress_thrice():
    print("abhinav")


Dict = {'Name': 'abhinav','age': '28', 'sex': 'male'}
print(Dict)
Dict = {v: k for k, v in Dict.items()}
print(Dict)
Dict(Name)


my_dict = {'name':["Raju","abhinav","akhil","vinay","x","y","z"],'Age':["28","25","30","64","42","45","25"]}
print(my_dict)
print(my_dict["name"])
quip=zip(my_dict["name"],my_dict["Age"])
print(quip)
for i in quip:
    print(i)



my_page = {'name':['x','y','z'],'Age':['1','2','3','4','5']}
print(my_page)
word=zip(my_page['name'],my_page['Age'])
print(word)
for i in word:
    print(i)

quip={'name':'abhinav','age':'28','gender':'male','location':'hyderabad'}
print('key',':','value')
for key in quip :
    print (key ,":", quip[key])
print(quip.keys())
print(quip.values())
print(quip.items())
print(type(quip.keys()))
print(type(quip.values()))
print(len(quip.items()))

#Adding items and removing to dictionary

excel = {'name':'arun','age':'28','gender':'male','location':'karimnagar'}
print(excel)
excel['weight'] = 68
print(excel)
excel['height'] = 5.4
print(excel)
excel['speed'] = 6.5
print(excel)
excel.update({"PG": "mukunda"})
print(excel)
excel.update({"mobile": "iphone", "bike":"activa", "number": 1234})
print(excel)
excel["gym"] = 'anjaiah_nagar'
print(excel)
excel['native'] = 'peddapalli'
print(excel)
excel.update([('friend','prasad'),('enemy','abhinav')])
print(excel)
excel.setdefault('name','akhil')
excel.setdefault('zip')
print(excel)
for key in excel :
    print(key, ":", excel[key])

deleted_item = excel.popitem()
print(deleted_item)
deleted_item = excel.pop('height')
print(deleted_item)
print(excel)
del excel['location']
print(excel)

print(excel.keys())
key_name = 'age'
if key_name in excel.keys():
    print('arun age is' , excel[key_name])
else :
    print ('key not found')


topics1 = {'name' : 'abhinav', "gender" : "male"}
topics2 = {'age' : "28" , "colour" : "fare"}
topics2.update(topics1)
print(topics2)


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(key,":", value)

Dict = {'Name': 'abhinav','age': '28', 'sex': 'male'}
print(Dict)
Dict = {v: k for k, v in Dict.items()}
print(Dict)
Dict(Name)


my_page = {'name':['x','y','z'],'Age':['1','2','3','4','5']}
print(my_page)
word=zip(my_page['name'],my_page['Age'])
print(word)
for i in word:
    print(i)

my_page = {'name':['x','y','z'],'Age':['1','2','3','4','5']}
print(my_page)
word=zip(my_page['name'],my_page['Age'])
print(word)
for i in word:
    print(i)

my_page = {'name':['x','y','z'],'Age':['1','2','3','4','5']}
print(my_page)
word=zip(my_page['name'],my_page['Age'])
print(word)
for i in word:
    print(i)


finalexcel= {**topics, **topics2}
print(finalexcel)


























