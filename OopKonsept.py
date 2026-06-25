class Araba:
    def __init__(self, marka, model, yakit_seviyesi):
        self.marka = marka
        self.model = model
        self.__yakit_seviyesi = yakit_seviyesi  # encapsulation: private değişken

    def yakit_doldur(self, miktar):
        self.__yakit_seviyesi += miktar
        print(f"{miktar} litre yakıt dolduruldu. Güncel seviye: {self.__yakit_seviyesi}")

    def yakit_seviyesini_goster(self):
        print(f"{self.marka} {self.model} - Yakıt seviyesi: {self.__yakit_seviyesi}")

    def bilgi_ver(self):
        print(f"Bu araç bir {self.marka} {self.model}.")


class ElektrikliAraba(Araba):  # inheritance: Araba sınıfından türetildi
    def __init__(self, marka, model, yakit_seviyesi, batarya_kapasitesi):
        super().__init__(marka, model, yakit_seviyesi)  # üst sınıfın constructor'ını çağırıyoruz
        self.batarya_kapasitesi = batarya_kapasitesi

    def sarj_et(self, miktar):
        self.batarya_kapasitesi += miktar
        print(f"{miktar} kWh şarj edildi. Güncel batarya: {self.batarya_kapasitesi} kWh")

    def bilgi_ver(self):  # polymorphism: üst sınıftaki metodu eziyoruz (override)
        print(f"Bu araç bir elektrikli {self.marka} {self.model}. Batarya: {self.batarya_kapasitesi} kWh")


# --- Test Senaryosu ---
if __name__ == "__main__":
    normal_araba = Araba("Toyota", "Corolla", 40)
    normal_araba.bilgi_ver()
    normal_araba.yakit_seviyesini_goster()
    normal_araba.yakit_doldur(10)

    print("-" * 30)

    elektrikli_araba = ElektrikliAraba("Tesla", "Model 3", 0, 50)
    elektrikli_araba.bilgi_ver()
    elektrikli_araba.sarj_et(20)
    elektrikli_araba.yakit_seviyesini_goster()  # kalıtım sayesinde Araba'dan gelen metodu kullanabiliyor