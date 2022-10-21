from multiprocessing import Process, Queue
import random
import time

def add_q(q) -> None:
    try:
        data : str = input("Введите число и степень через пробел: ")
        q.put(data.split())
    except Exception as e:  
        print(e)

def calc(q) -> None:
    while 1:
        item : list = q.get()
        res : int = int(item[0]) ** int(item[1])
        summ : int = 0
        for i in range(res):
            summ+=i
        with open(f"file.txt", "a", encoding="UTF-8") as f:
            f.write("["+time.strftime("%d.%m.%Y %H:%M:%S") + "]  " + f"{item[0]}^{item[1]} = {res} >> {summ}\n")
    

if __name__ == "__main__":
    q = Queue()

    t2 = Process(target=calc, args=(q,))
    t2.start()

    while 1:
        add_q(q)
    
    t2.join()
