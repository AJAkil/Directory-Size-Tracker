import os

path = 'C:\Users\Asus\Music\\tester'



'''This function recursively prints the total disk usage of a working directory'''
def disk_usage(dir_path, size_list):

    '''we get the size of the current path'''
    total_size = 0
    #print('total_size at the beginning = '+ str(total_size))
    
    '''we check whether the current path is an directory, if yes, we recursively proceed ahead'''
    if(os.path.isdir(dir_path)):
        #print('entered for the path = ' + dir_path)
        for file_stuffs in os.listdir(dir_path):

            child_path = os.path.join(dir_path, file_stuffs)
            child_size = os.path.getsize(child_path)

            #print('path = {} child size = {}'.format(child_path, child_size))
            

            if(child_size != 0L):
                print('{} ---> {}'.format(child_path, child_size))
                size_list.append(child_size)

            #print('state before entering recursion '+ child_path)
            #print('before == ' + str(total_size))
            disk_usage(os.path.join(dir_path, file_stuffs), size_list)
            total_size += size_list[len(size_list)-1]
            #print('total Size afte adding up = '+str(total_size))
            #print('after == ' + str(total_size))

        if(total_size != 0L):
            print('entered here')
            print('{} ---> {}'.format(dir_path, total_size))
            size_list.append(total_size)
    
    return size_list


if __name__ == '__main__':
    sizes = disk_usage(path, [])
    sizes = [int(s) for s in sizes]
    sizes.sort(reverse = True)
    print(sizes)
