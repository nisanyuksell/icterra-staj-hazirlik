"""
OopKonsept.py
Nesne Yönelimli Programlama (OOP) kavramlarını gösteren örnek kod.
İçerir: Encapsulation, Inheritance, Polymorphism.
"""


class Araba:
    """Standart bir yakıtlı arabayı temsil eder."""

    def __init__(self, marka, model, yakit_seviyesi):
        self.marka = marka
        self.model = model
        self.__yakit_seviyesi = yakit_seviyesi  # encapsulation: dışarıdan direkt erişilemez

    def yakit_doldur(self, miktar):
        """Yakıt deposuna belirtilen miktarda yakıt ekler."""
        self.__yakit_seviyesi += miktar
        print(f"{miktar} litre yakıt dolduruldu. Güncel seviye: {self.__yakit_seviyesi}")

    def yakit_seviyesini_goster(self):
        """Aracın güncel yakıt seviyesini ekrana yazdırır."""
        print(f"{self.marka} {self.model} - Yakıt seviyesi: {self.__yakit_seviyesi}")

    def bilgi_ver(self):
        """Aracın marka ve model bilgisini ekrana yazdırır."""
        print(f"Bu araç bir {self.marka} {self.model}.")


class ElektrikliAraba(Araba):
    """Araba sınıfından türetilen, batarya ile çalışan araç (inheritance)."""

    def __init__(self, marka, model, yakit_seviyesi, batarya_kapasitesi):
        super().__init__(marka, model, yakit_seviyesi)  # üst sınıfın constructor'ı çağrılıyor
        self.batarya_kapasitesi = batarya_kapasitesi

    def sarj_et(self, miktar):
        """Bataryaya belirtilen miktarda şarj ekler."""
        self.batarya_kapasitesi += miktar
        print(f"{miktar} kWh şarj edildi. Güncel batarya: {self.batarya_kapasitesi} kWh")

    def sarj_seviyesini_goster(self):
        """Aracın güncel batarya seviyesini ekrana yazdırır."""
        print(f"{self.marka} {self.model} - Batarya seviyesi: {self.batarya_kapasitesi} kWh")

    def bilgi_ver(self):
        """Polymorphism: üst sınıftaki bilgi_ver metodunu override eder."""
        print(f"Bu araç bir elektrikli {self.marka} {self.model}. Batarya: {self.batarya_kapasitesi} kWh")


def main():
    """Test senaryosu: Araba ve ElektrikliAraba sınıflarını çalıştırır."""
    normal_araba = Araba("Toyota", "Corolla", 40)
    normal_araba.bilgi_ver()
    normal_araba.yakit_seviyesini_goster()
    normal_araba.yakit_doldur(10)

    print("-" * 30)

    elektrikli_araba = ElektrikliAraba("Tesla", "Model 3", 0, 50)
    elektrikli_araba.bilgi_ver()
    elektrikli_araba.sarj_et(20)
    elektrikli_araba.sarj_seviyesini_goster()


if __name__ == "__main__":
    main()