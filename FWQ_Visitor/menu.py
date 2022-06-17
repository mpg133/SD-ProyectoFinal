def menuOption():
    print('1. Registrar usuario')
    print('2. Editar usuario')
    print('3. Registrar usuario via API')
    print('4. Editar usuario via API')
    print('5. Entrar al parque')
    print('6. Salir')
    print()
    return input()

def askCreds():
    name = input('Insert name: ')
    password = input('Insert password: ')
    return name, password

def askNewCreds():
    name = input('Insert name: ')
    password = input('Insert password: ')
    newName = input('Insert new name: ')
    newPassword = input('Insert new password: ')
    return name, password, newName, newPassword


