data1 = []

for i in range (2):
    inputan1 = input("masukan nama:")
    inputan2 = int(input("masukan umur:"))
    print("-----------------------------")
    
    data1.append(inputan1)
    data1.append(inputan2)
    

if inputan2 > 20:
    print(f"nama: {inputan1}")
    print(f"umur: {inputan2}")
    print("status:"+"tidak boleh daftar")
if inputan2 <20:
    print(f"nama: {inputan1}")
    print(f"umur: {inputan2}")
    print("status:"+"kamu boleh daftar")
    
    print(data1)
    

