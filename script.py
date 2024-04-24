def read_file():
    file_name = input("File Name: ")
file = open(file_name, 'r') 
content = file.read()   
read_file()
