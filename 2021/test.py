vykon = 1

class Auto():
    def __init__(self, vykon, barva):
        self.param1 = vykon
        self.param2 = barva

    def __init__(self):
        print("vytvořeno")

    def vypisVykon(self):
        param1 = self.param1
        print(param1)
        return "ahoj", "čau"

    def zacud(self):
        print("23456789098765434567898765434567890")
        return

# bavorak = Auto(5, "červená")
#
# bavorak.vypisVykon()


Auto().zacud()