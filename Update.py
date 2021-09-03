import os
print("fill the list ")
print("put 0 to stop ")
places = []
t = input("")
while t != 0 :
  if not t:
    break;  
  else :
    places.append(t)
  t = input("")
    
print("Done")

with open('listfile.txt', 'w') as filehandle:
    for listitem in places:
        filehandle.write('%s\n' % listitem)
