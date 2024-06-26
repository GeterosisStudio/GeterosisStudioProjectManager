import socket
import time
import threading


class Client:
    def __init__(self):
        self.client_status = False
        self.client_host = ""
        self.client_port = 0
        self.timeout = 3
        self.out_messages = []
        self.out_messages_lock = threading.RLock()
        self.in_messages = []
        self.in_messages_lock = threading.RLock()

    def set_client_host(self, client_host):
        self.client_host = client_host
        return self.client_host

    def get_client_host(self):
        return self.client_host

    def set_client_port(self, client_port):
        self.client_port = client_port
        return self.client_port

    def get_client_port(self):
        return self.client_port

    def set_timeout(self, timeout):
        self.timeout = timeout

    def get_timeout(self):
        return self.timeout

    def send_data(self, sock):
        while self.client_status:
            if not self.out_messages:
                print("Клиент: Данных для отправки нет.")
                time.sleep(self.timeout)
                continue

            # Вводим данные для отправки
            self.out_messages_lock.acquire()
            data = self.out_messages[0]
            # Отправляем данные серверу
            print(f"Клиент: Отправляем данные серверу. {0}".format(data))
            try:
                sock.sendall(data.encode())
                # Получаем ответ от сервера
                response = sock.recv(1024).decode()
                print(response)
                if response == data:
                    del self.out_messages[0]
                    self.out_messages_lock.release()
            except:
                print("Ошибка отправки.")
                self.out_messages_lock.release()
                break

    def get_message(self):
        self.in_messages_lock.acquire()
        if self.in_messages:
            data = self.in_messages[0]
            del self.in_messages[0]
            self.in_messages_lock.release()
            return data
        else:
            self.in_messages_lock.release()
            return None
    def add_message(self, data):
        self.in_messages_lock.acquire()
        self.out_messages.append(data)
        print(f"Сообщение добавлено: {0}".format(data))
        self.in_messages_lock.release()



    def check_port(self, timeout=3):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((self.client_host, self.client_port))
            s.close()
            return True
        except:
            return False

    def receive_data(self, s):
        while True:
            try:
                data = s.recv(1024).decode()
                print('Полученные данные от сервера:', data)
            except Exception as e:
                print(f"Ошибка приема. {0}".format(e))
                break

    def client_thread(self):
        # Создаем сокет
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(self.timeout)
            # Бесконечный цикл для подключения и обработки данных
            while self.client_status:
                try:
                    # Проверяем состояние сокета
                    if s.connect_ex((self.client_host, self.client_port)) == 0:
                        print("Клиент: Подключено к серверу.")
                        # Запускаем потоки для отправки и приема данных
                        send_thread = threading.Thread(target=self.send_data, args=(s,))
                        receive_thread = threading.Thread(target=self.receive_data, args=(s,))
                        send_thread.start()
                        receive_thread.start()
                        # Ждем завершения потоков
                        send_thread.join()
                        receive_thread.join()
                    else:
                        print(f"Сервер недоступен, попытка переподключения в секундах: {self.timeout}")
                        return False
                except ConnectionRefusedError:
                    print(f"Сервер недоступен, попытка переподключения в секундах: {self.timeout}")
                    return False

    def client_loop(self):
        while self.client_status:
            self.client_thread()
        print("Клиент остановлен.")

    def start_client(self):
        self.client_status = True
        client_loop = threading.Thread(target=self.client_loop)
        client_loop.start()

    def stop_client(self):
        print("Клиент в процессе остановки.")
        self.client_status = False


if __name__ == "__main__":
    import Settings.Settings as Settings
    client = Client()
    config = Settings.get_config()
    client.set_client_host(config["Project browser"]["host"])
    client.set_client_port(config["Project browser"]["port"])
    client.set_timeout(1)
    client.start_client()
    time.sleep(5)
    client.stop_client()
