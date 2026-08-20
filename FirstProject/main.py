from pathlib import Path
import os


def createFile():
    try:
        name = input("Tell file name plz:-")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as f:
                data = input("what you wannt to write in this file:-")
                f.write(data)
            print("file Created Successfully")    
        else:
            print("Error file name already exist")
    except Exception as error:
        print(f"an error {error} occured")


def readFile():
    try:
        name = input("Pleas tell me your file name :-")
        path = Path(name)
        if path.exists():
            with open(path,"r")as f:
                content = f.read()
                print(content)
        else:
            print("file does not exist.")
    except Exception as error:
        print(f"an error {error} occured")


def updateFile():
    try:
        name = input("enter file name")
        path = Path(name)
        if path.exists():
            print("1. Renaming file")
            print("2. Appending the content")
            print("3. OverWriting the content")
            choise = int(input("enter YOur Option:-"))
            if choise == 1:
                newname = input("tell Your new file Name:-")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed succcessfully")
                else :
                    print("file already exists")

            elif choise == 2:
                with open(path,"a") as fs:
                    data = input("what do you wanna to appended:-")
                    fs.write(" \n "+data)
                print("successfully Apppended")


            elif choise == 3:
                with open(path,'w') as fs:
                   data = input("what do you wanna to appended:-")
                   fs.write(data)
                print("successfully OverWrite")

        else :
            print("file not exists")
          


    except Exception as error:
        print(f"an error {error} occured")


def deleteFile():
    try:
        name = input("Enter file name")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("Delete Successfully")
        else : 
            print("Not file exist")
    except Exception as error:
        print(f"Error {error} occured")

print("press 1 for (creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

a = int(input("\ntell your response please: -"))

if a == 1:
    createFile()
elif a == 2:
    readFile()
elif a == 3:
    updateFile()
elif a == 4:
    deleteFile()
else:
    print("Not allowed Options")