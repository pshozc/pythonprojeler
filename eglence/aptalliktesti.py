import random
import time
aptal = str(input("Aptallık Testi Yapılacak Kişinin İsimi:"))
oran = random.randint(1,100)
print("\n \nAptallık Yüzdesi Hesaplanıyor....")
time.sleep( 1.25 )
print("\n \n{} Kişisi %{} Aptal".format(aptal,oran))
