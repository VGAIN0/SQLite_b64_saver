import os
imports = []
with open('listfile.txt', 'r') as filehandle:
    for line in filehandle:
       
        currentPlace = line[:-1]

     
        imports.append(currentPlace)
        
print(imports)
