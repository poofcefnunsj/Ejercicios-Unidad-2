class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasena = ''

    def __init__(self, id='', dom='', tipo='', passw=''):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipoDominio = tipo
        self.__contrasena = passw

    def __str__(self):
        return self.__idCuenta + '@' + self.getDominio() + '.' + self.__tipoDominio

    def getDominio(self):
        return self.__dominio

    def modificarContrasena(self, passvieja):
        if passvieja == self.__contrasena:
            self.__contrasena = input('Ingrese nueva contraseña:')
            print('La contraseña se cambió correctamente')
        else:
            print('ERROR: la contraseña ingresada es incorrecta')

    def modificarContraseña(self, contrasena):
        pass
