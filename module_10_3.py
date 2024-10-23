from threading import Thread, Lock
from time import sleep
from random import randint

class Bank():

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 0 and self.lock.locked():
                self.lock.release()
            money = randint(50, 500)
            self.balance += money
            print(f'Пополнение: {money}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            money = randint(50, 500)
            print(f'Запрос на {money}')
            if money <= self.balance:
                self.balance -= money
                print(f'Снятие: {money}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')