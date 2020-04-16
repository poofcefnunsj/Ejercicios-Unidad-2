from claseEmail import Email


class manejadorEmail:
    __mail: ''

    def __init__(self, mail=''):
        self.__mail = mail

    def crearObjeto(self):
        if (self.__mail.find("@") != -1) & (self.__mail.find(".") != -1):

            nuevoEmail = Email(self.__mail[:self.__mail.find("@")],
                               self.__mail[self.__mail.find("@") + 1:self.__mail.find(".")],
                               self.__mail[self.__mail.find(".") + 1:],
                               passw=input('Ingrese la contraseña para el nuevo objeto:'))
            print('El objeto de tipo Email fue creado correctamente.')
            return nuevoEmail
"""el código escrito para validad un mail, no es suficiente lo corrí con @., ésto es lo que produce:

    A continuación se creará un objeto de tipo Email mediante un mail ingresado
    Ingrese un mail:@.
    Ingrese la contraseña para el nuevo objeto:er
    El objeto de tipo Email fue creado correctamente.
    El identificador del objeto creado es x
"""
        else:
            print('ERROR: el formato del mail es invalido')
