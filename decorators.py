from time import perf_counter

def timer(f):
    def wrapper(*args, **kwds):
        start = perf_counter()
        ret = f(*args, **kwds)
        print(f"exec: {(perf_counter() - start)*1e6: .2f} us")
        return ret
    return wrapper