import os
from abc import ABC, abstractmethod
class AkunPoint:
    def __init__(self):
        self.total_poin = 0
    def tambah(self, poin):
        self.total_poin += poin

class Produk(ABC):
    def __init__(self, nama_produk, harga, stok):
        self.nama_produk = nama_produk
        self.harga = harga
        self.__stok = stok
        self.kategori = "Umum"

    @abstractmethod
    def hitung_diskon(self):
        pass

    @abstractmethod
    def deskripsi(self):
        pass
    def get_stok(self):
        return self.__stok
    def set_stok(self, stok_baru):
        if stok_baru >= 0:
            self.__stok = stok_baru
            return True
        print("Stok tidak boleh minus!")
        return False
    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah beli harus lebih dari 0!")
            return False
        if jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        print(f"Stok '{self.nama_produk}' tidak cukup!")
        return False
    def __str__(self):
        return f"{self.nama_produk} - Rp{self.harga:,.0f}"

class Hijab(Produk):
    def __init__(self, nama_produk, harga, stok, bahan="Tidak disebutkan"):
        super().__init__(nama_produk, harga, stok)
        self.kategori = "Hijab"
        self.bahan = bahan
    def hitung_diskon(self):
        return self.harga * 0.10
    def deskripsi(self):
        return f"Kategori Hijab, bahan {self.bahan}"

class Aksesoris(Produk):
    def __init__(self, nama_produk, harga, stok, jenis="Umum"):
        super().__init__(nama_produk, harga, stok)
        self.kategori = "Aksesoris"
        self.jenis = jenis
    def hitung_diskon(self):
        return self.harga * 0.05
    def deskripsi(self):
        return f"Kategori Aksesoris, jenis {self.jenis}"

class LaporanCetak:
    def cetak_bukti(self, pesan):
        print("\n=== BUKTI TRANSAKSI ===")
        print(pesan)
        print("=======================")

class LaporanDigital:
    def cetak_bukti(self, pesan):
        print("\n=== BUKTI TRANSAKSI DIGITAL ===")
        print(pesan)
        print("Bukti disiapkan dalam format digital.")
        print("===============================")
def kirim_laporan(media, pesan):
    media.cetak_bukti(pesan)

class Toko:
    def __init__(self, nama):
        self.nama = nama
        
        self.katalog_produk = []
    def tambah_produk(self, produk):
        self.katalog_produk.append(produk)
        
    def lihat_katalog(self):
        if not self.katalog_produk:
            print("Katalog produk masih kosong.")
            return False
        print("\n" + "=" * 78)
        print(f"KATALOG PRODUK {self.nama.upper()}")
        print("=" * 78)
        print(
            f"{'No':<4} {'Kategori':<12} {'Nama Produk':<22} "
            f"{'Harga':>12} {'Stok':>6} {'Diskon':>10}"
        )
        print("-" * 78)
        for i, produk in enumerate(self.katalog_produk, start=1):
            print(
                f"{i:<4} {produk.kategori:<12} "
                f"{produk.nama_produk:<22} "
                f"Rp{produk.harga:>9,.0f} "
                f"{produk.get_stok():>6} "
                f"Rp{produk.hitung_diskon():>7,.0f}"
            )
        print("=" * 78)
        return True

class Kasir:
    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir
        self.saldo_kas = 0
    def proses_transaksi(self, produk, jumlah):
        if jumlah <= 0:
            print("Jumlah beli harus lebih dari 0!")
            return False
        if not produk.kurangi_stok(jumlah):
            return False
        total_bayar = produk.harga * jumlah
        self.saldo_kas += total_bayar
        print(
            f"\nPenjualan berhasil: {jumlah} x "
            f"{produk.nama_produk} = Rp{total_bayar:,.0f}"
        )
        pilihan_bukti = input(
            "Jenis bukti transaksi (1. Cetak / 2. Digital / 0. Lewati): "
        ).strip()
        pesan = (
            f"Kasir: {self.nama_kasir}\n"
            f"Produk: {produk.nama_produk}\n"
            f"Jumlah: {jumlah}\n"
            f"Total: Rp{total_bayar:,.0f}"
        )
        if pilihan_bukti == "1":
            kirim_laporan(LaporanCetak(), pesan)
        elif pilihan_bukti == "2":
            kirim_laporan(LaporanDigital(), pesan)
        elif pilihan_bukti != "0":
            print("Pilihan bukti tidak valid. Transaksi tetap berhasil.")
        return True
    def atur_stok(self, produk, stok_baru):
        if produk.set_stok(stok_baru):
            print(
                f"Stok '{produk.nama_produk}' berhasil diubah "
                f"menjadi {produk.get_stok()}."
            )
    def bantu_pelanggan_member(self, pelanggan):
        print(
            f"Kasir {self.nama_kasir} menambah poin "
            f"member {pelanggan.nama}."
        )
        pelanggan.tambah_poin()

class Pelanggan:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.akun_poin = AkunPoint()
    def tambah_poin(self):
        self.akun_poin.tambah(5)
        print(
            f"{self.nama} mendapat 5 poin. "
            f"Total poin: {self.akun_poin.total_poin}"
        )
    def tampilkan_data(self):
        print(
            f"Nama: {self.nama:<20} | "
            f"HP: {self.no_hp:<15} | "
            f"Poin: {self.akun_poin.total_poin}"
        )

toko_syifa = Toko("Syifa Hijab")
daftar_pelanggan = []
kasir_aktif = None

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def pause():
    input("\nTekan Enter untuk lanjut...")
def input_angka(pesan, minimal=0):
    while True:
        nilai = input(pesan).strip()
        try:
            angka = int(nilai)
            if angka < minimal:
                print(f"Masukkan angka minimal {minimal}.")
                continue
            return angka
        except ValueError:
            print("Input harus berupa angka.")
def input_nama(pesan):
    while True:
        nama = input(pesan).strip()
        if nama and any(huruf.isalpha() for huruf in nama):
            return nama
        print("Nama tidak boleh kosong.")
def input_hp():
    while True:
        no_hp = input(
            "No HP (minimal 12 digit, diawali 08): "
        ).strip()
        if (
            no_hp.isdigit()
            and no_hp.startswith("08")
            and len(no_hp) >= 12
        ):
            return no_hp
        print("Nomor HP tidak valid.")
def cari_pelanggan(nama):
    for pelanggan in daftar_pelanggan:
        if pelanggan.nama.lower() == nama.lower():
            return pelanggan
    return None
def login():
    global kasir_aktif
    clear_screen()
    print("=== LOGIN KASIR ===")
    nama = input_nama("Masukkan nama kasir: ")
    kasir_aktif = Kasir(nama)
    print(f"Selamat bertugas, {kasir_aktif.nama_kasir}!")
    pause()
def menu_tambah_produk():
    print("\nPilih Kategori:")
    print("1. Hijab")
    print("2. Aksesoris")
    pilihan = input("Pilihan (1/2): ").strip()
    if pilihan not in ("1", "2"):
        print("Pilihan kategori tidak valid.")
        return
    nama = input_nama("Nama produk: ")
    harga = input_angka("Harga: Rp", 1)
    stok = input_angka("Stok awal: ", 0)
    if pilihan == "1":
        bahan = input_nama("Bahan hijab: ")
        produk_baru = Hijab(nama, harga, stok, bahan)
    else:
        jenis = input_nama("Jenis aksesoris: ")
        produk_baru = Aksesoris(nama, harga, stok, jenis)
    toko_syifa.tambah_produk(produk_baru)
    print("Produk berhasil ditambahkan.")
def menu_ubah_stok():
    if not toko_syifa.lihat_katalog():
        return
    indeks = input_angka("Pilih nomor produk: ", 1)
    if indeks > len(toko_syifa.katalog_produk):
        print("Nomor produk tidak ditemukan.")
        return
    stok_baru = input_angka("Masukkan stok baru: ", 0)
    kasir_aktif.atur_stok(
        toko_syifa.katalog_produk[indeks - 1],
        stok_baru
    )
def menu_transaksi():
    if not toko_syifa.lihat_katalog():
        return
    indeks = input_angka("Pilih nomor produk: ", 1)
    if indeks > len(toko_syifa.katalog_produk):
        print("Nomor produk tidak ditemukan.")
        return
    produk = toko_syifa.katalog_produk[indeks - 1]
    jumlah = input_angka("Jumlah beli: ", 1)
    if kasir_aktif.proses_transaksi(produk, jumlah):
        is_member = input(
            "Apakah pelanggan member? (y/n): "
        ).strip().lower()
        if is_member == "y":
            nama_member = input_nama("Nama member: ")
            pelanggan = cari_pelanggan(nama_member)
            if pelanggan:
                kasir_aktif.bantu_pelanggan_member(pelanggan)
            else:
                print("Member tidak ditemukan.")
        elif is_member == "n":
            daftar = input("Mau daftar member? (y/n): ").strip().lower()
            if daftar == "y":
                nama = input_nama("Nama: ")
                no_hp = input_hp()
                pelanggan_baru = Pelanggan(nama, no_hp)
                daftar_pelanggan.append(pelanggan_baru)
                kasir_aktif.bantu_pelanggan_member(pelanggan_baru)
def menu_lihat_pelanggan():
    if not daftar_pelanggan:
        print("Belum ada data pelanggan.")
        return
    print("\n=== DAFTAR MEMBER ===")
    for pelanggan in daftar_pelanggan:
        pelanggan.tampilkan_data()
def menu_tambah_pelanggan():
    nama = input_nama("Nama pelanggan: ")
    no_hp = input_hp()
    daftar_pelanggan.append(Pelanggan(nama, no_hp))
    print("Pelanggan berhasil ditambahkan.")
def menu_saldo_kas():
    print(f"Saldo kas: Rp{kasir_aktif.saldo_kas:,.0f}")
def menu_utama():
    while True:
        clear_screen()
        print(f"=== MENU UTAMA ({kasir_aktif.nama_kasir}) ===")
        print("1. Lihat Katalog Produk")
        print("2. Tambah Produk")
        print("3. Ubah Stok")
        print("4. Transaksi Penjualan")
        print("5. Lihat Daftar Member")
        print("6. Tambah Member Baru")
        print("7. Lihat Saldo Kas")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            toko_syifa.lihat_katalog()
        elif pilihan == "2":
            menu_tambah_produk()
        elif pilihan == "3":
            menu_ubah_stok()
        elif pilihan == "4":
            menu_transaksi()
        elif pilihan == "5":
            menu_lihat_pelanggan()
        elif pilihan == "6":
            menu_tambah_pelanggan()
        elif pilihan == "7":
            menu_saldo_kas()
        elif pilihan == "0":
            print("Selesai. Terima kasih!")
            break
        else:
            print("Pilihan menu salah.")
        pause()
def uji_konsep_pbo():
    print("=== BUKTI ABSTRAKSI ===")
    try:
        Produk("Contoh", 10000, 1)
    except TypeError as error:
        print("Produk tidak bisa diinstansiasi karena bersifat abstract.")
        print(f"Bukti: {error}")
    print("\n=== PENGUJIAN POLIMORFISME ===")
    produk_uji = [
        Hijab("Pashmina", 50000, 5, "Voal"),
        Aksesoris("Bros Dagu", 15000, 10, "Bros")
    ]
    for produk in produk_uji:
        print(produk)
        print(produk.deskripsi())
        print(f"Diskon: Rp{produk.hitung_diskon():,.0f}")
    print("\n=== PENGUJIAN DUCK TYPING ===")
    pesan = "Transaksi contoh: Rp50.000"
    kirim_laporan(LaporanCetak(), pesan)
    kirim_laporan(LaporanDigital(), pesan)
if __name__ == "__main__":
    toko_syifa.tambah_produk(
        Hijab("Pashmina", 50000, 10, "Voal")
    )
    toko_syifa.tambah_produk(
        Aksesoris("Bros Dagu", 15000, 20, "Bros")
    )
    login()
    menu_utama()