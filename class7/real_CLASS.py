# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе
# Метод show должен показать информацию об объекте. Создайте два разных объекта и вызовите у них метод show

class Bank_account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def show(self):
        print(f'{self.name},{self.balance}')

my_account = Bank_account('lis',30)
friend_account = Bank_account('den',20)
my_account.show()
friend_account.show()








