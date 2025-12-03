import networkx as nx
from networkx.classes import degree

from database.dao import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph() #grafico, semplice, non diretto ma pesato
        self._lista_rifugi = []
        self.get_nodes()
        self._dict_rifugi = {}
        for rifugio in self._lista_rifugi:
            self._dict_rifugi[rifugio.id_rifugio] = rifugio

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        #aggiungo i nodi
        self._grafo.add_nodes_from(self._dict_rifugi)

        #devo cercare le connessioni nel database
        connessioni= DAO.get_connessioni(year, self._dict_rifugi)
        for c in connessioni:
            self._grafo.add_edge(c.id_rifugio1, c.id_rifugio2)


        # TODO

    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        self._lista_rifugi = DAO.ReadRifugi()

        # TODO

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        degree = node.get_degree()
        return degree

        # TODO

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        return nx.number_connected_components(self._grafo)
        # TODO

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO
