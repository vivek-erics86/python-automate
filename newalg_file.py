#######it works fine to avoid redundancy of folder creation

#!/usr/bin/env python

import re
import errno
import  sys
from distutils.dir_util import copy_tree
import shutil
import os
import errno
import zipapp


path = 'C:/Python27/forsourcefiles/' ####  Folder where the source files/ python scripts are present
target_dest = 'C:/Python27/Target/'  ####  Destination folder/path where the .pyz files will be stored
dirs = os.listdir(path)
length_d = len(dirs)
#print(length_d)
i = 0
for value in dirs:
    str1 = (dirs[i][0:dirs[i].find('.')])
    #print (str1)
    final_path = os.path.join(path, str1)##fetching file name to be used for opening file for reading
    source = final_path + '.py'
    target_path = os.path.join(target_dest, str1)  ##creating folder with name same as source file name
    #print (final_path)
    #print(source)
    #print(target_path)
    #for x in os.listdir('C:/test_vepc_depl/src/forpyz/Test/Target/'):##checking if the folder already exists
    if os.path.exists(target_path):
        #print("traversing")#
        #if (x == str1):
        print("folder named "' ' + str1 + ' '"already exists")
        if os.path.exists(final_path+'.py'):
           print("file "' '+source +' '"already exists")
           shutil.copy2('C:/Python27/__main__.py', target_path)##insert __main__ to newly created folder
        else:
            shutil.copy(source, target_path)###copy source .py file to path
    else:
        os.makedirs(target_path)## make folder in the same name as of the source file
        shutil.copy(source, target_path)##copy the file to the newly created folder
        shutil.copy2('C:/Python27/__main__.py', target_path)#insert __main__ to newly created folder
        print ("new folder"' '+str1+' ' "created" +' ' "created and source file inserted" )
    i=i+1
    hand = open(source)
    for line in hand:
        line = line.rstrip()
        if re.search('^import.* [a-z]+', line):  #### search for string "import."
           lib_test = line.split()  ## split the words in the line
        # print (lib_test[1])
           str2 = ''.join(lib_test[1])  ## store the module name (string after import into str2)
        #print(str2)
        # if any(x.startswith(str2) for x in os.listdir('C:/test_vepc_depl/src/non_lib/')):
           for x in os.listdir('C:/Python27/non_lib/'):
            # re.match(str2,x)
               if (x == str2):
                ##print(str2)
                  src = 'C:/Python27/non_lib/'  ### place to look for the lib files
                  src_path = os.path.join(src,str2)  ###specify name and location of the first custom library module to be read
                  destination_path = os.path.join(target_path, str2)  ###specify path to create new library module
                  copy_tree(src_path,destination_path)  ### copy the custum made library module to the newly made folder of the same name in the source file location
                  shutil.copy2('C:/Python27/__init__.py',destination_path)  ###insert the __init__.py required for the folder to be recognized as module

           #######packing the modules listed as "from"######
        if re.search('^from.* ([^a-z])', line):
            lib_test = line.split()
            abs_str3 = lib_test[1].split('.')
            # print(abs_str3[0])
            str3 = abs_str3[0]
            # print(str3)
            for x in os.listdir('C:/Python27/non_lib/'):
                # re.match(str3,x)
                if (x == str3):
                    #print(str3)
                    src = 'C:/Python27/non_lib/'  ### place to look for the lib files
                    src_path = os.path.join(src, str3)  ###specify name and location of the first custom library module to be read
                    destination_path = os.path.join(target_path, str3)  ###specify path to create new library module
                    #print(src_path)
                    #print(destination_path)
                    copy_tree(src_path,destination_path)  ### copy the custum made library module to the newly made folder of the same name in the source file location
                    shutil.copy2('C:/Python27/__init__.py',destination_path)  ###insert the __init__.py required for the folder to be recognized as module
    zipapp.create_archive(target_path, target=None, interpreter=None, main=None)


