print("-----selamat datang bosku-----")
print("buat akun dulu ya")

print("---------------------------------")

data = {}

username= input("masukan username:")
passwoard =input("masukan password:")
data[username] = passwoard 

print("terima kasih udah login")
print("-----------------------")
print("masuk untuk mulai")

username = input("masukan username:")
passwoard = input("masukan passwoard:")

if username in data:
    if passwoard == data[username]:
        print("login berasil")
        print("------------------")
        print("pilih salah satu di bawah")
        
        
    else:
        print("passoard salah")    
else:
    print("username failed")        







    

    
    
