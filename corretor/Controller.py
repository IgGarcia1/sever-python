
class Controller():

    def __init__(self, jsonEntradas, codigo, user):
        self.__jsonEnters = jsonEntradas
        self.__code = codigo
        self.__user = user 
        self.main()

    def getJsonNameFile(self):
        from corretor.Subcontroler import Subcontroler
        return Subcontroler
    def getEnters(self):
        return self.__jsonEnters
    def getCode(self):
        return self.__code 
    def getUser(self):
        return self.__user

    def main(self):
        try:
            from Subcontroler import Subcontroler
            from ExecucaoException import ExecucaoException
        except:
            from corretor.Subcontroler import Subcontroler
            from corretor.ExecucaoException import ExecucaoException

        entradas = self.getEnters()
        entradasLength = len(entradas)
        
        semEntradas =False
        try: firstEnter = entradas[0]
        except: 
            firstEnter = [] 
            semEntradas = True
        if entradasLength ==1:
            semEntradas = True 
        #elif entradasLength == 0:
        try:
            Subcontroler(firstEnter, self.getCode(), 1, self.getUser(), last=semEntradas)
        except:
            raise ExecucaoException()
        

        for x in range (1,entradasLength):
            if x == entradasLength-1:
                Subcontroler(entradas[x], self.getCode(), x+1, self.getUser(), appendFile=True, last = True)
            else:
                Subcontroler(entradas[x], self.getCode(), x+1, self.getUser(), appendFile=True)

entradas = {
    "input1":["a", "b", "c"],
    "input2":["e", "f", "g"],
    "input3":["h","i","j"]
}

#c = Controller(entradas, 'print(10)\nprint(20)', 'testeUser')