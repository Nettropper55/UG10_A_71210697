x=str(input("Mendatar/Menurun?" ))

if x == 'Mendatar':
    y=int(input("Masukkan kolom: " ))
    print("#"*y)
elif x== 'Menurun':
    y=int(input("Masukkan baris: " ))
    row="* \n"
    print(row*y)
else:
    print("Pola tidak dikenali")
