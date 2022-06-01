def menuOption():
    print('1. Registrar usuario')
    print('2. Editar usuario')
    print('3. Entrar al parque')
    print()
    return input()

def askCreds():
    name = input('name: ')
    password = input('password: ')
    return name, password

def askNewCreds():
    name = input('name: ')
    password = input('password: ')
    newName = input('name: ')
    newPassword = input('password: ')
    return name, password, newName, newPassword


