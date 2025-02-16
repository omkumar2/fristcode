week_5.py

# Dictionaries

d={}
d['om kumar']=6203884166
d['jay kumar '] = 8104022050
d['raj kumar'] = 9102024444

print(d) #{'om kumar': 6208894766, 'jay kumar ': 8104022050, 'raj kumar': 9102024444}

malgudi = ['It', 'was', 'Monday', 'morning.', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his','eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant' ,'in', 'the', 'calendar.', 'After', 'the', 'delicious', 'freedom', 'of', 'Saturday', 'And', 'Sunday,', 'it', 'was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline.', 'He', 'shuddered', 'at', 'the', 'very', 'thought', 'of', 'school:' ,'the', 'dismal', 'yellow', 'building;', 'the', 'fire-eyed', 'Vedanayagam,', 'his', 'class', 'teacher,', 'and', 'headmaster', 'with', 'his', 'thin', 'long', 'cane...']

print(malgudi) # ['It', 'was', 'Monday', 'morning.', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his', 'eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar.', 'After', 'the', 'delicious', 'freedom', 'of', 'Saturday', 'And', 'Sunday,', 'it', 'was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline.', 'He', 'shuddered', 'at', 'the', 'very', 'thought', 'of', 'school:', 'the', 'dismal', 'yellow', 'building;', 'the', 'fire-eyed', 'Vedanayagam,', 'his', 'class', 'teacher,', 'and', 'headmaster', 'with', 'his', 'thin', 'long', 'cane...']

print(malgudi[0]) # it

print(d['om kumar'])  # 6208894766

l=[1,2,3,4,5,6,7,8,9,100]

for i in range(len(l)):
  print(i) 
 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
for i in l:
  print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 100

for i in range(len(l)):
  print(l[i])

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 100

print(len(malgudi)) #65

s=set(malgudi)
print(s) #{'delicious', 'very', 'reluctant', 'in', 'Swaminathan', 'of', 'thought', 'work', 'unpleasant', 'specially', 'Monday', 'open', 'thin', 'After', 'freedom', 'mood', 'school:', 'his', 'He', 'the', 'difficult', 'get', 'class', 'It', 'And', 'eyes.', 'at', 'it', 'long', 'cane...', 'was', 'into', 'Saturday', 'shuddered', 'Sunday,', 'discipline.', 'with', 'and', 'yellow', 'headmaster', 'calendar.', 'teacher,', 'Vedanayagam,', 'building;', 'considered', 'dismal', 'morning.', 'fire-eyed', 'to'}

print(malgudi) # ['It', 'was', 'Monday', 'morning.', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his', 'eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar.', 'After', 'the', 'delicious', 'freedom', 'of', 'Saturday', 'And', 'Sunday,', 'it', 'was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline.', 'He', 'shuddered', 'at', 'the', 'very', 'thought', 'of', 'school:', 'the', 'dismal', 'yellow', 'building;', 'the', 'fire-eyed', 'Vedanayagam,', 'his', 'class', 'teacher,', 'and', 'headmaster', 'with', 'his', 'thin', 'long', 'cane...']


print(len(s)) # 49
print(len(malgudi)) # 65
print(malgudi[47]) # school:


for x in malgudi:
  print(x)

# It
# was
# Monday
# morning.
# Swaminathan
# was
# reluctant
# to
# open
# his
# eyes.
# He
# considered
# Monday
# specially
# ...

d={}
for x in s:
  d[x]=0

print(s) #{'mood': 0, 'was': 0, 'Vedanayagam,': 0, 'class': 0, 'And': 0, 'open': 0, 'headmaster': 0, 'his': 0, 'Sunday,': 0, 'into': 0, 'to': 0, 'school:': 0, 'of': 0, 'freedom': 0, 'with': 0, 'discipline.': 0, 'specially': 0, 'delicious': 0, 'and': 0, 'teacher,': 0, 'Swaminathan': 0, 'very': 0, 'get': 0, 'He': 0, 'shuddered': 0, 'morning.': 0, 'the': 0, 'at': 0, 'thought': 0, 'long': 0, 'eyes.': 0, 'considered': 0, 'thin': 0, 'Saturday': 0, 'calendar.': 0, 'unpleasant': 0, 'work': 0, 'yellow': 0, 'in': 0, 'cane...': 0, 'It': 0, 'building;': 0, 'it': 0, 'reluctant': 0, 'dismal': 0, 'Monday': 0, 'After': 0, 'difficult': 0, 'fire-eyed': 0}

print(d) # {'mood': 1, 'was': 3, 'Vedanayagam,': 1, 'class': 1, 'And': 1, 'open': 1, 'headmaster': 1, 'his': 3, 'Sunday,': 1, 'into': 1, 'to': 2, 'school:': 1, 'of': 3, 'freedom': 1, 'with': 1, 'discipline.': 1, 'specially': 1, 'delicious': 1, 'and': 2, 'teacher,': 1, 'Swaminathan': 1, 'very': 1, 'get': 1, 'He': 2, 'shuddered': 1, 'morning.': 1, 'the': 6, 'at': 1, 'thought': 1, 'long': 1, 'eyes.': 1, 'considered': 1, 'thin': 1, 'Saturday': 1, 'calendar.': 1, 'unpleasant': 1, 'work': 1, 'yellow': 1, 'in': 1, 'cane...': 1, 'It': 1, 'building;': 1, 'it': 1, 'reluctant': 1, 'dismal': 1, 'Monday': 3, 'After': 1, 'difficult': 1, 'fire-eyed': 1}

print(d['get']) # 0
for x in malgudi:
  d[x]=d[x]+1

print(d) # {'freedom': 1, 'was': 3, 'get': 1, 'it': 1, 'teacher,': 1, 'After': 1, 'class': 1, 'to': 2, 'reluctant': 1, 'morning.': 1, 'eyes.': 1, 'thought': 1, 'open': 1, 'fire-eyed': 1, 'It': 1, 'considered': 1, 'with': 1, 'unpleasant': 1, 'yellow': 1, 'headmaster': 1, 'thin': 1, 'delicious': 1, 'of': 3, 'into': 1, 'Monday': 3, 'his': 3, 'the': 6, 'Swaminathan': 1, 'specially': 1, 'Saturday': 1, 'mood': 1, 'and': 2, 'very': 1, 'dismal': 1, 'discipline.': 1, 'school:': 1, 'cane...': 1, 'at': 1, 'And': 1, 'shuddered': 1, 'calendar.': 1, 'in': 1, 'He': 2, 'Vedanayagam,': 1, 'building;': 1, 'Sunday,': 1, 'long': 1, 'work': 1, 'difficult': 1}

print(d['his']) # 3
max=0

d={}
answer_word = ''
for x in s:
  d[x]=0

print(d) # {'freedom': 0, 'was': 0, 'get': 0, 'it': 0, 'teacher,': 0, 'After': 0, 'class': 0, 'to': 0, 'reluctant': 0, 'morning.': 0, 'eyes.': 0, 'thought': 0, 'open': 0, 'fire-eyed': 0, 'It': 0, 'considered': 0, 'with': 0, 'unpleasant': 0, 'yellow': 0, 'headmaster': 0, 'thin': 0, 'delicious': 0, 'of': 0, 'into': 0, 'Monday': 0, 'his': 0, 'the': 0, 'Swaminathan': 0, 'specially': 0, 'Saturday': 0, 'mood': 0, 'and': 0, 'very': 0, 'dismal': 0, 'discipline.': 0, 'school:': 0, 'cane...': 0, 'at': 0, 'And': 0, 'shuddered': 0, 'calendar.': 0, 'in': 0, 'He': 0, 'Vedanayagam,': 0, 'building;': 0, 'Sunday,': 0, 'long': 0, 'work': 0, 'difficult': 0}

for x in malgudi:
  d[x]=d[x]+1
  if(d[x]>max):
    max=d[x]
    answer_word=x

print(d) # {'freedom': 1, 'was': 3, 'get': 1, 'it': 1, 'teacher,': 1, 'After': 1, 'class': 1, 'to': 2, 'reluctant': 1, 'morning.': 1, 'eyes.': 1, 'thought': 1, 'open': 1, 'fire-eyed': 1, 'It': 1, 'considered': 1, 'with': 1, 'unpleasant': 1, 'yellow': 1, 'headmaster': 1, 'thin': 1, 'delicious': 1, 'of': 3, 'into': 1, 'Monday': 3, 'his': 3, 'the': 6, 'Swaminathan': 1, 'specially': 1, 'Saturday': 1, 'mood': 1, 'and': 2, 'very': 1, 'dismal': 1, 'discipline.': 1, 'school:': 1, 'cane...': 1, 'at': 1, 'And': 1, 'shuddered': 1, 'calendar.': 1, 'in': 1, 'He': 2, 'Vedanayagam,': 1, 'building;': 1, 'Sunday,': 1, 'long': 1, 'work': 1, 'difficult': 1}
print(max) # 6

print(answer_word) # the

for x in malgudi:
  print(x,end=' ') # It was Monday morning. Swaminathan was reluctant to open his eyes. He considered Monday specially unpleasant in the calendar. After the delicious freedom of Saturday And Sunday, it was difficult to get into the Monday mood of work and discipline. He shuddered at the very thought of school: the dismal yellow building; the fire-eyed Vedanayagam, his class teacher, and headmaster with his thin long cane...

d={}
d['om kuamr'] = [98,99,95]
d['jaynkumar'] = [99,98,97]
d['rahul'] = [97,98,99]

print(d) # {'om kuamr': [98, 99, 95], 'jaynkumar': [99, 98, 97], 'rahul': [97, 98, 99]}
print(d['om kuamr'][0]) #98

# More on Dictionaries

d = {'key' : 'value'}
print(d['key'])  # value

#next
d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
for key in d:
    print(key, d[key])

# 0 0
# 1 1
# 2 4
# 3 9
# 4 16

#next
d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d.keys()) # dict_keys([0, 1, 2, 3, 4])
print(d.values()) # dict_values([0, 1, 4, 9, 16])
print(d.items()) # dict_items([(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)])

#: Sorting using Functions














