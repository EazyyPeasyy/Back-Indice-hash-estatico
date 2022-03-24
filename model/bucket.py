from numpy import size
import pageBucketSize

class Bucket:
    def __init__(self):
        self.pages = list()
        self.nextBucket = None
        self.overFlow = False
        self.size = 0

    #Verifica se a page ta cheia
    def max(self):
        return self.size > (pageBucketSize.bucketSize - 1)
    
    #Adiciona na page e se tiver overflow adiciona no novo bucket 
    #caso o bucket esteja vazio ele cria um bucket e adiciona
    def addRef(self, page):
        if(not self.max()):
            self.pages.append(page)
            self.size = self.size + 1
            self.overFlow = False
        else:
            if(self.nextBucket is None):
                newBucket = Bucket()
                newBucket.addRef(page)
                self.nextBucket = newBucket
                self.overFlow = True
            else:
                bucket = self.nextBucket
                bucket.addRef(page)