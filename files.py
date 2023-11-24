# Reading a File
# f = open('samplefile.txt', 'r')
# print(f.readline())

# Writing into a file
# f=open('samplefile.txt','w')
# print(f.write("Annamani\n"))

# Appending files
f = open('samplefile.txt', 'a')
f.write('Kamma\n')
f.write('Software Engineer\n')
f.close()

with open('samplefile.txt', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')
    
print(f)





f.close()