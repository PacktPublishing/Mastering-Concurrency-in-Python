# ch4/example2.py

from threading import Lock

my_lock = Lock()

# induces deadlocks
def get_data_from_file_v1(filename):
    my_lock.acquire()

    with open(filename, 'r') as f:
        data.append(f.read())

    my_lock.release()

# handles exceptions
def get_data_from_file_v2(filename):
    with my_lock, open(filename, 'r') as f:
        data.append(f.read())

data = []

try:
    get_data_from_file_v1('output2/sample0.txt')
    #get_data_from_file_v2('output2/sample0.txt')
except FileNotFoundError:
    print('File could not be found...')

my_lock.acquire()
print('Lock can still be acquired.')
