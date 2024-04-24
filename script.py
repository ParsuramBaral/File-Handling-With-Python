import random
def file_read() :
    file_name = input("File Name :")
    file = open(file_name, "r")
    
    for i in file:
        file_name_list = i.strip().split(',')
        for j in file_name_list:
            y = random.randint(1,9)
            print(j,str(y) + "@test.com")
file_read()
