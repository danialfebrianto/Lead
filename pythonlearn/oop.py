class bank:
    
    def __init__(self):
        self.daftar = {}
        self.saldo = []
        self.mutasi = []
        self.transfer = {}
        
    def menu (self):
        
        while True:
            print("pilih menu berikut")
            print("1.buat")
            print("2.masuk")
            print("3.isi saldo")
            print("4.keluar")
            
            p = input("masukan pilihanmu: ")
            if p == "1":
                self.buat()
            elif p == "2":
                self.masuk()
            elif p == "3":
                self.tambahsaldo()
            elif p == "4":             
             break
        
    def buat(self):
        username = input("masukan nama: ")
        passwoard = input("masukan passwoard kamu: ")
        self.daftar[username] = passwoard
        print(self.daftar)
        
            
    def masuk(self):
        user = input("masukan username: ")
        pas = input("masukan passwoardnya: ")
        if user in self.daftar:
            if pas == self.daftar [user]:
                print("kamu berhasil")
        else:
            print("username salah")    
        
    def tambahsaldo(self):
        return
    
    def mutasi(self):
        return
    
    def transfer(self):
        return    
    
data = bank()
    
data.menu()
data.buat()
data.masuk()