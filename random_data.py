import random


class RandomAccountData:

    @staticmethod
    def login(length=5):
        """
        Генерирует электронный почтовый адрес заданной длины
        :param length: длина логина (минимальное значение - 5 символов не считая домена)
        :return: случайный электронный почтовый адрес заданной длинны
        """
        domain = random.choice(['@gmail.com', '@yandex.ru', '@mail.ru', '@icloud.com'])
        n = 1
        login = ''
        while n <= length:
            login += random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
            n += 1
        login += domain
        return login

    @staticmethod
    def password(length):
        """
        Генерирует пароль заданной длинны
        :param length: длина пароля
        :return: случайный пароль заданной длинны
        """
        n = 1
        password = ''
        while n <= length:
            password += random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
            n += 1
        return password

