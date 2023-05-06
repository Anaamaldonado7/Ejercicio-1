class Email:
    __idCuenta =''
    __dominio =''
    __tipoDom =''
    _contra =''
   #a
    def __init__ (self, idCuenta, dominio, tipoDom, contra):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDom = tipoDom
        self._contra = contra
    #b      
    def getCorreo(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDom
   #c
    def getDominio(self):
        return self.__dominio
   #d
    def cuenta(self,correo):
        partes = correo.split("@")
        self.__idCuenta = partes[0]
        dominio_tipo = partes[1].split(".")
        self.__dominio = dominio_tipo[0]
        self.__tipoDom = dominio_tipo[1]
       
        
    def modificarContra(self, actual):
      if actual == self._contra:
       nueva=input("Ingrese la contraseña nueva: ")
       self._contra=nueva
       print("La contraseña fue cambiada con exito \n")
      else :
          print("Contraseña incorrecta")
       