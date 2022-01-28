"""
Program Perulangan Baca Buku Sampai Paham dengan WHILE
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua buku sampai paham.')

total_jumlah_baca = 0

jumlah_buku_dibaca_dipahami = 0
print(f"jumlah buku yang telah dibaca dan dipahami {jumlah_buku_dibaca_dipahami}.")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_dibaca_dipahami == 9:
        print(f"Buku ke {jumlah_buku_dibaca_dipahami + 1} belum paham.")
    else:
        jumlah_buku_dibaca_dipahami = jumlah_buku_dibaca_dipahami + 1
        print(f"Buku ke {jumlah_buku_dibaca_dipahami} telah dibaca dan dipahami.")

print(f"Total buku yang telah dibaca dan dipahami {jumlah_buku_dibaca_dipahami}.")

