import networkx as nx
from networkx.classes import degree

from database.dao import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph() #grafico, semplice, non diretto ma pesato

        self._lista_rifugi = DAO.ReadRifugi()
        #dictionary comprehension
        self._dict_rifugi = {rifugio.id: rifugio for rifugio in self._lista_rifugi}

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        #aggiungo i nodi
        self._grafo.clear()

        connessioni = DAO.get_connessioni(year, self._dict_rifugi)

        #Aggiungo gli archi
        edges = [(c.id_rifugio1, c.id_rifugio2) for c in connessioni]
        #edges riceve delle tuple di nodi
        self._grafo.add_edges_from(edges)


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        return list(self._grafo.nodes)

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        return self._grafo.degree[node]

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        return nx.number_connected_components(self._grafo)

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

        id_rifugio_start = start.id
        rifugio_richiesto = self._dict_rifugi[id_rifugio_start]

        # METODO 1: NetworkX (DFS Tree)
        albero = nx.dfs_tree(self._grafo, rifugio_richiesto)
        risultato_nx = list(albero.nodes())    #nel controller reggiungibili è una lista
        #tolgo il nodo di partenza
        if rifugio_richiesto in risultato_nx:
            risultato_nx.remove(rifugio_richiesto)

        #METODO 2: DFS Ricorsivo
        visitati = {rifugio_richiesto}
        # Avvio la ricorsione
        self._ricorsione(rifugio_richiesto, visitati)
        visitati.remove(rifugio_richiesto)
        lista_visitabili = list(visitati)

        return lista_visitabili
        #return risultato_nx   per verifica

    def _ricorsione(self, nodo_corrente, visitati):
        #scorro tutti i vicini del nodo_corrente
        vicini = list(self._grafo.neighbors(nodo_corrente))

        #CONDIZIONE DI USCITA
        #quando non ci sono più vicini da visitare
        if vicini == []:
            return

        #RICORSIONE
        for vicino in vicini:
            if vicino not in visitati:
                visitati.add(vicino)
                #passo vicino come nodo corrente nella ricorsione
                self._ricorsione(vicino, visitati)

