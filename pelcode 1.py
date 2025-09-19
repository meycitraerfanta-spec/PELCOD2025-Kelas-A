jumlah_episode =float(input("jumlah episode :"))
durasi_per_episode = float(input("durasi per menit :"))

total_durasi_per_menit = jumlah_episode * durasi_per_episode

total_durasi_jam = total_durasi_per_menit / 60

print ("total waktu menonton : ", (total_durasi_jam),"jam")