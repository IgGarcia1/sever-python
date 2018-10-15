
class ExecuteCode():
    
    def getCode(self):
        return self.__code

    def getEntradas(self):
        return self.__entradas

    def deleteEntrada(self, index):
        del(self.__entradas[index])

    def meuInput(self, *args):
        retornado = self.getEntradas()[0]
        self.deleteEntrada(0)
        return retornado
    
    def meuPrint(self, *args, **kargs):
        endAtributte = ""
        sepAtributte=" "
        string=""
        try:
            sepAtributte = kargs['sep'] 
        except: pass

        tam=len(args)
        for x in range(tam):
            string += str(args[x])
            if x != tam-1:
                string+=str(sepAtributte)

        try:
            endAtributte = kargs['end']
        except: 
            endAtributte = '\n'
        string+=str(endAtributte)

        f = open(str(self.__fileName)+".txt", "a")
        f.write(string)
        f.close()
        
    def runCode(self, code, p, i):
        print = p 
        input = i 
        try:
            exec(code)
        except Exception as e:
            try:from ExecucaoException import ExecucaoException
            except: from corretor.ExecucaoException import ExecucaoException
            raise ExecucaoException()

    def __init__(self, entradas, code, userActive):
        self.__entradas = entradas
        self.__code = code
        self.__fileName = userActive
        self.__firstPrintAdd = True
        self.clearFile(str(self.__fileName)+".txt")
        self.main()

    def clearFile(self, fileName):
        f = open(fileName, "w")
        f.close()

    def main(self): 
        print = self.meuPrint
        input = self.meuInput

        #self.testesPrint(print, input)
        self.runCode(self.getCode(), print, input)

#codigoTeste = """print("olá mundo!")\nprint(1+1)\nprint('{}:{}'.format(18, 50))\nx = input('Digite um numero')\nprint(x)\nx = input('Digite um numero')\nprint(x)"""
#v = ExecuteCode([3, 4], codigoTeste, 'usuario1')