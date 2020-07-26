# this is os module quiz 
# in this a quiz we make a programm that the programm is give a user input for full path and user input the full path and agian programm is give a user input with folder you go .

import os

# this is a function

def soldier_Excersice(path,file,format):
    os.chdir(path)
    i = 0
    files_ = os.listdir(path)

    with open(file) as f:
        f_list = f.read().split("\n")

    for file in files_ :
        if file not in files_:
            os.rename(file,file.capitalize()) 

        if os.path.splitext(file)[1] == format:
            os.rename(file,f"{i}.{format}")
            i += 1

if __name__ == "__main__":
    try:
        print("Enter Your path:")
        path_our = input()
        print("Enter your file path:")
        files = input()
        print("Enter your format :")
        formats = input()
        soldier_Excersice(path_our,files,formats)                
    except:
        print("Something wrong, check you path,file and format.")    
    # soldier_Excersice(r"D:\Aric\Temps file\temps",r"D:\Aric\Temps file\temps\main.txt",".png")                



