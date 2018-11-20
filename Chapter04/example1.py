# ch4/example1.py

n_files = 254
files = []

# method 1
for i in range(n_files):
    files.append(open('output1/sample%i.txt' % i, 'w'))

# method 2
'''for i in range(n_files):
    f = open('output1/sample%i.txt' % i, 'w')
    files.append(f)
    f.close()'''

# method 3
'''for i in range(n_files):
    with open('output1/sample%i.txt' % i, 'w') as f:
        files.append(f)'''
