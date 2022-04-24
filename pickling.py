import pickle

mydict = {'1': 'a', '2': 'b'}
pickle_file = open('pickled.txt', 'wb')  # write byte
pickle.dump(mydict, pickle_file)  # dump or store

pickle_file = open('pickled.txt', 'rb')  # read byte
newmydict = pickle.load(pickle_file)  # load from the dumped file

print(newmydict)
