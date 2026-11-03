import geometri as geo
# from geometri import luasLingkaran, volTabung

def main():
    jari2 = float(input("Masukkan jari-jari lingkaran:"))
    tinggi = float(input("Masukkan tinggi tabung: "))
    VolTab = geo.volTabung(geo.luasLingkaran(jari2), tinggi)
    #VolTab = volTabung(luasLingkaran(jari2), tinggi)

    print("Volume Tabung", VolTab)

    if __name__ == "__main__":
        main()
        
