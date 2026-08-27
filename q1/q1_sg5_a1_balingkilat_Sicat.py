class Hero:
    def __init__(self,name,hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self,amount):
        self.hp -= amount
        print(self.name,"took",amount,"damage!" )

arthur = Hero(name="Arthur", hp=100)
morgana = Hero(name="Morgana", hp=100)

arthur.take_damage(10)

print(arthur.name,"has",arthur.hp,"HP")
print(morgana.name,"has",morgana.hp,"HP")

