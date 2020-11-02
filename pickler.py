import pickle
import os
from converter import *


class Pickler:

    def __init__(self):
        self.new_file_name = ''
        self.to_be_pickled = ''

        self.file_to_pickle = ''
        self.pickle_name = ''

    # edan's work
    def serialise(self, to_pickle):
        pickle_file = open('pickle.txt', 'wb')
        pickle.dump(to_pickle, pickle_file)
        print(to_pickle)
        pickle_file.close()

    # Jack's work
    def use_pickle(self):
        print('Starting Pickle...')
        try:
            if os.path.exists('pickle.txt'):
                pickle_file = open('pickle.txt', 'rb')
                load_file = pickle.load(pickle_file)
                return load_file
            else:
                print('Cannot find a pickle file, please try {create_pickle} first!')

        except FileNotFoundError as e:
            print(e)

    def convert(self, data):
        if isinstance(data, bytes):  return data.decode('utf-8')
        if isinstance(data, dict):   return dict(map(self.convert, data.items()))
        if isinstance(data, tuple):  return map(self.convert, data)
        return data

    def delete_pickle(self, pickle_name):
        try:
            if os.path.exists(pickle_name):
                os.remove(pickle_name)
                print(pickle_name + ' deleted!')
            else:
                print('You have not create a pickle, please try {create_pickle} first!')

        except FileNotFoundError as e:
            print(e)

if __name__ == '__main__':
    p = Pickler()
    """"
    c = Converter()
    c.load_data("JStest1.js")
    c.visit(c.extract_data(c))
    c.convert_to_uml()
    c.make_pickle()
    p.use_pickle()
    print(p.convert(p.use_pickle()))
    """
    p.delete_pickle("pickle1.txt")
