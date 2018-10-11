import os
import pickle as pkl

class FileWriter:
    class help_path:
        def __init__(self,path):
            self._path = path

        def __eq__(self, other):
            return self._path == str(os.path.abspath(os.path.expanduser(other)))

        def __str__(self):
            return self._path

        def __repr__(self):
            return self._path

    def __init__(self, path):
        """path - путь до файла"""
        path = self._check_path(path)
        if path:
            self._path = path
            self._file = None
        else:
            raise Exception("Directory does not exists")
        
    def _check_path(self, path):
        path = os.path.abspath(os.path.expanduser(path))
        return path if os.path.isdir(os.path.dirname(path)) else False

    def __enter__(self):
        if os.path.exists(self._path):
            self._file = open(self._path, 'a')
        else:
            self._file = open(self._path, 'w')
        return self._file

    def __exit__(self, exc_type, exc_value, traceback):
        self._file.close()

    @property
    def path(self):
        return FileWriter.help_path(self._path)
    
    @path.setter
    def path(self, value):
        value = self._check_path(value)
        if value:
            self._path = value
        else:
            raise Exception("Directory does not exists")

    @path.deleter
    def path(self):
        del self._path
    
    def print_file(self):
        with open(self._path, 'r') as self._filej:
            print(self._file.read())
    
    def write(self, some_string):
        self._file.write(some_string)
    
    def save_yourself(self, file_name):
        with open(file_name, 'wb') as self._file:
            pkl.dump(self._path, self._file)

    @classmethod
    def load_file_writer(cls, pickle_file):
        f = open(pickle_file, 'rb')
        path = pkl.load(f)
        return FileWriter(path)