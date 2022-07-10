#!/usr/bin/env python3

import os

os.system("clear")
os.system("pkg install nmap -y")
os.system("pkg install whois")
os.system("pkg install figlet")
os.system("clear")
os.system("figlet MAMI")
print("""
İslemler

1) Site Hakkında Genel Bilgi
2) Hızlı Port Taraması
3) Versiyon bilgisi
4) Kişiye Özel Word List
5) Oltalama linki oluştur
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")

if islemno=="1":
        hedefip= input("Hedef Site Giriniz: ")
        os.system("whois "+hedefip)
elif islemno=="2":
          hedefip= input("Hedef Site Giriniz: ")
          os.system("nmap "+hedefip)
elif islemno=="3":
          hedefip= input("Hedef Site Giriniz: ")
          os.system("nmap -sV "+hedefip)
elif islemno=="4":
          os.system("clear")
          os.system("python3 Mamiworldlist.py -i ")
elif islemno=="5":
          os.system("clear")
          os.system("bash Mamioltalama.sh")
elif islemno=="q" or islemno=="Q":
          quit()
else:
     quit()
