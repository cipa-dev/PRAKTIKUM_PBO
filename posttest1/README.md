# deskripsi program
program ini digunakan untuk mengelola data produk, melakukan transaksi penjualan, serta mengelola data pelanggan pada toko hijab. program ini menerapkan konsep object oriented programming, sehingga data dan fungsi dikelompokkan ke dalam beberapa class. Terdapat tiga class utama yang digunakan, yaitu `Produk`, `Kasir`, dan `Pelanggan`. program dijalankan secara interaktif melalui terminal menggunakan `input()`, sehingga pengguna dapat langsung memasukkan data dan mencoba setiap fitur yang tersedia.

# struktur class
1. class Produk
class `Produk` digunakan untuk menyimpan data produk yang dijual di toko.
atribut yang digunakan antara lain:
- `nama_produk` untuk menyimpan nama produk
- `harga` untuk menyimpan harga produk
- `__stok` untuk menyimpan jumlah stok produk
- `nama_toko` untuk menyimpan nama toko
- `total_produk_terdaftar` untuk menghitung jumlah produk yang telah dibuat
- `satuan` untuk menyimpan satuan produk (pcs)
method `tampilkan_info()` digunakan untuk menampilkan data produk, sedangkan `kurangi_stok()` digunakan untuk mengurangi stok saat terjadi transaksi. atribut `__stok` bersifat private sehingga tidak bisa diubah secara langsung. perubahan stok hanya dapat dilakukan melalui property `stok`, yang juga melakukan validasi agar stok tidak diisi angka negatif atau bukan bilangan bulat.

2. class Kasir
class `Kasir` digunakan untuk menyimpan data kasir dan menjalankan proses transaksi
atribut yang digunakan:
- `nama_kasir` untuk menyimpan nama kasir
- `shift` untuk menyimpan shift kerja kasir
- `__saldo_kas` untuk menyimpan saldo hasil transaksi
- `total_transaksi` untuk menghitung jumlah transaksi yang terjadi
- `pajak` sebagai atribut konfigurasi umum
method `proses_transaksi()` digunakan untuk melakukan transaksi penjualan. method ini memeriksa stok produk, mengurangi stok jika mencukupi, menghitung total harga, lalu menambahkan hasilnya ke saldo kas. class ini juga memiliki method `atur_stok()` untuk memperbarui stok produk.

3. class pelanggan
class `Pelanggan` digunakan untuk menyimpan data member toko. Data yang disimpan meliputi nama, nomor HP, dan poin. nomor HP disimpan pada atribut private `__no_hp` dan hanya bisa diubah melalui property yang memvalidasi format nomor (harus diawali angka 08 dan minimal 10 digit). jika format tidak sesuai, perubahan akan ditolak melalui `raise ValueError`. saat ditampilkan, sebagian nomor HP disamarkan menjadi `xxxx` agar tidak terlihat secara penuh. Method `tambah_poin()` digunakan untuk menambahkan poin setiap kali pelanggan melakukan pembelian, dengan nilai poin diatur pada atribut kelas `poin_per_pembelian`.

# konsep OOP yang digunakan
1. encapsulation: diterapkan pada atribut private `__stok`, `__saldo_kas`, dan `__no_hp`, yang hanya bisa diakses atau diubah melalui property dan method tertentu.
2. class attribute: digunakan untuk data yang dipakai bersama oleh seluruh objek, contohnya `Produk.total_produk_terdaftar`, `Kasir.total_transaksi`, dan `Pelanggan.total_pelanggan`.
3. class method: digunakan pada `dari_dict()` (Produk) dan `buat_dari_data()` (Kasir) sebagai factory method untuk membuat objek dari data dictionary.
4. static method: digunakan pada `hitung_total_harga()` (Kasir) dan `validasi_no_hp()` (Pelanggan), yaitu fungsi bantuan yang tidak bergantung pada objek tertentu.
5. property dan setter: digunakan untuk mengatur cara mengambil dan mengubah atribut private, contohnya pada `stok`, `saldo_kas`, dan `no_hp`.

# Alur Program
Saat program dijalankan, pengguna terlebih dahulu login dengan memasukkan nama. Setelah itu, akan muncul menu utama:
----- SYIFA HIJAB -----
1. lihat produk
2. tambah produk
3. ubah stok
4. transaksi jual
5. lihat pelanggan
6. tambah pelanggan
7. lihat saldo kas & total transaksi
0. keluar

# Fitur Program
1. Lihat & Tambah Produk: menampilkan daftar produk yang tersedia, atau menambahkan produk baru dengan memasukkan nama, harga, dan stok awal.
2. Ubah Stok: memperbarui jumlah stok produk yang sudah ada.
3. Transaksi Jual: memilih produk dan jumlah pembelian. Jika stok mencukupi, stok akan berkurang dan saldo kas bertambah. Setelah transaksi, program akan menanyakan apakah pembeli sudah menjadi member untuk menambahkan poin.
4. Lihat & Tambah Pelanggan: menampilkan daftar pelanggan atau mendaftarkan pelanggan baru dengan nama dan nomor HP.
5. Lihat Saldo Kas & Total Transaksi: menampilkan saldo kas kasir yang sedang login beserta jumlah transaksi keseluruhan.

# cara menjalankan program
tinggal run aja di terminal

# Panduan Pengujian
1. Pengujian Tambah Produk
Pilih menu `2. tambah produk`, lalu masukkan nama, harga, dan stok. Jika berhasil, program akan menampilkan pesan `produk berhasil ditambah`.
2. Pengujian Transaksi
Pastikan produk sudah tersedia, lalu pilih menu `4. transaksi jual`. Pilih produk dan masukkan jumlah pembelian sesuai stok yang ada. Jika berhasil, stok produk akan berkurang dan saldo kas bertambah.
3. Pengujian Stok Tidak Cukup
Lakukan transaksi dengan jumlah pembelian melebihi stok yang tersedia. Program akan menampilkan pesan bahwa stok tidak cukup dan transaksi tidak dilanjutkan.
4. Pengujian Setter Stok (Valid dan Tidak Valid)
Pilih menu `3. ubah stok`, lalu coba masukkan angka positif (valid) dan angka negatif (tidak valid). Untuk input tidak valid, program akan menampilkan pesan penolakan dan stok tidak berubah.
5. Pengujian Poin Member
Setelah melakukan transaksi, pilih `y` saat ditanya apakah pembeli sudah menjadi member, lalu masukkan nama member yang terdaftar. Jika ditemukan, poin pelanggan akan bertambah.
6. Pengujian Setter Nomor HP (Valid dan Tidak Valid)
Pilih menu `6. tambah pelanggan`, lalu coba masukkan nomor HP dengan format salah (misalnya tidak diawali 08). Program akan menolak dan meminta input ulang hingga nomor yang dimasukkan valid.
7. Pengujian Input Tidak Valid
Coba masukkan huruf saat program meminta input angka, misalnya pada harga atau stok. Program akan menampilkan pesan `input harus angka, coba lagi` dan meminta input kembali.