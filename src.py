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

text = "It's pretty good.I heard you're loving skydiving."
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

#Converting labels to str itself
reverse_d = {v: k for k, v in d.items()}
texta = ' '.join([reverse_d[i] for i in new_x])

print(texta)
