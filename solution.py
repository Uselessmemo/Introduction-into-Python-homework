class FileReader:
    def __init__(self, path):
        self.path = path
    
    def read(self):
        try:
            f = open (self.path, 'r')
            data = f.read()
            f.close()
            return data

        except FileNotFoundError:
            data = ''
            return data

