# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HVHFWbR7Od7aaov0aB2nLLvyIPgiI2jI
"""

print("pilih operasi")
print("1. Jumlah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
pilihan = input ("Masukan pilihan operssi (1/2/3/4) : ")

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukan angka kedua: "))
if pilihan == "1":
   hasil = angka1 + angka2
   print(f"Hasil dari {angka1} + {angka2} adalah {hasil}")
elif pilihan == "2":
  hasil = angka1 - angka2
  print(f"Hasil dari {angka1} - {angka2} adalah {hasil}")
elif pilihan == "3":
  hasil = angka1 * angka2
  print(f"Hasil dari {angka1} x {angka2} adalah {hasil}")
elif pilihan == "4":
  hasil = angka1 / angka2
  print(f"Hasil dari {angka1} : {angka2} adalah {hasil}")

# I GEDE OKTA ANDIKA YASA
# 2401010745
# INFORMATIKA

print("penjumlahan (angka1 , angka2)")

# Program Penjumlahan Sederhana
def penjumlahan(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

# Meminta input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Memanggil fungsi penjumlahan dan menampilkan hasil
hasil = penjumlahan(angka1, angka2)
print(f"Hasil dari {angka1} + {angka2} adalah {hasil}")