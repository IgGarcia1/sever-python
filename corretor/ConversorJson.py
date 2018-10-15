
class ConversorJson():

    def __init__(self, userIdentifier, append=False):
        self.__fileName = userIdentifier
        if not append:
            self.initFile()

    def addAtributte(self, atribute, end=',\n'):
        f = open(str(self.getFileName())+'.json','a')
        f.write(str(atribute)+str(end))
        f.close()

    def getFileName(self):
        return self.__fileName

    def initFile(self):
        self.clearFile()
        self.addAtributte('{', '\n')

    def finalizeFile(self):
        self.addAtributte('\n', '}')

    def clearFile(self):
        f = open(str(self.getFileName())+'.json', 'w')
        f.close()

    #@staticmethod
    def returnFileJson(self):
        name = self.getFileName()+'.json'
        return name

#c = ConversonJson('usuario1')