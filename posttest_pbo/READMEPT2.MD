1. Implementasi Relasi UML
A. Komposisi
Kelas yang terlibat: Pelanggan dan AkunPoint
Penjelasan: Objek AkunPoint diinstansiasi langsung di dalam kelas Pelanggan melalui atribut self.akun_poin = AkunPoint(). Hubungan ini bersifat kompositional karena data poin melekat secara utuh pada objek pelanggan dan tidak bisa berdiri sendiri tanpa adanya objek pelanggan tersebut.
B. Agregasi
Kelas yang terlibat: Toko dan Produk
Penjelasan: Kelas Toko menyimpan daftar objek Produk ke dalam list self.katalog_produk. Hubungan ini berupa agregasi karena objek Produk dibuat secara terpisah di luar kelas Toko sebelum dimasukkan ke dalam daftar katalog.
C. Asosiasi
Kelas yang terlibat: Kasir dan Pelanggan
Penjelasan: Hubungan asosiasi terjadi saat kelas Kasir memanggil fungsi pada objek Pelanggan melalui method bantu_pelanggan_member(pelanggan). Kedua kelas saling berinteraksi saat proses penambahan poin member, tetapi masing-masing objek tetap berdiri sendiri.

2. Implementasi Inheritance
Penerapan inheritance dilakukan untuk mengelompokkan produk berdasarkan jenisnya agar struktur kode lebih rapi dan dapat digunakan kembali (reusable).
-Superclass = Produk
Menjadi kelas induk yang menyimpan atribut umum dari seluruh produk, yaitu nama_produk, harga, dan __stok dibuat private untuk enkapsulasi.
-Subclass = Hijab dan Aksesoris
Menjadi kelas turunan dari Produk. Kedua kelas ini menggunakan fungsi super().__init__() untuk mengambil atribut dari kelas induk, sekaligus menetapkan atribut kategori secara otomatis sesuai jenis produknya.