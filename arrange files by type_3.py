# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:29:17 2019

@author: rampa
"""

# Python program to sort files by type

## Sorts files by their extension type and moves to a selected folder

# importing the necessary libraries
import os
import shutil

# Enter the path that you want to sort
path = '/Users/rampa/Desktop'

# Enter the destination to which you want to sort and send all the files
path_2='/Users/rampa/Desktop/Desk_files'

# Using try function to make a directory
try:
    os.mkdir(path_2)
except OSError:
    print ("Creation of the directory %s failed" % path_2)
else:
    print ("Successfully created the directory %s" % path_2)

#Create a function that takes input and sorts by type
def Sort_by_type(path):
    # making a list of all the files 
    list_=os.listdir(path)
    # This will go through each and every file 
    for file_ in list_: 
        name, ext = os.path.splitext(file_) 

        # This is going to store the extension type 
        ext = ext[1:] 

        if name != "Desk_files":
            # This forces the next iteration, 
            # if it is the directory 
            if ext == '': 
                continue

            # This will move the file to the directory 
            # where the name 'ext' already exists 
            if os.path.exists(path+'/'+ext): shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 

            # This will create a new directory, 
            # if the directory does not already exist 
            else: 
                os.makedirs(path+'/'+ext) 
                shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
        else:
            print("All good cases executed")

#Function executed for the given path
Sort_by_type(path)

#Move all the files to Desk_files folder in documents
source = '/Users/rampa/Desktop'
dest = '/Users/rampa/Desktop/Desk_files'

files = os.listdir(source)
for f in files:
    if f != "Dest_files":
        shutil.move(source+"/"+f,dest)
    else:
        print("Executed")
