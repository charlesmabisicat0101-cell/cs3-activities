class Glassware:
    def __init__(self, capacity_ml: float = 250.0):
        self.capacity_ml = capacity_ml


class Beaker(Glassware):
    pass


class Tray:
    def __init__(self):1
        self.beakers = [Beaker() for _ in range(5)]

if __name__ == "__main__":
    tray = Tray()
    print(f"Tray created with {len(tray.beakers)} beakers.")
    del tray
