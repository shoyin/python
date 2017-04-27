def count():
    fs = []
    for i in range(1,4):
        def f(x):
            return lambda: x*x
        fs.append(f(i))
    return fs 


count() 


print(count()())