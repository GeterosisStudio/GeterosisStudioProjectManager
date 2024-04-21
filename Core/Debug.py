import logging

class Debug(logging.Logger):
    def __init__(self, name='Debug', level=logging.DEBUG):
        super().__init__(name, level)

    def log_user_info(self, user_id, message):
        self.info(f'User {user_id}: {message}')

my_logger = Debug()
my_logger.log_user_info(123, 'Logged in successfully')