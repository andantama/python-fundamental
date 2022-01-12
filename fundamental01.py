"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu memberi perintah,"Beli 1 botol susu"')
print('Andi menjawab,"Ok"')
print('Ibu memberi perintah tambahan, "Dan jika ada jual telur, maka beli juga 6 butir telur."')
print('Andi merespon, "Ok,bu."')
print("Andi pergi ke toko dan mulai berbelanja.")

# Percabangan
jumlah_botol_susu = 100

if jumlah_botol_susu > 0:
    print("Andi cek harga susu, dan uangnya cukup.")
    print("Andi membeli 1 botol susu.")
else:
    print("Andi tidak jadi membeli susu")

print("Andi pulang ke rumah.")
print("Andi menyerahkan barang belanjaan kepada ibu.")
