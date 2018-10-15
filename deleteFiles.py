def deleteFiles(nameFileTxt, nameFileJson):
    import os
    os.remove(nameFileTxt)
    os.remove(nameFileJson)