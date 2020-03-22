- Dati OSM

I dati sono ricavati con query overpass:

```
( area[name=Cuneo]; )->.searchArea;
(
  nwr["delivery"][delivery!=no]["name"!="La cantinetta"]["name"!="Tokyo Fusion Restaurant"](area.searchArea);
);
out body center;
>;

```

l'output va salvato come:

```
delivery.osm
```

- Categorie

Installare python 3 e osmfilter
```
$ python categories.py
```


- Icone su Umap

Incollare questo link nelle impostazioni del layer:

```
https://raw.githubusercontent.com/fansanelli/delivery-cuneo/master/markers/{amenity}{office}{shop}.png
```

TUTTI I DIRITTI SULLE ICONE SONO DI PROPRIETA' DI ICON FINDER (https://www.iconfinder.com/)
