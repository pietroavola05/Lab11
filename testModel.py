from model.model import Model

model = Model()
model.build_graph(year=1900)
nodo_richiesto = model._dict_rifugi[1]
model.get_reachable(nodo_richiesto)
