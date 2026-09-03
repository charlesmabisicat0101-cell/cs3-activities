
class Lab:
    def __init__(self, room_number):
        self.room_number = room_number

class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None  


chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")

mr_cruz.assigned_lab = chem_lab

print(f"Technician {mr_cruz.name} is assigned to Room {mr_cruz.assigned_lab.room_number}.")
