import os
def menu():
        strs = ('Enter 1 for update\n'
                'Enter 2 for import\n'
                'Enter 3 for add   \n'
                'Enter 0 to exit : ')
        choice = input(strs)
        return int(choice) 
print("/////")
x= int(input('Enter 1 for update\n'
                'Enter 2 for import\n'
                'Enter 3 for add   \n'
                'Enter 0 to exit : '))
while x != "":
  if x==1:
    if input("This operation will delete the old data\nare you sure? (y/n)") == "y":
      exec(open('update.py').read())
    else :
      exit()
    x = menu()
  elif x==2:
    exec(open('import.py').read())
    x = menu()
  elif x==3:
    exec(open('add_to.py').read())
    x = menu()
  elif x==0:
    break;
  else :
    print("put a valid number")
