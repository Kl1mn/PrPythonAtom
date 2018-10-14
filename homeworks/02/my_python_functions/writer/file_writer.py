import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self._path = path
            self._file = None
        else:
            raise Exception("Directory does not exists")
        
    def _check_path(self, path):
        path = os.path.abspath(os.path.expanduser(path))
        return os.path.isdir(os.path.dirname(path))

    def __enter__(self):
        self._file = open(self._path, 'a')

    def __exit__(self, exc_type, exc_value, traceback):
        self._file.close()

    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, value): 
        if self._check_path(value):
            self._path = value
        else:
            raise Exception("Directory does not exists")

    @path.deleter
    def path(self):
        self._path = ''
    
    def print_file(self):
        with open(self._path, 'r') as self._file:
            print(self._file.read())
    
    def write(self, some_string):
        self._file.write(some_string)
    
    def save_yourself(self, file_name):
        self._file = None
        with open(file_name, 'wb') as file:
            pkl.dump(self, file)

    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as file:
            newWriter = pkl.load(file)
            return newWriter