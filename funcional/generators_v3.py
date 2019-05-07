#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

def sequencia():
    num = 0
    while True:
        num += 1
        yield num

if __name__ == "__main__":
    seq = sequencia()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))