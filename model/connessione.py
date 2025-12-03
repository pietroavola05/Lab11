from dataclasses import dataclass

from model.rifugio import Rifugio


@dataclass
class Connessione:
    id_connessione :int
    id_rifugio1: Rifugio
    id_rifugio2: Rifugio

    def __hash__(self):
        return hash(self.id_connessione)
