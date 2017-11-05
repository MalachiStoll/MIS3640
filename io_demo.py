fout = open('output.txt', 'w')
line1 = "How many roads must a man walk down\n"
fout.write(line1)
line2 = "Before you call him a man?\n"
fout.write(line2)
fout.close()

import os
cwd = os.getcwd() 
# cwd stands for “current working directory”. 
# print(cwd)

print(os.path.abspath('output.txt'))
print(os.path.exists('output.txt'))

def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# walk(cwd)


# try:    
#     fin = open('bad_file')
# except:
#     print('Now we are here.')

import pickle
t = [1, 2, 3]
print(pickle.dumps(t))

t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)

print( t1 == t2 )
