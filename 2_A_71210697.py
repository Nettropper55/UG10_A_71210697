print("#"*28)
print("Kalkulator Advance Sederhana")
print("#"*28)
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan kebawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")
op=float(input("Masukkan menu yang anda pilih:"))
if op==1 :
    bil=float(input("Masukkan bilangan yang ingin dibagi:"))
    pemb=float(input("Masukkan bilangan pembagi: "))
    h1 =(bil % pemb)
    print("Sisa hasil bagi", bil,"dibagi dengan",pemb,"adalah",h1)
elif op==2 :
    bil = float(input("Masukkan bilangan yang ingin dibagi:"))
    pemb = float(input("Masukkan bilangan pembagi: "))
    h2 = float(int(bil / pemb))
    print("Hasil pembagian", bil, "dibagi dengan", pemb, "dibulatkan kebawah adalah ", h2)
elif op==3 :
    bil = float(input("Masukkan bilangan yang ingin dicari akar kubiknya:"))
    h3 = float(bil **(1/3))
    print("Akar kubik dari", bil, "adalah",h3)
else:
    print("Menu yang anda pilih tidak tersedia")