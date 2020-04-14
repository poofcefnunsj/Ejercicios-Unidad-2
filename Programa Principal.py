import csv

from claseEmail import Email

from claseManejadorEmail import manejadorEmail

if __name__ == '__main__':

    print('Ingrese los siguientes datos:')

    nombre = input('Nombre:')
    idCuenta = input('Id de la cuenta:')
    dominio = input('Dominio de la cuenta:')
    tipoDominio = input('Tipo de dominio de la cuenta:')
    contrasena = input('Contrasena:')

    mail = Email(idCuenta, dominio, tipoDominio, contrasena)

    print(' ')
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, mail.__str__()))
    print(' ')
    # aca termina el punto 1

    print('A continuación se cambiará la contraseña ingresada anteriormente,')
    print('para eso deberá escribirla correctamente, en caso contraria se mostrará un mensaje de error.')
    print(' ')
    contrasena = input('Ingrese contraseña actual:')
    mail.modificarContrasena(contrasena)
    print(' ')
    # aca termina el punto 2

    print('A continuación se creará un objeto de tipo Email mediante un mail ingresado')
    email = manejadorEmail(input('Ingrese un mail:'))
    x = email.crearObjeto()
    if type(x) == Email:
        print('El identificador del objeto creado es x')
    # aca termina el punto 3

    dominio = input('Ingrese un dominio:')
    cont = 0
    archivo = open('archivo.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        if fila[1] == dominio:
            cont += 1
    print('La cantidad de mails con el dominio ingresado es:', cont)
    archivo.close()
