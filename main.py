from claseEmail import Email
import csv
import re 



if __name__ =='__main__':
    nombre = input("Ingrese nombre: ")
    idCuenta = input("Ingrese el id de la cuenta: ")
    dominio = input("Ingrese el dominio de la cuenta: ")
    tipoDominio = input("Ingrese el tipo de dominio de la cuenta: ")
    contrasena = input("Ingrese la contraseña: ")
    
    unEmail = Email(idCuenta, dominio, tipoDominio, contrasena)
    print("Estimado "+ nombre + " te enviaremos tus mensajes a la direccion "+ unEmail.getCorreo())
    contrActual=input("Ingrese la contraseña actual: ")
    unEmail.modificarContra(contrActual)
    unEmail2 = Email(0,0,0,0)
    unEmail2.cuenta('informatica.fcefn@gmail.com')
    print(f"correo: {unEmail2.getCorreo()}")
    
    archivo=open('email.csv')
    reader =csv.reader(archivo,delimiter=",")
    for fila in reader:
        direccion=fila[0]
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(patron,direccion):
            unmail = Email(0,0,0,0)
            unmail.cuenta(direccion)
            print(f"Cuenta creada exitosamente para {unmail.getCorreo()}")
        else:
            print(f"Direccion {direccion} no valida") 
    archivo.close()
    dom=input("Ingresar un dominio: ")
    cant = 0
    archivo=open('email.csv')
    reader =csv.reader(archivo,delimiter=",")
    for fila in reader:
        direccion=fila[0]
        partes = direccion.split("@")
        if (len(partes)>=2):
            partes2=partes[1].split(".")
            domi=partes2[0]
            if (domi==dom):
                cant=cant +1
    archivo.close()
    print(f"La cantidad de usuarios registrados con ese dominio es {cant}")#cuenta todos incluyendo las cuentas no validas
    
    
    
               
            
        
    
    
    
       
    
    
