from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, lama):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.lama = lama
   
    
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    def get_lama(self):
        return "\nLama Sewa : " + str(self.lama) + " tahun.\n"

    def get_detail(self):
        return "Hunian Rumah \nNama Pemilik : " + self.nama_pemilik + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nJumlah Kamar : " + str(self.jml_kamar) 
   