# Multilevel Inheritance

class Dad:
    chess = True
    pass

class Son(Dad):
    # The previous chess variable has now been overrode into
    # the new chess variable below. So, the previous chess
    # variable will not be used now.
    dance = True
    chess = False

    @staticmethod
    def see():
        print("I don't like chess.")
    pass

class Grandson(Son):
    # The previous dance and chess variables have now been
    # overrode into the dance and chess variables below. So,
    # the previous variables will not be used now.
    dance = False
    chess = True
    cricket = True
    @staticmethod
    # The previous see() method has now been overrode into
    # the new see() method below. So, the previous see()
    # method will not be used now.
    def see():
        print("I like chess and cricket.")
    pass

Harsh = Dad()
Aditya = Son()
Aarav = Grandson()

Aarav.see()
print(Aarav.dance)
print(Aarav.cricket)
print(Aarav.chess)


