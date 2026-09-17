class Glassware:
    def __init__(self, glassware):
        self.glassware = glassware


class Beaker(Glassware):
    def __init__(self, glassware, beaker):
        super().__init__(glassware)
        self.beaker = beaker


class Tray:
    def __init__(self, tray):
        self.tray = tray
        self.container = [Beaker("Glassware", f"Glass Beaker{i}") for i in range (1, 6)]

Ray_Tray = Tray("Ray_Tray")

for Glass_Beaker in Ray_Tray.container:
    print(Glass_Beaker.beaker)
    print()
