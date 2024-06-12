
import os

#Detect file

#path ="C:\\Users\\junpe\\OneDrive\\デスクトップ\\New folder"
#* U gotta add ".filetype" after file name
#if os.path.exists(path):
#    print("This location exists")
#    if os.path.isfile(path):
#        print('This is a file')
#    elif os.path.isdir(path):
#        print('That is a directory!')
#else:
#    print('That location doesnt exist')
#--------------------------------------------------------------------------------------------------------------
#Read file

#try:
#    with open("C:\\Users\\junpe\\OneDrive\\デスクトップ\\test.txt.txt") as file:
#        print(file.read())
#except FileNotFoundError as e:
#    print('file not exist')
#    print(e)

#print(file.closed) #True or False
#--------------------------------------------------------------------------------------------------------------
#Write something in file

text = '\nApparently, this shit got appended successfully mf hahahahhahahahaha'
#with open("sometest.txt", 'w') as file:
#    file.write(text)
#Append what you write by 'a' cuz 'w' overwrite what you've wrote
#with open("sometest.txt", 'a') as file:
#    file.write(text)
#--------------------------------------------------------------------------------------------------------------
#Copy files
#copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata(file's creation and modificaction times)

import shutil

#shutil.copyfile('sometest.txt','C:\\Users\\junpe\\OneDrive\\デスクトップ\\copy.txt') #(sorce, destination)
#--------------------------------------------------------------------------------------------------------------
#Move files

source = "C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\json"
destination = "C:\\Users\\junpe\\OneDrive\\デスクトップ\\kaihasafatpenis"

#try:
#    if os.path.exists(destination):
#        print('There is already a file there')
#    else:
#        os.replace(source, destination)
#        print(source+' was moved!')

#except FileNotFoundError as e:
#    print(e)
#--------------------------------------------------------------------------------------------------------------
#Delete files

path = "C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\shitty ahh file"
#path2 = "C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\empty_folder"
path3 = "C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\folder"
try:
    os.remove(path)
    #os.rmdir(path2) #Delete empty folder
    #shutil.rmtree(path3) #Delete specified folders and all contained files
except FileNotFoundError:
    print('The file aint exist')
except PermissionError:
    print('you aint got no permission to delete that shi')
except OSError:
    print('You cannot delete that using .rmdir function')
else:
    print(path3+' was deleted')


