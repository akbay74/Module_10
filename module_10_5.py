import multiprocessing
from datetime import datetime
import glob
import os

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line != '':
            all_data.append(line)
            line = file.readline()

num_files = sum(os.path.isfile(f) for f in glob.glob('./*.txt'))
all_files = [f'./file {f}.txt' for f in range(1, num_files+1)]

# Линейный метод
start = datetime.now()
for f in all_files:
    read_info(f)
end = datetime.now()
print(end - start)  # 0:00:05.391137

# Многопроцессорный метод
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, all_files)
    end = datetime.now()
    print(end - start) #  0:00:01.996923