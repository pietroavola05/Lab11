from dataclasses import dataclass

@dataclass
class Rifugio:
    id_rifugio: int
    nome: str
    localita: str
    altitudine : float
    capienza : int
    aperto: True


    def __hash__(self):
            return hash(self.id_rifugio)

    def __eq__(self, other):
        return self.id_rifugio == other.id_rifugio

    def __str__(self):
        return self.nome



