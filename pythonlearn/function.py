
penghasilan = []

def tarik_saldo(penghasilan, tarik):
    if tarik <= penghasilan[0]:
         penghasilan[0] -= tarik
         return penghasilan[0]
    else:
           print("saldo tidak cukup")
def cek_saldo(penghasilan):
       return penghasilan[0]
def tambah_saldo(penghasilan, hasil):
       nominal = penghasilan + hasil
       return nominal


while True:    
    
 print("HALO SELAMAT DATANG")
 print("1.setor saldo")
 print("2.tarik saldo")
 print("3.cek saldo")
 print("4.keluar")

 pilih = input("masukan pilihanmu: ")


 if pilih == "1":
        hasil = int(input("masukan saldo: "))
        penghasilan.append(hasil)
        print(f"ini adalah saldomu {penghasilan}")
        
 elif pilih == "2":
        tarik = int(input("masukan penarikan:"))
        p = tarik_saldo(penghasilan,tarik)
        print("saldo kamu :", p)

        
 elif pilih == "3":
        print("penghasilanmu adalah: ", cek_saldo(penghasilan))  
        
 elif pilih == "4":
    break 
    