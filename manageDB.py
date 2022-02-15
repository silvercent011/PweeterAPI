from models import User, Pweet
def ManageDB():
    try:
        User.User.create_table()
        print('Tabela User criada')
    except:
        print('Tabela User já criada previamente')
    try:
        Pweet.Pweet.create_table()
        print('Tabela Pweet criada')
    except:
        print('Tabela Pweet já criada previamente')