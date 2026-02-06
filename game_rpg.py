from abc import ABC, abstractmethod

# =========================
# ABSTRACT CLASS (Latihan 5)
# =========================
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target=None):
        pass

    @abstractmethod
    def info(self):
        pass


# =========================
# CLASS HERO + ENKAPSULASI (Latihan 1–4)
# =========================
class Hero(GameUnit):
    def __init__(self, nama, hp=100, attack_power=10):
        self.nama = nama
        self.__hp = hp
        self.attack_power = attack_power

    # Getter & Setter HP
    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def serang(self, target):
        print(f"{self.nama} menyerang {target.nama}")
        target.diserang(self.attack_power)

    def diserang(self, damage):
        sisa = self.get_hp() - damage
        self.set_hp(sisa)
        print(f"{self.nama} terkena {damage}, sisa HP: {self.get_hp()}")

    def info(self):
        print(f"Hero {self.nama} | HP: {self.get_hp()}")


# =========================
# INHERITANCE (Latihan 3)
# =========================
class Mage(Hero):
    def __init__(self, nama, hp=80, attack_power=30, mana=100):
        super().__init__(nama, hp, attack_power)
        self.mana = mana

    def serang(self, target):
        print(f"{self.nama} (Mage) melempar bola api!")
        target.diserang(self.attack_power * 2)

    def info(self):
        print(f"{self.nama} [Mage] | HP: {self.get_hp()} | Mana: {self.mana}")


class Archer(Hero):
    def serang(self, target):
        print(f"{self.nama} (Archer) memanah!")
        target.diserang(self.attack_power)


class Fighter(Hero):
    def serang(self, target):
        print(f"{self.nama} (Fighter) menebas dengan pedang!")
        target.diserang(self.attack_power)


# =========================
# POLYMORPHISM (Latihan 6)
# =========================
class Healer(Hero):
    def serang(self, target=None):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")


# =========================
# MAIN PROGRAM
# =========================
print("\n--- POLYMORPHISM TEST ---")
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Rafaela")
]

for p in pasukan:
    p.serang(pasukan[0])  # target bebas, tidak mengubah loop
