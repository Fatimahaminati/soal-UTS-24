jarak_meter = float(input("Masukkan jarak dalam meter: "))

jarak_km = jarak_meter / 1000

if jarak_km < 2:
    kategori = "Dekat"
elif 2 <= jarak_km < 10:
    kategori = "Jauh"
else:
    kategori = "Sangat Jauh"

print(f"Jarak dalam kilometer: {jarak_km} KM")
print(f"Kategori jarak: {kategori}")