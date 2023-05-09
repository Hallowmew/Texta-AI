import random


#Seed starter
startingseed = ""
pickedseed = random.randint(1, 3)
if pickedseed == 1:
 startingseed = "I"
elif pickedseed == 2:
 startingseed = "Yes"
else:
 startingseed = "No"

with open('text.txt', 'r', encoding='utf-8') as file:
  text = file.read()

print(startingseed)
splittedtext = text.split(".")

print(splittedtext)
a = 0
for x in range(10):
  a = a + 1
 
  print(splittedtext)
  
  




texttest = "Hello", "How are you"

mystring = "aawa"

mylist = "so", "ok"

aanw = 1
anew = [s + str(aanw) for s in mylist]

print(anew)

#Str labeller
d = {}

count = 0
for i in splittedtext:
  if i not in d:
     d[i] = count
     count += 0.01

new_x = [d[i] for i in splittedtext]

print(new_x)

#converting tokenizied values to string
reverse_d = {v: k for k, v in d.items()}
texta = ' '.join([reverse_d[i] for i in new_x])

print(texta)

#Tokinozer 
w = [0.5 for w in range(1000)]
an = [0.5 for an in range(10)]

result = [] 
for i in range(min(len(w), len(new_x))):
    result.append(w[i] * new_x[i])

print(result)




