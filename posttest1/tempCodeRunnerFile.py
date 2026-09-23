import os
class Produk:
    nama_toko = "SYIFA HIJAB"
    total_produk_terdaftar = 0
    diskon_member = 0.1  # diskon 10% untuk member
    def __init__(self, nama_produk, harga, stok):
        self.nama_produk = nama_produk      # atribut public
        self.harga = harga                  # atribut public
        self.__stok = stok                  # atribut private
        Produk.total_produk_terdaftar += 1  # increment total produk

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
        print(f"[{self.nama_toko}] {self.nama_produk} | harga: Rp{self.harga:,} | stok: {self.__stok}")
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
    @classmethod
    def ubah_diskon_member(cls, diskon_baru):
        cls.diskon_member = diskon_baru
        print(f"diskon member adalah {cls.diskon_member*100:.0f}%")
    @staticmethod
    def validasi_kode_produk(kode):
        return kode.startswith("HJB-") and len(kode) > 4

class Kasir:
    nama_toko = "SYIFA HIJAB"
    total_transaksi = 0
    pajak = 0.0 
    def __init__(self, nama_kasir, shift, role="kasir"):
        self.nama_kasir = nama_kasir   # public
        self.shift = shift             # public
        # role cuma boleh "admin" atau "kasir", kalau salah default ke "kasir"
        self.role = role if role in ("admin", "kasir") else "kasir"
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
        # khusus admin, kasir biasa (user) gaboleh ubah stok langsung
        if self.role != "admin":
            print(f"akses ditolak, {self.nama_kasir} bukan admin, gabisa ubah stok")
            return
        produk.stok = stok_baru
        print(f"admin {self.nama_kasir} ubah stok '{produk.nama_produk}' jadi {produk.stok}")
    def atur_diskon(self, diskon_baru):
        # khusus admin juga
        if self.role != "admin":
            print(f"akses ditolak, {self.nama_kasir} bukan admin, gabisa ubah diskon")
            return
        Produk.ubah_diskon_member(diskon_baru)

    @classmethod
    def buat_dari_data(cls, data):
        return cls(data["nama"], data["shift"], data.get("role", "kasir"))
    @classmethod
    def reset_total_transaksi(cls):
        cls.total_transaksi = 0
        print("total transaksi sudah direset ke 0.")
    @staticmethod
    def hitung_total_harga(harga, jumlah):
        return harga * jumlah

class Pelanggan:
    jenis_member = ["reguler", "silver", "gold"]
    total_pelanggan = 0
    poin_per_pembelian = 5
    def __init__(self, nama, no_hp, member="reguler"):
        self.nama = nama            # public
        self.member = member        # public
        self.__no_hp = None         # private
        self.no_hp = no_hp          # lewat setter agar validasi
        self.poin = 0
        Pelanggan.total_pelanggan += 1
        
    @property
    def no_hp(self):
        return self.__no_hp[:4] + "xxxx" + self.__no_hp[-2:]
    @no_hp.setter
    def no_hp(self, nomor):
        if Pelanggan.validasi_no_hp(nomor):
            self.__no_hp = nomor
        else:
            print(f"nomor HP '{nomor}' tidak valid, harus diawali 08 dan berisi angka.")
            self.__no_hp = "081200000000"
    def tambah_poin(self):
        self.poin += Pelanggan.poin_per_pembelian
        print(f"{self.nama} dapat tambahan {Pelanggan.poin_per_pembelian} poin, total poin: {self.poin}")
    def tampilkan_data(self):
        print(f"Nama: {self.nama} | Member: {self.member} | HP: {self.no_hp} | Poin: {self.poin}")

    @classmethod
    def dari_string(cls, teks):
        nama, no_hp, member = teks.split(",")
        return cls(nama.strip(), no_hp.strip(), member.strip())
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

def cari_pelanggan(nama):
    for p in daftar_pelanggan:
        if p.nama.lower() == nama.lower():
            return p
    return None

def login():
    global kasir_aktif
    clear_screen()
    print("=== LOGIN KASIR SYIFA HIJAB ===")
    nama = input("nama kamu: ")
    role = input("login sebagai admin atau kasir? (admin/kasir): ").strip().lower()
    kasir_aktif = Kasir(nama, "harian", role)
    print(f"\nhalo {kasir_aktif.nama_kasir}, kamu login sebagai {kasir_aktif.role}")
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
    if kasir_aktif.role != "admin":
        print("hanya admin yang bisa menambah produk")
        return
    nama = input("nama produk: ")
    harga = input_angka("harga: ")
    stok = input_angka("stok awal: ")
    daftar_produk.append(Produk(nama, harga, stok))
    print("produk berhasil ditambah")


def menu_ubah_stok():
    if kasir_aktif.role != "admin":
        print("hanya admin yang bisa ubah stok")
        return
    menu_lihat_produk()
    if not daftar_produk:
        return
    idx = input_angka("pilih nomor produk: ")
    if 1 <= idx <= len(daftar_produk):
        stok_baru = input_angka("stok baru: ")
        kasir_aktif.atur_stok(daftar_produk[idx - 1], stok_baru)
    else:
        print("nomor produk tidak valid")

def submenu_produk():
    while True:
        clear_screen()
        print("=== KELOLA PRODUK ===")
        print("1. lihat produk")
        print("2. tambah produk")
        print("3. ubah stok")
        print("0. kembali")
        pilihan = input("pilih: ")
        print()
        if pilihan == "1":
            menu_lihat_produk()
        elif pilihan == "2":
            menu_tambah_produk()
        elif pilihan == "3":
            menu_ubah_stok()
        elif pilihan == "0":
            return
        else:
            print("menu tidak valid, coba lagi")
        pause()

def menu_transaksi():
    clear_screen()
    print("=== TRANSAKSI JUAL ===")
    menu_lihat_produk()
    if not daftar_produk:
        return
    idx = input_angka("pilih nomor produk: ")
    if not (1 <= idx <= len(daftar_produk)):
        print("nomor produk tidak valid")
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
        mau_daftar = input("mau daftar member? (y/n): ").strip().lower()
        if mau_daftar == "y":
            nama = input("nama: ")
            no_hp = input("no hp: ")
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
    no_hp = input("no hp: ")
    member = input("jenis member (reguler/silver/gold): ")
    daftar_pelanggan.append(Pelanggan(nama, no_hp, member))
    print("pelanggan berhasil ditambah")

def submenu_pelanggan():
    while True:
        clear_screen()
        print("=== KELOLA PELANGGAN ===")
        print("1. lihat pelanggan")
        print("2. tambah pelanggan manual")
        print("0. kembali")
        pilihan = input("pilih: ")
        print()
        if pilihan == "1":
            menu_lihat_pelanggan()
        elif pilihan == "2":
            menu_tambah_pelanggan()
        elif pilihan == "0":
            return
        else:
            print("menu tidak valid, coba lagi")
        pause()

def submenu_admin():
    if kasir_aktif.role != "admin":
        print("akses ditolak, hanya admin")
        pause()
        return
    while True:
        clear_screen()
        print("=== PANEL ADMIN ===")
        print("1. ubah diskon member")
        print("2. lihat saldo kas & total transaksi")
        print("0. kembali")
        pilihan = input("pilih: ")
        print()
        if pilihan == "1":
            diskon = input_angka("diskon baru: ", boleh_desimal=True)
            kasir_aktif.atur_diskon(diskon)
        elif pilihan == "2":
            print(f"saldo kas {kasir_aktif.nama_kasir}: Rp{kasir_aktif.saldo_kas:,}")
            print(f"total transaksi semua kasir: {Kasir.total_transaksi}")
        elif pilihan == "0":
            return
        else:
            print("menu tidak valid, coba lagi")
        pause()
        
def tampilkan_menu():
    print(f"===== SYIFA HIJAB ({kasir_aktif.nama_kasir} - {kasir_aktif.role}) =====")
    print("1. kelola produk")
    print("2. transaksi jual")
    print("3. kelola pelanggan")
    print("4. panel admin")
    print("0. keluar")

if __name__ == "__main__":
    login()
    while True:
        clear_screen()
        tampilkan_menu()
        pilihan = input("pilih menu: ")
        print()
        if pilihan == "1":
            submenu_produk()
        elif pilihan == "2":
            menu_transaksi()
            pause()
        elif pilihan == "3":
            submenu_pelanggan()
        elif pilihan == "4":
            submenu_admin()
        elif pilihan == "0":
            print("terima kasih sudah pakai program SYIFA HIJAB")
            break
        else:
            print("menu tidak valid, coba lagi")
            pause()