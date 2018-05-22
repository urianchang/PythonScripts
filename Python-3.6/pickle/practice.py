# Python 3.6
import pickle

a = ['test value 1', 'test value 2', 'test value 3']

file_name = "testfile"

# Write to file
file_object = open(file_name, 'wb')

pickle.dump(a, file_object)

file_object.close()

# Read from file
file_object = open(file_name, 'rb')

b = pickle.load(file_object)

print(b)
print(a==b)
