import random

angka_rahasia = random.randint(1, 100)
tebakan = None
percobaan = 0

print("Tebak angka antara 1 dan 100")

while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan Anda: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu rendah!")
    elif tebakan > angka_rahasia:
        print("Terlalu tinggi!")
    else:
        print(f"Selamat! Anda menebak dengan benar dalam {percobaan} percobaan.")
