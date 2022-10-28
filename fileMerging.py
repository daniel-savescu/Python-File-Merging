from sys import argv

file1 = open(argv[1])

file2 = open(argv[2])

file3 = open(argv[3],'w')

for x in file1:
    file3.write(x)

for x in file2:
    file3.write(x)

print("File merging...done!")
