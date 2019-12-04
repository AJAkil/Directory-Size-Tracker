import os
from collections import OrderedDict
import pprint

path = 'C:\Users\Asus\Music\\tester'



'''This function recursively prints the total disk usage of a working directory
def disk_usage(dir_path, size_list):

    we get the size of the current path
    total_size = 0
    #print('total_size at the beginning = '+ str(total_size))
    
    we check whether the current path is an directory, if yes, we recursively proceed ahead
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
            if os.path.isdir(child_path):
                disk_usage(os.path.join(dir_path, file_stuffs), size_list)

            total_size += size_list[len(size_list)-1]
            #print('total Size afte adding up = '+str(total_size))
            #print('after == ' + str(total_size))

        if(total_size != 0L):
            print('entered here')
            print('{} ---> {}'.format(dir_path, total_size))
            size_list.append(total_size)
    
    return size_list
'''


def disk_usage(dir_path, path_size_dict):

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
                #print('{} ---> {}'.format(child_path, child_size))
                path_size_dict[child_path] = child_size 

            #print('state before entering recursion '+ child_path)
            #print('before == ' + str(total_size))
            if os.path.isdir(child_path):
                disk_usage(os.path.join(dir_path, file_stuffs), path_size_dict)

            total_size += path_size_dict.values()[-1]
            #print('total Size afte adding up = '+str(total_size))
            #print('after == ' + str(total_size))

        if(total_size != 0L):
            #print('entered here')
            #print('{} ---> {}'.format(dir_path, total_size))
            path_size_dict[dir_path] = total_size
    
    return path_size_dict


def dict_sort_by_val(dict):
    return sorted(dict.items(), key = lambda k: (k[1], k[0]), reverse=True)  


def structure_sorted_dict(sorted_dict):
    
    pp = pprint.PrettyPrinter(indent=6)

    for items in sorted_dict:
        (path, size) = items
        pp.pprint('{} ----> {}'.format(path, size))



if __name__ == '__main__':

    d = OrderedDict()
    sizes = disk_usage(path, d)
    list_of_sorted_tuples = dict_sort_by_val(d)
    
    structure_sorted_dict(list_of_sorted_tuples)
