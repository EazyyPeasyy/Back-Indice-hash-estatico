
from model.tupla import Tupla
import pageBucketSize

class Page:
    def __init__(self):
        self.maxSize = pageBucketSize.pageSize
        self.register = list()
        self.next = None
    
    #Registrando até o tamanho máximo da pagina
    #caso ultrapasse o tamanho máximo cria uma nova page
    def setRegister(self, name):
        size = len(self.register)
        if(size < self.maxSize):
            tuplaa = Tupla(name)
            self.register.append(tuplaa)
            return True
        else:
            newPage = Page()
            newPage.setRegister(name)
            self.next = newPage
            return False
