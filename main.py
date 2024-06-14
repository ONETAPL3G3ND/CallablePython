#https://github.com/ONETAPL3G3ND
def test():
    print("Calling")


class Test:
    def __init__(self):
        self.test = "example str"

    def Test(self):
        print("test")


if __name__ == "__main__":
    t = Test()

    print(callable(test))
    for i in vars(t):
        if callable(vars(t).get(i)):
            print(vars(t).get(i))
        else:
            print(vars(t).get(i))

