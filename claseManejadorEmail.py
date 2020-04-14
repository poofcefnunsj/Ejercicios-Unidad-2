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

        else:
            print('ERROR: el formato del mail es invalido')
