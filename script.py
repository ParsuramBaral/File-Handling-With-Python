import random
def file_read() :
    file_name = input("File Name :")
    file = open(file_name, "r")
    for i in file:
        file_name_list = i.strip().split(',')
        for j in file_name_list:
            y = str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))
            print(j.strip()+str(y)+"@test.com")
            file = open(file_name, "w")
            file.write(j.strip()+str(y)+"@test.com")
        
file_read()
