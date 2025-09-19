jarak = float(input("total jarak :"))
bbm = float(input("konsumsi bbm perkilometer "))
tanki = float(input("kapasitas tanki "))

harga_bensin = tanki * 12900
if tanki >= 3 :
   bayar = (12900 - 500) * tanki
   
   
total_bensin = jarak / bbm


asumsi = total_bensin / tanki


print ("harga bayar bbm : ", bayar)
print ("konsumsi bensin : ", total_bensin , "liter")
print ("asumsi isi ulang bensin : ", asumsi , "kali")