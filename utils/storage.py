from tinydb import Storage
import pickle


class StoragePickle(Storage):

    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, 'rb') as handle:
            try:
                donnees = pickle.load(handle)
                return donnees
            except EOFError:
                None

    def write(self, donnees):
        with open(self.filename, 'wb+') as handle:
            pickle.dump(donnees, handle)
    
    def close(self):
        pass

"""except FileNotFoundError:
                       return None
                   except IOError:
                       pass
                   except pickle.PickleError:
                       return None"""
