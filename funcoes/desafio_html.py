#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

def tag(tag, *args, **kwargs):
    pass


if __name__ == "__main__":
    html = tag(
        'p',
        tag('span', 'Curso de Python 3, por'),
        tag('span', 'Curso de Python 3'),
        tag('span', 'Curso de Python 3'),
    )