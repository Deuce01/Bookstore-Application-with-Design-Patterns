class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Logger instance")
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        with open('logs/bookstore_log.txt', 'a') as log_file:
            log_file.write(f"LOG: {message}\n")
