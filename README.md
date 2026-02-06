
<img width="555" height="479" alt="Screenshot 2026-02-06 191942" src="https://github.com/user-attachments/assets/f695d2b1-0be3-45d1-97f1-b82dcf8b65ed" />
 <img width="462" height="253" alt="Screenshot 2026-02-06 192009" src="https://github.com/user-attachments/assets/7d99e7d2-9d2d-45c6-8948-4ed5f71c9c52" />
 Analisis Konsep OOP (Object-Oriented Programming)

Dokumen ini berisi ringkasan analisis penerapan konsep OOP dalam Python, meliputi atribut objek, interaksi antar objek, inheritance, enkapsulasi, abstract class, dan polimorfisme.

---

##  Analisis 1: Perubahan Atribut Objek

### Penjelasan
Atribut pada sebuah objek dapat diubah setelah objek dibuat. Perubahan tersebut hanya berlaku pada objek yang dimodifikasi dan tidak memengaruhi objek lain.

### Kesimpulan
- Atribut objek di Python bersifat dinamis.
- Perubahan atribut hanya berdampak pada objek terkait.
- Constructor (`__init__`) hanya memberi nilai awal, bukan nilai permanen.

---

##  Analisis 2: Method Menerima Objek sebagai Parameter

### Penjelasan
Method sebaiknya menerima **objek utuh**, bukan sekadar string atau data sederhana, agar dapat:
- Mengakses atribut objek lain
- Memanggil method milik objek lain
- Mengubah kondisi objek lain secara langsung

### Kesimpulan
- Interaksi dalam OOP terjadi antar objek.
- Menggunakan objek sebagai parameter membuat program lebih realistis dan terstruktur.

---

##  Analisis 3: Fungsi `super()` pada Inheritance

### Masalah
Menghapus `super().__init__()` pada class turunan menyebabkan atribut milik parent tidak terbentuk.

### Dampak
- Object child tidak memiliki atribut dasar dari parent
- Method parent yang mengakses atribut tersebut akan error

### Peran `super()`
- Memanggil constructor class induk
- Menjaga agar atribut parent tetap dimiliki child
- Membuat inheritance berjalan sempurna

### Kesimpulan
- `super()` adalah penghubung penting antara class child dan parent.
- Tanpa `super()`, inheritance menjadi tidak lengkap.

---

##  Analisis 4: Enkapsulasi dan Keamanan Data

### 1. Name Mangling
Atribut private (`__atribut`) masih bisa diakses dengan cara khusus (`_Class__atribut`), namun:
- Tidak dianjurkan
- Melanggar prinsip enkapsulasi
- Dianggap praktik tidak profesional

### 2. Validasi Setter
Tanpa validasi pada setter:
- Data bisa menjadi tidak logis (contoh: HP negatif)
- Perlindungan data menjadi sia-sia

### Kesimpulan
- Enkapsulasi menjaga konsistensi dan keamanan data
- Setter berfungsi sebagai gerbang kontrol data
- Validasi sangat penting dalam pemrograman yang baik

---

##  Analisis 5: Abstract Class

### 1. Melanggar Kontrak Abstract Method
Jika class turunan tidak mengimplementasikan method abstract:
- Object tidak bisa dibuat
- Program akan error

### 2. Instansiasi Abstract Class
Abstract class:
- Hanya berfungsi sebagai blueprint
- Tidak boleh diinstansiasi langsung

### Kesimpulan
- Abstract class memaksa standar method pada class turunan
- Menjamin konsistensi struktur program

---

##  Analisis 6: Polimorfisme

### 1. Skalabilitas Program
Menambah class baru (contoh: Healer) tidak memerlukan perubahan kode lama selama mengikuti interface yang sama.

### 2. Konsistensi Nama Method
Jika nama method berbeda:
- Program akan error saat dipanggil secara polimorfik

### Kesimpulan
- Polimorfisme membuat program fleksibel dan mudah dikembangkan
- Konsistensi nama method adalah kunci

---

##  Kesimpulan Akhir (Super Singkat)

- Atribut objek bisa diubah setelah dibuat
- Method sebaiknya menerima objek, bukan data sederhana
- `super()` menghubungkan child dengan parent
- Enkapsulasi menjaga data tetap aman dan valid
- Abstract class menetapkan standar method
- Polimorfisme membuat program scalable dan rapi

---

 **Dokumen ini cocok digunakan sebagai laporan praktikum, README proyek, atau catatan belajar OOP.**

