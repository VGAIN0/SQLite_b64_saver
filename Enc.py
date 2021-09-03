import base64
imports_from_file = []
imports_enc = []

with open('listfile.txt', 'r') as filehandle:
    for line in filehandle:
       
        currentPlace = line[:-1]

     
        imports_from_file.append(currentPlace)
        
for i in imports_from_file:
    message = i
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    imports_enc.append(base64_message)
    
with open('enc_list.txt', 'r') as filehandle2:
    for line2 in filehandle2:
       
        currentPlace = line[:-1]

     
        imports_enc.append(currentPlace)
        
with open('enc_list.txt', 'a') as filehandle3:
    for listitem in imports_enc:
        filehandle3.write('%s\n' % listitem)
print(imports_enc)
