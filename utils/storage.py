from tinydb import Storage
import pickle

from models.joueur import Joueur
from models.tournoi import Tournoi

class StoragePickle(Storage):

    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, 'rb') as handle:
            while True:
                try:
                    o = pickle.load(handle)
                except EOFError:
                    break
                else:
                    print(o)
                """except FileNotFoundError:
                       return None
                   except IOError:
                       pass
                   except pickle.PickleError:
                       return None"""

    def write(self, data):
        with open(self.filename, 'ab') as handle:
            for o in data:
                pickle.dump(o, handle, pickle.HIGHEST_PROTOCOL)
    
    def close(self):
        pass
