from threading import Thread
from queue import Queue
from time import sleep
from random import randint

class Table():

    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe():

    list_thread = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for gs in guests:
            free_tb = True
            for tb in self.tables:
                if tb.guest is None:
                    tb.guest = gs
                    tb.guest.start()
                    self.list_thread.append(tb.guest)
                    print(f'{gs.name} сел(-а) за стол номер {tb.number}')
                    free_tb = False
                    break
            if free_tb:
                self.queue.put(gs)
                print(f'{gs.name} в очереди')

    def discuss_guests(self):
        while not (self.queue.empty()) or any(not tb.guest is None for tb in self.tables):
            for tb in self.tables:
                if not(tb.guest is None) and not(tb.guest.is_alive()):
                    print(f'{tb.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {tb.number} свободен')
                    tb.guest.join()
                    tb.guest = None
                    if not self.queue.empty():
                        tb.guest = self.queue.get()
                        print(f'{tb.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tb.number}')
                        tb.guest.start()
                        self.list_thread.append(tb.guest)

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()