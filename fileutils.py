import os
import uuid

def create_output_dns_file():
    path = os.path.join('output', str(uuid.uuid4())+'.txt')
    if(not os.path.exists('output')):
        os.mkdir('output')

    file = open(path, 'x')
    file.close()
    return path

def select_file():
    """
    Run for the folder files and return a file
    """
    file_list = os.listdir()
    for file in file_list:
        if file.endswith(".txt"):
            print(file)
    
    
def clear_file():
    """
    Clear the output files
    """
    if not os.path.exists('output'):
        print('The output directory does not exist')
        return
    for file in os.listdir('output'):
        os.remove(os.path.join('output', file))
    os.rmdir('output')
    os.remove('outputfile.txt')
    