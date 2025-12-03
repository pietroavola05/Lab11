from dataclasses import dataclass

@dataclass
class Connessione:
    id_connessione :int
    id_rifugio1: int
    id_rifugio2: int
    distanza : float
    difficolta : int
    durata: float
    anno: int

    def __hash__(self):
        return hash(self.id_connessione)

    def __str__(self):
        TODO
        TODO