def fibonacci(quantidade, seq=(0, 1)):
    return seq if len(seq) == quantidade else \
        fibonacci(quantidade, seq + (sum(seq[-2:]),))


if __name__ == '__main__':
    for f in fibonacci(20):
        print(f)