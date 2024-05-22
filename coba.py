jumlah_pemain = int(input("Masukkan jumlah pemain: "))
kartu = list(range(1, 53))
hasil = [[] for _ in range(jumlah_pemain)]

def bagibagi(kartunya, pemainya, dari=0, hasil=hasil):
    if not kartunya:
        return hasil
    
    hasil[dari].append(kartunya[0])
    
    return bagibagi(kartunya[1:], pemainya, dari, hasil)

bagibagi(kartu, jumlah_pemain)

for i, pemain in enumerate(hasil, 1):
    print(f"Pemain {i}: {pemain}")
