rata = float(input("Masukan nilai rata-rata UG anda"))
TTS = float(input("Masukan nilai TTS anda"))
TAS = float(input("Masukan nilai TAS anda"))

print("="*25)
R=(0.7*rata)
T=(0.15*TTS)
S=(0.15*TAS)
v=(R+T+S)

print("Nilai anda:", v)

if v >= 85 :
    print("Nilai huruf anda: A")
elif v >=80 :
    print("Nilai huruf anda: A-")
elif v >=75 :
    print("Nilai huruf anda: B+")
elif v >=70 :
    print("Nilai huruf anda: B")
elif v >=65 :
    print("Nilai huruf anda: B-")
elif v >=60 :
    print("Nilai huruf anda: C+")
elif v >=55 :
    print("Nilai huruf anda: C")
elif v >=45 :
    print("Nilai huruf anda: D")
else :
    print("Nilai huruf anda: E")

