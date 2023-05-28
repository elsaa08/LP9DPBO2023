from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, lama):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.lama = lama

    def get_dokumen(self):
        return "\nSertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."
   
    def get_nama_pemilik(self):
        return self.nama_pemilik
    def get_detail(self):
        return "Hunian Apartemen \nPemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n"
    def get_lama(self):
        return "Lama Sewa : " + str(self.lama) + " tahun." + "\n"
