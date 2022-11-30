import abc

class IStrategy(object):
    @abc.abstractmethod
    def hitung_tarif_ojol(self) -> int:
        raise NotImplementedError

class JamNormal(IStrategy):
    def hitung_tarif_ojol(self) -> int:
        return 30000

class JamSibuk(IStrategy):
    def hitung_tarif_ojol(self) -> int:
        return 37000

if __name__ == '__main__':
    tarifOjol = JamNormal().hitung_tarif_ojol()

    print("Tarif Perjalanan Anda RP. ", tarifOjol)

    tarifOjol = JamSibuk().hitung_tarif_ojol()

    print("Tarif Perjalanan Anda RP. ", tarifOjol)
