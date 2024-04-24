def file_read() :
    file_name = input("File Name :")
    file = open(file_name, "r")
    contents = file.read()
    print(contents)
file_read()