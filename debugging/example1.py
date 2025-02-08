import string

metaslash = 1


def printNames():
    neal = 'neal'
    michelle = 'michele'
    eric = 5
    print("Local values: %(neal)S %(michele)s %(eric)" % locals())


class Nothing:
    def printValue(value):
        print(value)

    def set(self, value):
        self.value = value


def tryToDoSomething(self, value):
    try:
        import string
        if not value:
            raise (RuntimeError, "Hey, there's no value")
        printNames('a, b, c')
    except:
        traceback.print_exc()


def setGlobal(value=None):
    metaslash = value
    print('Old MetaSlash value is:', metaslash)
    useless = Nothing(5)
    print('a useless value is:', useless.valeu)

setGlobal(50)


def main():
    print("==========")
    print("Starting the program")
    print("==========")

    setGlobal(50)

    print("\n==========")
    print("Trying to do something with no value:")
    tryToDoSomething(None, "")

    print("\n==========")
    print("Trying to do something with a value:")
    tryToDoSomething(None, "some value")

    print("\n==========")
    print("Printing a value using the Nothing class:")
    useless = Nothing()
    useless.printValue(10)

    print("==========")
    print("Ending the program")
    print("==========")


if __name__ == "__main__":
    main()
