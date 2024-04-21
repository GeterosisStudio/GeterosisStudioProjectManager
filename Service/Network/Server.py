import socket
import threading
import time


class Server:

    def __init__(self):
        self.in_meassages = []
        self.lock_in_meassages = threading.RLock()
        self.out_messages = []
        self.lock_out_messages = threading.RLock()
        self.server_status = False
        self.server_host = ''
        self.server_port = 0
        self.timeout = 1

    def set_server_host(self, server_host):
        self.server_host = server_host
        return True

    def get_server_host(self):
        return self.server_host

    def set_server_port(self, server_port):
        if isinstance(server_port, int):
            self.server_port = server_port
            return True
        return False

    def get_server_port(self):
        return self.server_port

    def set_timeout(self, timeout):
        self.timeout = timeout
        return self.timeout

    def get_timeout(self):
        return self.timeout

    def check_free_addres(self, host=None, port=None):
        import Settings.Settings as Settings
        from Service.Network.Client import Client
        config = Settings.get_config()
        client = Client()

        if host:
            client.set_client_host(host)
        else:
            client.set_client_host(config["Project browser"]["host"])
        if port:
            client.set_client_port(port)
        else:
            client.set_client_port(config["Project browser"]["port"])

        if not client.check_port():
            print("Адрес свободен")
            return True
        else:
            print("Адрес занят")
            return False

    def handle_client(self, client_socket, client_address):
        # Обработка входящих сообщений от клиента
        while self.server_status:
            try:
                # Получение данных от клиента
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    continue
                self.lock_in_meassages.acquire()
                self.in_meassages.append(data)
                print(f"Сервер: Клиент прислал: {0}".format(data))
                # Отправка ответа клиенту
                client_socket.sendall("Сервер: Сообщение получено: ".encode('utf-8'))
                self.lock_in_meassages.release()
            except ConnectionResetError:
                print("Сервер: Ошибка приема.", ConnectionResetError)
                continue
        # Закрытие соединения с клиентом
        client_socket.close()
        print(f"Соединение для клиента закрыто: {client_address[0]}:{client_address[1]}")

    def check_client_connection(self, client_thread, client_address):
        while self.server_status:
            time.sleep(1)
            if not client_thread.is_alive():
                print(f"Клиент отключен: {client_address[0]}:{client_address[1]}")
                break

    def start_server(self):
        self.server_status = True
        server_thread_loop = threading.Thread(target=self.server_loop)
        server_thread_loop.start()

    def server_loop(self):
        # Создание серверного сокета
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.settimeout(self.timeout)
        # Привязка серверного сокета к хосту и порту
        server_socket.bind((self.server_host, self.server_port))

        # Ожидание подключений от клиентов
        server_socket.listen(4)
        print(f"Сервер запущен. Ожидание подключений на {self.server_host}:{self.server_port}...")

        while self.server_status:
            # Принятие подключения от клиента
            try:
                client_socket, client_address = server_socket.accept()
                # остальной код
            except socket.timeout:
                continue  # продолжить цикл, если истек таймаут
            # остальной код
            print(f"Подключен клиент: {client_address[0]}:{client_address[1]}")

            # Запуск потока для обработки клиента
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

            # Запуск потока для проверки подключения клиента
            check_thread = threading.Thread(target=self.check_client_connection, args=(client_thread, client_address))
            check_thread.start()
        if not self.server_status:
            print("Сервер остановлен.")

    def stop_server(self):
        self.server_status = False
        print("Сервер в процессе остановки...")
        return True


if __name__ == '__main__':
    import Settings.Settings as Settings

    server = Server()
    config = Settings.get_config()
    server.set_server_host(config["Project browser"]["host"])
    print(server.get_server_host())
    server.set_server_port(config["Project browser"]["port"])
    print(server.get_server_port())
    server.set_timeout(1)
    if server.check_free_addres():
        server.start_server()
    time.sleep(15)
    server.stop_server()
