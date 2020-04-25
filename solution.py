import os.path
import tempfile

class File():
    def __init__(self, file_name):
        self.file_name = file_name
        self.path = file_name
        with open(self.path, 'w+'):
            pass

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()
    
    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)
        
    def __add__(self, obj):
        new_obj = File(os.path.join(tempfile.gettempdir(), str(hash(self.file_name + obj.file_name))))
        #new_obj = object.__init__(os.path.join(tempfile.gettempdir(), str(hash(self.file_name + obj.file_name))))
        new_obj.file_name = str(hash(self.file_name + obj.file_name))
        new_obj.path = os.path.join(tempfile.gettempdir(), new_obj.file_name)
        with open(new_obj.path, 'w') as f:
            f.write(self.read() + obj.read())
        return new_obj
    
    def __str__(self):
        return(self.path)
    
    def __iter__(self):
        with open(self.path, 'r') as f:
            self. strs = f.readlines()
            self.top = len(self.strs)
            self.current = 0
        return iter(self.strs)
    
    def __next__(self):
        if self.current >= self.top:
            raise StopIteration
        current = self.current
        self.current += 1
        return self.strs[current]  