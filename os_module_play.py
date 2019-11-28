import os

path = os.getcwd()

file_size = os.path.getsize(path+'\\b.txt')

#print(file_size)

#print(type(os.listdir(path)))


def disk_usage(dir_path):

    '''we get the size of the current path'''
    total_size = os.path.getsize(dir_path)
    
    '''we check whether the current path is an directory, if yes, we recursively proceed ahead'''
    if(not os.path.isfile(dir_path)):

        for file_stuffs in os.listdir(dir_path):
            child_path = os.path.join(dir_path, file_stuffs)
            total_size += disk_usage(child_path)
                

    print('{} ---> {}'.format(dir_path, total_size))
    return total_size


 disk_usage(path)
