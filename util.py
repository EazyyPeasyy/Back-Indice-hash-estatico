import math
from model.bucket import Bucket
from model.page import Page
from model.table import Table
from model.tupla import Tupla


class Util:
    #pares chave-valor
    buckets = dict()

    table = Table()
    info = {"colisao": 0, "overflow": 0}
    pages = Page()


    def hash(self, name):
        value = str()
        for i in name:
            char_value = math.sqrt(ord(i))
            value += str(int(math.modf(char_value)[0] * 10))
        return int(value)

    def readFile(self, file):
        page = self.pages
        tuple = list()
        with open(file, 'r') as reader:
            for reg in reader:
                reg = reg.replace("\n", "")
                tuple.append(Tupla(reg))
                if(not page.setRegister(reg)):
                    page = page.next
        self.table.tuple = tuple
        self.hashEXE()

    def hashEXE(self):
        page = self.pages
        while(page is not None):
            tuple = page.register
            for tuplaa in tuple:
                hashAux = self.hash(tuplaa.name)
                if(hashAux not in self.buckets):
                    bucket = Bucket()
                    bucket.addRef(page)
                    self.buckets[hashAux] = bucket
                else:
                    bucket = self.buckets[hashAux]
                    self.info["colisao"] += 1
                    bucket.addRef(page)
                if(bucket.overFlow):
                    self.info["overflow"] += 1
            page = page.next

    def ver(self):
        return {"colisao": self.info["colisao"], "overflow": self.info["overflow"]}

    def busca(self, name):
        cost = int()
        index = self.hash(name)
        bucket = self.buckets[index]
        while(bucket is not None):
            for page in bucket.pages:
                for reg in page.register:
                    cost += 1
                    if reg.name == name:
                        return cost, reg.name
            bucket = bucket.nextBucket
