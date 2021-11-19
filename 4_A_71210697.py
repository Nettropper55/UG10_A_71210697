k = input("Masukan artikel yang ingin dipindai:" )
l = input("nama klub bola:" )
m = input("Masukan skor yang ingin dicari:")

if l + k and m+k :
    print("Hasil pencarian ditemukan")
elif l+k:
    print("Hanya kata",l, "yang ditemukan pada artikel ini")
elif m+k:
    print("Hanya skor",m, "yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian ", l, "dan", m,"tidak ditemukan")
