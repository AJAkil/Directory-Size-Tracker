import os

path = os.getcwd()



'''This function recursively prints the total disk usage of a working directory'''
def disk_usage(dir_path, size_list):

    '''we get the size of the current path'''
    total_size = os.path.getsize(dir_path)
    
    '''we check whether the current path is an directory, if yes, we recursively proceed ahead'''
    if(os.path.isdir(dir_path)):
        
        for file_stuffs in os.listdir(dir_path):

            child_path = os.path.join(dir_path, file_stuffs)
            total_size += os.path.getsize(child_path)
            #print(total_size)
            child_size = os.path.getsize(child_path)

            if(child_size != 0L):
                print('{} ---> {}'.format(child_path, child_size))
                size_list.append(os.path.getsize(child_path))

            disk_usage(os.path.join(dir_path, file_stuffs), size_list)

        if(total_size != 0L):
            print('{} ---> {}'.format(dir_path, total_size))
            size_list.append(total_size)
        
    return size_list

sizes = disk_usage(path, [])
sizes = [int(s) for s in sizes]
sizes.sort(reverse = True)
print(sizes)
