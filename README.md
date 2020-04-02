- Dati OSM

I dati sono ricavati con query overpass:

```
( area[name=Cuneo]; )->.searchArea;
(
  node["delivery"][delivery!=no]["name"!="Tokyo Fusion Restaurant"](area.searchArea);
  way["delivery"][delivery!=no](area.searchArea);>;
  node["delivery:covid19"](area.searchArea);
  way["delivery:covid19"](area.searchArea);>;

);
out body;

```

l'output va salvato come:

```
delivery.osm
```

- Categorie

Installare python 3, osmfilter e osmconvert
```
$ python categories.py
```


- Icone su Umap

Incollare questo link nelle impostazioni del layer:

```
https://raw.githubusercontent.com/fansanelli/delivery-cuneo/master/markers/{amenity}{office}{shop}.png
```

TUTTI I DIRITTI SULLE ICONE SONO DI PROPRIETA' DI ICON FINDER (https://www.iconfinder.com/)
