def greet(**kwargs):
    if kwargs is not None:
        for k, v in kwargs.items():
            print("%s == %s" %(k, v))

greet(name="Davis")
