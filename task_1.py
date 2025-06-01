import queue
import random
import time

# Створити чергу заявок
queue = queue.Queue()

#Функція generate_request():
#    Створити нову заявку
#    Додати заявку до черги

def generate_request():
    new_request = {
        'req_id': random.randint(1, 999),
        'req_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
    queue.put(new_request)
    print(f"Generated request {new_request['req_id']} created at {new_request['req_time']}")


#Функція process_request():
#    Якщо черга не пуста:
#        Видалити заявку з черги
#        Обробити заявку
#    Інакше:
#        Вивести повідомлення, що черга пуста

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request {request['req_id']} at {request['req_time']}")
    else:
        print("Queue is empty")


#Головний цикл програми:
#    Поки користувач не вийде з програми:
#        Виконати generate_request() для створення нових заявок
#        Виконати process_request() для обробки заявок
#

def main():
    while True:
        command = input("Enter the command: g-create a request, p-process a request, e-exit the program: ")
        if command == "e":
            break
        elif command == "g":
            generate_request()
            time.sleep(1)
        elif command == "p":
            process_request()
            time.sleep(1)
        else:
            print("\033[91m INCORRECT INPUT!\033[0m Please enter next command: g, p, or e.")


if __name__ == "__main__":
    main()