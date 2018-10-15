class ExecucaoException(Exception):

    def __init__(self):
        super().__init__('Há erros no código')