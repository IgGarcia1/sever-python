# coding: utf-8

class Subcontroler():

    def __init__(self, entrada, codigo, index, userID, appendFile=False, last=False):
        try:
            from ConversorJson import ConversorJson
            from ExecuteCode import ExecuteCode
            from ExecucaoException import ExecucaoException
        except:
            from corretor.ConversorJson import ConversorJson
            from corretor.ExecuteCode import ExecuteCode
            from corretor.ExecucaoException import ExecucaoException

        
        self.__numberCase = index 
        self.__code = codigo 
        self.__enters = entrada 
        self.__userID = userID

        self.__conversor = ConversorJson(str(userID), appendFile)
        try:
            self.__runner = ExecuteCode(self.getEnters(), self.getCode(), self.getUser())
        except Exception as e:
            raise e
       

        self.main(last)

    ###  GETs ####
    def getRunner(self):
        return self.__runner
    def getConversor(self):
        return self.__conversor
    def getUser(self):
        return self.__userID
    def getCode(self):
        return self.__code
    def getEnters(self):
        return self.__enters
    def getNumberCase(self):
        return self.__numberCase


    def main(self, last):
        import json 

        convertionCopy = self.getConversor()
        execution = self.getRunner()
        
        saidasGeradas = open(str(self.getUser())+'.txt').readlines()
        
        stringSaida = []
        [stringSaida.append(saida) for saida in saidasGeradas]
        
        stringSaida = json.dumps(stringSaida, ensure_ascii=False)
        
        convertionCopy.addAtributte('"case'+str(self.getNumberCase())+'"', end=':')
       
        if last:
            convertionCopy.addAtributte(stringSaida, end='')
            convertionCopy.finalizeFile()
        else:
            convertionCopy.addAtributte(stringSaida)


#codigoTeste = """print("olá mundo!")\nprint(1+1)\nprint('{}:{}'.format(18, 50))"""
#c = Subcontroler([], codigoTeste, 1, '152user-uid')

