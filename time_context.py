from time import time

class TimerCtx:
    def __enter__(self):
        self.start = time()

    def __exit__(self, x_type, x_msg, x_trace):
        print(round(time() - self.start, 2))