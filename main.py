import sys

from util import Util
# problema com o arquivo grande
sys.setrecursionlimit(2500)

util = Util()
print("reading file...")
util.readFile("words.txt")
print(util.ver())
print(util.busca("representability"))