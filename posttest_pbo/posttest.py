import os

class AkunPoint:
    def __init__(self):
        self.total_poin = 0
        
    def tambah(self, poin):
        self.total_poin += poin

class Produk:
    def __init__(self, nama_produk, harga, stok):
        self.nama_produk = nama_produk  
        self.harga = harga              
        self.__stok = stok  # Private
        self.kategori = "Umum"
    def get_stok(self):
        return self.__stok
    def set_stok(self, stok_baru):
        if stok_baru >= 0:
            self.__stok = stok_baru
        else:
            print("Stok tidak boleh minus!")
    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        else:
            print(f"Stok '{self.nama_produk}' tidak cukup!")
            return False

class Hijab(Produk):
    def __init__(self, nama_produk, harga, stok):
        super().__init__(nama_produk, harga, stok)
        self.kategori = "Hijab"

class Aksesoris(Produk):
    def __init__(self, nama_produk, harga, stok):
        super().__init__(nama_produk, harga, stok)
        self.kategori = "Aksesoris"

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
        print("\n=======================================================")
        print(f"               KATALOG PRODUK {self.nama.upper()}")
        print("=======================================================")
        print(f"{'No':<3} | {'Kategori':<10} | {'Nama Produk':<20} | {'Harga':<10} | {'Stok':<5}")
        print("-------------------------------------------------------")
        
        for i, p in enumerate(self.katalog_produk, start=1):
            print(f"{i:<3} | {p.kategori:<10} | {p.nama_produk:<20} | Rp{p.harga:<8} | {p.get_stok():<5}")
            
        print("=======================================================")
        return True

class Kasir:
    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir   
        self.saldo_kas = 0           
    def proses_transaksi(self, produk, jumlah):
        if jumlah <= 0:
            print("Jumlah beli harus lebih dari 0!")
            return False
            
        if produk.kurangi_stok(jumlah):
            total_bayar = produk.harga * jumlah
            self.saldo_kas += total_bayar
            print(f"\n[+] Penjualan berhasil: {jumlah}x {produk.nama_produk} = Rp{total_bayar}")
            return True
        return False
    def atur_stok(self, produk, stok_baru):
        produk.set_stok(stok_baru)
        print(f"[+] Stok '{produk.nama_produk}' berhasil diubah jadi {produk.get_stok()}")
    def bantu_pelanggan_member(self, pelanggan):
        print(f">> Kasir {self.nama_kasir} menambah poin member {pelanggan.nama}")
        pelanggan.tambah_poin()

class Pelanggan:
    def __init__(self, nama, no_hp):
        self.nama = nama            
        self.no_hp = no_hp          
        self.akun_poin = AkunPoint() 
    def tambah_poin(self):
        self.akun_poin.tambah(5)
        print(f"[+] {self.nama} dapat 5 poin. Total poin: {self.akun_poin.total_poin}")
    def tampilkan_data(self):
        print(f"Nama: {self.nama:<12} | HP: {self.no_hp:<13} | Poin: {self.akun_poin.total_poin}")

toko_syifa = Toko("Syifa Hijab")
daftar_pelanggan = []
kasir_aktif = None

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def pause():
    input("\nTekan enter untuk lanjut...")
    
def cari_pelanggan(nama):
    for p in daftar_pelanggan:
        if p.nama.lower() == nama.lower():
            return p
    return None

def login():
    global kasir_aktif
    clear_screen()
    print("=== LOGIN KASIR ===")
    nama = input("Masukkan nama kasir: ")
    kasir_aktif = Kasir(nama)
    print(f"Selamat bertugas, {kasir_aktif.nama_kasir}!")
    pause()
    
def menu_tambah_produk():
    print("\nPilih Kategori:")
    print("1. Hijab")
    print("2. Aksesoris")
    pilihan = input("Pilihan (1/2): ")
    nama = input("Nama produk: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok awal: "))
    if pilihan == "1":
        p_baru = Hijab(nama, harga, stok)
    elif pilihan == "2":
        p_baru = Aksesoris(nama, harga, stok)
    else:
        print("Pilihan tidak valid!")
        return
    toko_syifa.tambah_produk(p_baru)
    print("[+] Produk berhasil ditambahkan!")
    
def menu_ubah_stok():
    if toko_syifa.lihat_katalog():
        idx = int(input("\nPilih nomor produk: "))
        if 1 <= idx <= len(toko_syifa.katalog_produk):
            stok_baru = int(input("Masukkan stok baru: "))
            kasir_aktif.atur_stok(toko_syifa.katalog_produk[idx - 1], stok_baru)
        else:
            print("Nomor produk salah!")
            
def menu_transaksi():
    clear_screen()
    if not toko_syifa.lihat_katalog():
        return
        
    idx = int(input("\nPilih nomor produk: "))
    if 1 <= idx <= len(toko_syifa.katalog_produk):
        produk = toko_syifa.katalog_produk[idx - 1]
        jumlah = int(input("Jumlah beli: "))
        if kasir_aktif.proses_transaksi(produk, jumlah):
            is_member = input("Apakah pelanggan member? (y/n): ").lower()
            if is_member == "y":
                nama_m = input("Nama member: ")
                pelanggan = cari_pelanggan(nama_m)
                if pelanggan:
                    kasir_aktif.bantu_pelanggan_member(pelanggan)
                else:
                    print("Member tidak ditemukan!")
            elif is_member == "n":
                daftar = input("Mau daftar member? (y/n): ").lower()
                if daftar == "y":
                    nama_b = input("Nama: ")
                    hp_b = input("No HP: ")
                    p_baru = Pelanggan(nama_b, hp_b)
                    daftar_pelanggan.append(p_baru)
                    kasir_aktif.bantu_pelanggan_member(p_baru)
    else:
        print("Nomor produk salah!")
        
def menu_lihat_pelanggan():
    if not daftar_pelanggan:
        print("Belum ada data pelanggan.")
        return
    print("\n=== DAFTAR MEMBER ===")
    for p in daftar_pelanggan:
        p.tampilkan_data()

def menu_tambah_pelanggan():
    nama = input("Nama pelanggan: ")
    no_hp = input("No HP: ")
    daftar_pelanggan.append(Pelanggan(nama, no_hp))
    print("[+] Pelanggan berhasil ditambahkan!")

if __name__ == "__main__":
    login()
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
        pilihan = input("Pilih menu: ")
        print()
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
            print(f"Saldo Kas: Rp{kasir_aktif.saldo_kas}")
        elif pilihan == "0":
            print("Selesai. Terima kasih!")
            break
        else:
            print("Pilihan menu salah!")
            
        pause()