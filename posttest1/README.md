# Deskripsi Program
Program SYIFA HIJAB adalah program kasir sederhana yang dibuat menggunakan Python. Program ini digunakan untuk mengelola produk, melakukan transaksi penjualan, dan mengelola data pelanggan. Program ini menggunakan konsep Object Oriented Programming, sehingga data dan fungsi dikelompokkan ke dalam beberapa class. Ada tiga class utama yang digunakan, yaitu `Produk`, `Kasir`, dan `Pelanggan`. Program juga memiliki dua jenis pengguna, yaitu admin dan kasir. Beberapa fitur seperti menambah produk, mengubah stok, dan mengubah diskon hanya bisa dilakukan oleh admin.

# Struktur Class
1. Class Produk
Class `Produk` digunakan untuk menyimpan data produk yang dijual di toko.
Beberapa atribut yang digunakan yaitu:
* `nama_produk` untuk menyimpan nama produk.
* `harga` untuk menyimpan harga produk.
* `__stok` untuk menyimpan jumlah stok produk.
* `nama_toko` untuk menyimpan nama toko.
* `total_produk_terdaftar` untuk menghitung jumlah produk yang dibuat.
* `diskon_member` untuk menyimpan diskon member.
Class ini memiliki beberapa method, seperti `tampilkan_info()` untuk menampilkan data produk dan `kurangi_stok()` untuk mengurangi stok ketika terjadi transaksi.
Atribut `__stok` dibuat private sehingga perubahan stok tidak bisa dilakukan secara langsung. Untuk mengatur stok digunakan property dan setter yang juga melakukan pengecekan agar stok tidak boleh negatif.

2. Class Kasir
Class `Kasir` digunakan untuk menyimpan data kasir dan menjalankan proses transaksi.
Atribut yang digunakan antara lain:
* `nama_kasir` untuk nama kasir.
* `shift` untuk menyimpan shift kasir.
* `role` untuk menentukan apakah pengguna merupakan admin atau kasir.
* `__saldo_kas` untuk menyimpan saldo kas.
* `total_transaksi` untuk menghitung jumlah transaksi.
Method `proses_transaksi()` digunakan untuk melakukan transaksi penjualan. Method ini akan memeriksa stok produk, mengurangi stok jika mencukupi, menghitung total harga, dan menambahkan hasil transaksi ke saldo kas. Class `Kasir` juga memiliki method `atur_stok()` dan `atur_diskon()`. Kedua fitur tersebut hanya bisa digunakan jika role pengguna adalah admin.

3. Class Pelanggan
Class `Pelanggan` digunakan untuk menyimpan data pelanggan atau member. Data yang disimpan antara lain nama, jenis member, nomor HP, dan poin. Nomor HP disimpan dalam atribut private `__no_hp`. Saat ditampilkan, nomor HP akan dibuat sebagian menjadi `xxxx` agar tidak ditampilkan secara penuh. Method `tambah_poin()` digunakan untuk menambahkan poin setelah pelanggan melakukan pembelian. Program memberikan 5 poin untuk setiap pembelian.

# Konsep OOP yang Digunakan
Program ini menerapkan beberapa konsep OOP, yaitu:
1. Encapsulation
Encapsulation digunakan pada atribut yang bersifat private, seperti:
__stok
__saldo_kas
__no_hp
Atribut tersebut tidak diakses secara langsung, tetapi melalui property atau method tertentu.

2. Class Attribute
Class attribute digunakan untuk data yang digunakan bersama oleh objek dalam satu class.
Contohnya:
Produk.total_produk_terdaftar
Kasir.total_transaksi
Pelanggan.total_pelanggan

3. Class Method
Class method digunakan pada beberapa fungsi seperti `dari_dict()`, `buat_dari_data()`, dan `ubah_diskon_member()`.

4. Static Method
Static method digunakan untuk fungsi yang tidak bergantung pada objek tertentu, contohnya:
validasi_no_hp()
hitung_total_harga()
validasi_kode_produk()

5. Property dan Setter
Property digunakan untuk mengatur cara mengambil dan mengubah atribut private. Contohnya digunakan pada stok produk, saldo kas, dan nomor HP.

# Alur Program
Saat program dijalankan, pengguna terlebih dahulu melakukan login.
Pengguna memasukkan nama dan memilih role sebagai `admin` atau `kasir`.
Setelah login, akan muncul menu utama:

===== SYIFA HIJAB =====
1. kelola produk
2. transaksi jual
3. kelola pelanggan
4. panel admin
0. keluar
Dari menu tersebut pengguna dapat memilih fitur yang tersedia sesuai dengan role masing-masing.

# Fitur Program
1. Kelola Produk
Menu ini digunakan untuk melihat produk, menambah produk baru, dan mengubah stok. Fitur tambah produk dan ubah stok hanya dapat digunakan oleh admin.
2. Transaksi Jual
Pada menu transaksi, pengguna memilih produk dan memasukkan jumlah pembelian. Jika stok mencukupi, program akan mengurangi stok dan menghitung total harga. Saldo kas dan jumlah transaksi juga akan bertambah. Setelah transaksi selesai, program akan menanyakan apakah pembeli sudah menjadi member. Jika sudah, pelanggan akan mendapatkan poin.
3. Kelola Pelanggan
Menu ini digunakan untuk melihat dan menambahkan data pelanggan. Data pelanggan terdiri dari nama, nomor HP, jenis member, dan poin.
4. Panel Admin
Panel admin digunakan untuk mengubah diskon member dan melihat saldo kas serta jumlah transaksi. Menu ini hanya bisa dibuka oleh pengguna dengan role `admin`.

# Cara Menjalankan Program
Sesuaikan `nama_file.py` dengan nama file program yang digunakan, lalu run saja.

# Panduan Pengujian
1. Pengujian Login Admin
Jalankan program kemudian masukkan nama dan pilih:
login sebagai admin atau kasir? (admin/kasir): admin
Jika berhasil, program akan menampilkan bahwa pengguna login sebagai admin.
Setelah itu coba masuk ke menu kelola produk dan panel admin.
2. Pengujian Login Kasir
Login menggunakan role:
kasir
Kemudian coba masuk ke menu kelola produk dan pilih tambah produk.
Hasil yang diharapkan:
hanya admin yang bisa menambah produk
Hal yang sama juga berlaku ketika kasir mencoba mengubah stok atau membuka panel admin.
3. Pengujian Tambah Produk
Login sebagai admin kemudian pilih:
1. kelola produk
2. tambah produk
Masukkan nama produk, harga, dan stok.
Jika berhasil, program akan menampilkan:
produk berhasil ditambah
4. Pengujian Transaksi
Pastikan sudah ada produk terlebih dahulu.
Pilih:
2. transaksi jual
Kemudian pilih produk dan masukkan jumlah pembelian.
Jika stok mencukupi, transaksi akan berhasil dan stok produk akan berkurang.
5. Pengujian Stok Tidak Cukup
Coba melakukan transaksi dengan jumlah pembelian yang lebih besar dari stok.
Program akan menampilkan pesan bahwa stok tidak cukup dan transaksi tidak akan dilanjutkan.
6. Pengujian Data Pelanggan
Masuk ke:
3. kelola pelanggan
2. tambah pelanggan manual
Masukkan nama, nomor HP, dan jenis member.
Setelah berhasil ditambahkan, data pelanggan dapat dilihat melalui menu lihat pelanggan.
7. Pengujian Poin Member
Lakukan transaksi kemudian pilih `y` ketika program menanyakan apakah pembeli sudah menjadi member.
Masukkan nama member yang sudah terdaftar.
Jika ditemukan, poin pelanggan akan bertambah.
8. Pengujian Input Tidak Valid
Coba masukkan huruf ketika program meminta input angka, misalnya pada harga atau jumlah stok.
Program akan menampilkan:
input harus angka, coba lagi
Program kemudian meminta pengguna memasukkan angka kembali.
9. Pengujian Hak Akses Admin
Login sebagai kasir kemudian coba membuka panel admin.
Hasil yang diharapkan:
akses ditolak, hanya admin
Hal ini menunjukkan bahwa pembatasan hak akses berdasarkan role sudah berjalan.

# Kesimpulan
Program SYIFA HIJAB merupakan program kasir sederhana yang menerapkan konsep OOP dalam Python. Program ini memiliki tiga class utama yaitu `Produk`, `Kasir, dan `Pelanggan`. Dengan program ini, pengguna dapat mengelola produk, melakukan transaksi, mengelola pelanggan, serta mengatur fitur tertentu berdasarkan hak akses admin dan kasir. Konsep OOP seperti encapsulation, class attribute, class method, static method, property, dan setter juga diterapkan dalam program untuk mengatur data dan fungsi agar lebih terstruktur.