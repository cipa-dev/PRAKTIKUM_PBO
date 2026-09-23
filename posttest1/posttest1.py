import os
class Produk:
    nama_toko = "SYIFA HIJAB"
    total_produk_terdaftar = 0
    satuan = "pcs"
    def __init__(self, nama_produk, harga, stok):
        self.nama_produk = nama_produk      # atribut public
        self.harga = harga                  # atribut public
        self.__stok = stok                  # atribut private
        Produk.total_produk_terdaftar += 1

    @property
    def stok(self):
        return self.__stok
    @stok.setter
    def stok(self, nilai_baru):
        if not isinstance(nilai_baru, int):
            print("stok harus berupa angka bulat")
            return
        if nilai_baru < 0:
            print(f"gagal update stok '{self.nama_produk}': jumlah tidak boleh minus")
            return
        self.__stok = nilai_baru
    def tampilkan_info(self):
        print(f"[{self.nama_toko}] {self.nama_produk} | harga: Rp{self.harga:,} | stok: {self.__stok} {self.satuan}")
    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        else:
            print(f"stok '{self.nama_produk}' tidak cukup, sisa stok: {self.__stok}")
            return False

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["harga"], data["stok"])

class Kasir:
    nama_toko = "SYIFA HIJAB"
    total_transaksi = 0
    pajak = 0.0
    def __init__(self, nama_kasir, shift):
        self.nama_kasir = nama_kasir   # public
        self.shift = shift             # public
        self.__saldo_kas = 0           # private

    @property
    def saldo_kas(self):
        return self.__saldo_kas
    @saldo_kas.setter
    def saldo_kas(self, nilai):
        if nilai < 0:
            print("saldo tidak boleh negatif, transaksi dibatalkan")
            return
        self.__saldo_kas = nilai
    def proses_transaksi(self, produk: Produk, jumlah):
        if jumlah <= 0:
            print("jumlah tidak valid")
            return False
        berhasil = produk.kurangi_stok(jumlah)
        if berhasil:
            total_bayar = Kasir.hitung_total_harga(produk.harga, jumlah)
            self.__saldo_kas += total_bayar
            Kasir.total_transaksi += 1
            print(f"kasir {self.nama_kasir} berhasil jual {jumlah}x {produk.nama_produk} = Rp{total_bayar:,}")
            return True
        else:
            print("transaksi gagal, stok tidak cukup")
            return False
    def atur_stok(self, produk: Produk, stok_baru):
        produk.stok = stok_baru
        print(f"{self.nama_kasir} ubah stok '{produk.nama_produk}' jadi {produk.stok}")

    @classmethod
    def buat_dari_data(cls, data):
        return cls(data["nama"], data["shift"])

    @staticmethod
    def hitung_total_harga(harga, jumlah):
        return harga * jumlah

class Pelanggan:
    total_pelanggan = 0
    poin_per_pembelian = 5
    nama_program = "Member SYIFA HIJAB"
    def __init__(self, nama, no_hp):
        self.nama = nama            # public
        self.poin = 0                # public
        self.__no_hp = None          # private
        self.no_hp = no_hp           # lewat setter, kalau invalid raise error
        Pelanggan.total_pelanggan += 1

    @property
    def no_hp(self):
        return self.__no_hp[:4] + "xxxx" + self.__no_hp[-2:]
    @no_hp.setter
    def no_hp(self, nomor):
        if not Pelanggan.validasi_no_hp(nomor):
            raise ValueError(f"nomor HP '{nomor}' tidak valid, harus diawali 08 dan berisi angka minimal 10 digit")
        self.__no_hp = nomor
    def tambah_poin(self):
        self.poin += Pelanggan.poin_per_pembelian
        print(f"{self.nama} dapat tambahan {Pelanggan.poin_per_pembelian} poin, total poin: {self.poin}")
    def tampilkan_data(self):
        print(f"[{self.nama_program}] Nama: {self.nama} | HP: {self.no_hp} | Poin: {self.poin}")

    @staticmethod
    def validasi_no_hp(no_hp):
        return no_hp.isdigit() and no_hp.startswith("08") and len(no_hp) >= 10

daftar_produk = []
daftar_pelanggan = []
kasir_aktif = None

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def pause():
    input("\ntekan enter untuk lanjut...")
def input_angka(teks, boleh_desimal=False):
    while True:
        nilai = input(teks)
        try:
            return float(nilai) if boleh_desimal else int(nilai)
        except ValueError:
            print("input harus angka, coba lagi")
def input_no_hp(teks="no hp (diawali 08, minimal 10 digit angka): "):
    while True:
        nomor = input(teks)
        if Pelanggan.validasi_no_hp(nomor):
            return nomor
        print("nomor gak valid, coba lagi")
def cari_pelanggan(nama):
    for p in daftar_pelanggan:
        if p.nama.lower() == nama.lower():
            return p
    return None
def login():
    global kasir_aktif
    clear_screen()
    print("--- LOGIN KASIR SYIFA HIJAB ---")
    nama = input("nama kamu: ")
    kasir_aktif = Kasir.buat_dari_data({"nama": nama, "shift": "harian"})
    print(f"\nhalo {kasir_aktif.nama_kasir}, selamat kerja!")
    pause()
def menu_lihat_produk():
    if not daftar_produk:
        print("belum ada produk")
        return
    print("\n-- daftar produk --")
    for i, p in enumerate(daftar_produk, start=1):
        print(f"{i}. ", end="")
        p.tampilkan_info()
def menu_tambah_produk():
    nama = input("nama produk: ")
    harga = input_angka("harga: ")
    stok = input_angka("stok awal: ")
    produk_baru = Produk.dari_dict({"nama": nama, "harga": harga, "stok": stok})
    daftar_produk.append(produk_baru)
    print("produk berhasil ditambah")
def menu_ubah_stok():
    menu_lihat_produk()
    if not daftar_produk:
        return
    idx = input_angka("pilih nomor produk: ")
    if 1 <= idx <= len(daftar_produk):
        stok_baru = input_angka("stok baru: ")
        kasir_aktif.atur_stok(daftar_produk[idx - 1], stok_baru)
    else:
        print("nomor produk tidak ada")
def menu_transaksi():
    clear_screen()
    print("--- TRANSAKSI JUAL ---")
    menu_lihat_produk()
    if not daftar_produk:
        return
    idx = input_angka("pilih nomor produk: ")
    if not (1 <= idx <= len(daftar_produk)):
        print("nomor produk tidak ada")
        return
    produk = daftar_produk[idx - 1]
    jumlah = input_angka("jumlah beli: ")
    berhasil = kasir_aktif.proses_transaksi(produk, jumlah)
    if not berhasil:
        return
    sudah_member = input("pembeli sudah jadi member? (y/n): ").strip().lower()
    if sudah_member == "y":
        nama_cari = input("nama member: ")
        pelanggan = cari_pelanggan(nama_cari)
        if pelanggan:
            pelanggan.tambah_poin()
        else:
            print("nama tidak terdaftar sebagai member")
    else:
        mau_daftar = input("mau daftar member sekalian? (y/n): ").strip().lower()
        if mau_daftar == "y":
            nama = input("nama: ")
            no_hp = input_no_hp()
            pelanggan_baru = Pelanggan(nama, no_hp)
            daftar_pelanggan.append(pelanggan_baru)
            pelanggan_baru.tambah_poin()
def menu_lihat_pelanggan():
    if not daftar_pelanggan:
        print("belum ada pelanggan")
        return
    print("\n-- daftar pelanggan --")
    for p in daftar_pelanggan:
        p.tampilkan_data()
def menu_tambah_pelanggan():
    nama = input("nama pelanggan: ")
    no_hp = input_no_hp()
    daftar_pelanggan.append(Pelanggan(nama, no_hp))
    print("pelanggan berhasil ditambah")
def menu_saldo():
    print(f"saldo kas {kasir_aktif.nama_kasir}: Rp{kasir_aktif.saldo_kas:,}")
    print(f"total transaksi semua kasir: {Kasir.total_transaksi}")
def tampilkan_menu():
    print(f"--- SYIFA HIJAB ({kasir_aktif.nama_kasir}) ---")
    print("1. lihat produk")
    print("2. tambah produk")
    print("3. ubah stok")
    print("4. transaksi jual")
    print("5. lihat pelanggan")
    print("6. tambah pelanggan")
    print("7. lihat saldo kas & total transaksi")
    print("0. keluar")

if __name__ == "__main__":
    login()
    while True:
        clear_screen()
        tampilkan_menu()
        pilihan = input("pilih menu: ")
        print()
        if pilihan == "1":
            menu_lihat_produk()
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
            menu_saldo()
        elif pilihan == "0":
            print("terima kasih sudah belanja di SYIFA HIJAB")
            break
        else:
            print("menu tidak valid, coba lagi")
        if pilihan != "0":
            pause()