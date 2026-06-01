from pathlib import Path
import os

def readfileandfolder():
    path = Path(' ')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the file name: ")
        p = Path(name)
        if not p.exists() and p.is_file():           
            with open(name,"w") as f:
                data = input("Enter the data: ")
                f.write(data)
            print(f"{name} created successfully")
        else:
            print(f"{name} created successfully")
    except Exception as e:
        print(f"sorry there is an error of {e}.")  

def readfile():
    try:
        readfileandfolder()
        name = input("Enter the file name which do u want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name,"r") as f:
                data = f.read()
                print(f"The content of the file is: {data}")
        else:
            print(f"{name} does not exist.")

    except Exception as e:
        print(f"sorry there is an error of {e}.")


def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the file name which do u want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 to change name the of file")
            print("press 2 to overwrite the content of file")
            print("press 3 for append the content of file")

            res = int(input("Enter your opinion: "))

            if res == 1:
                newname = input("Enter the new name of the file: ")
                p2 = Path(newname)
                p.rename(p2)
            if res == 2:
                with open(name,'w') as f:
                    data = input("enter the data to overwrite: ")
                    f.write(data)
            if res == 3:
                with open(name,'a')as f:
                    data = input("enter the data to append: ")
                    f.write(data)
    except Exception as e:
        print(f"sorry there is an error of {e}.")  

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the file name which do u want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print(f"{name} deleted successfully.")
        else:
            print(f"{name} does not exist.")
    except Exception as e:
        print(f"sorry there is an error of {e}.")


print("press 1 to create a file")
print("press 2 to read a file")
print("press 3 to update a file")
print("press 4 to delete a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()