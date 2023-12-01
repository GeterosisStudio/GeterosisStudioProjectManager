import socket
import time
import threading

HOST = '127.0.0.1'  # Локальный хост
PORT = 12345        # Локальный порт


def send_data(s):
    while True:
        # Вводим данные для отправки
        data = input("Введите данные для отправки: ")
        # Отправляем данные серверу
        try:
            s.sendall(data.encode())
            # Получаем ответ от сервера
            response = s.recv(1024).decode()
            print('Полученный ответ:', response)
        except:
            print("Ошибка отправки.")
            break

def receive_data(s):
    while True:
        try:
            data = s.recv(1024).decode()
            print('Полученные данные от сервера:', data)
        except:
            print("Ошибка приема.")
            break

def client_thread():
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Бесконечный цикл для подключения и обработки данных
        while True:
            try:
                # Проверяем состояние сокета
                if s.connect_ex((HOST, PORT)) == 0:
                    print("Подключено к серверу")
                    # Запускаем потоки для отправки и приема данных
                    send_thread = threading.Thread(target=send_data, args=(s,))
                    receive_thread = threading.Thread(target=receive_data, args=(s,))
                    send_thread.start()
                    receive_thread.start()
                    # Ждем завершения потоков
                    send_thread.join()
                    receive_thread.join()
                else:
                    print("Сервер недоступен, попытка переподключения через 3 секунды...")
                    time.sleep(3)  # Ждем 3 секунды и пытаемся подключиться снова.
                    return False
            except ConnectionRefusedError:
                print("Сервер недоступен, попытка переподключения через 3 секунды...")
                time.sleep(3)  # Ждем 3 секунды и пытаемся подключиться снова.
                return False

def client_loop():
    while True:
        client_thread()

if __name__ == "__main__":
    client = threading.Thread(target=client_loop)
    client.start()