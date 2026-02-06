from abc import ABC, abstractmethod

# =========================
# ABSTRACT CLASS
# =========================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    # ENCAPSULATION
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# =========================
# LAPTOP
# =========================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        pajak = int(self.get_harga_dasar() * 0.10)
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {pajak:,}")

    def hitung_harga_total(self, jumlah):
        return (self.get_harga_dasar() * 1.10) * jumlah


# =========================
# SMARTPHONE
# =========================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        pajak = int(self.get_harga_dasar() * 0.05)
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {pajak:,}")

    def hitung_harga_total(self, jumlah):
        return (self.get_harga_dasar() * 1.05) * jumlah


# =========================
# TRANSAKSI
# =========================
def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0

    for i, item in enumerate(daftar_barang, start=1):
        barang = item["barang"]
        jumlah = item["jumlah"]

        print(f"{i}. ", end="")
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")

        total += subtotal

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")
    print("----------------------------------------")


# =========================
# MAIN PROGRAM
# =========================
print("--- SETUP DATA ---")

laptop = Laptop("MacBook Pro M2", 25_000_000, "Apple M2")
smartphone = Smartphone("Samsung Galaxy S23", 18_000_000, "50MP")

laptop.tambah_stok(5)
smartphone.tambah_stok(15)

keranjang = [
    {"barang": laptop, "jumlah": 1},
    {"barang": smartphone, "jumlah": 2},
]

proses_transaksi(keranjang)
