from database.dao import DAO

results = DAO.ReadRifugi()
dict_rifugi = {}
for rifugio in results:
    dict_rifugi[rifugio.id] = rifugio
print((results))

risultato=DAO.get_connessioni(5,dict_rifugi)
print(risultato)