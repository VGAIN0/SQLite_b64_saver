import os
print("add to list the list ")
print("press empty enter to stop ")
app = []
t = input("")
while t != 0 :
  if not t:
    break;  
  else :
    app.append(t)
  t = input("")
    
print("Done")
with open('listfile.txt', 'a') as filehandle:
    for listitem in app:
        filehandle.write('%s\n' % listitem)
