import logging


class Logger:
    def __init__(self, level="info"):
        self.level = level.lower()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(asctime)s] - [%(levelname)s] - [%(message)s]')

        # adding the stream handler so that we can see the output in console
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        self.log_level_decider(handler=streamHandler)
        self.logger.addHandler(streamHandler)

    def log_level_decider(self, handler):
        if self.level == "debug":
            print("Setting Log Level : DEBUG")
            handler.setLevel(logging.DEBUG)
        elif self.level == "info":
            print("Setting Log Level : INFO")
            handler.setLevel(logging.INFO)
        elif self.level == "warning":
            print("Setting Log Level : WARNING")
            handler.setLevel(logging.WARNING)
        elif self.level == "error":
            print("Setting Log Level : ERROR")
            handler.setLevel(logging.ERROR)
        else:
            message = """
                Incorrect Logging Level parameter specified please select from the following 
                debug, info, warning, error
            """
            print(message)
            print("Setting Log Level : INFO")
            handler.setLevel(logging.INFO)
