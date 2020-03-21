dati ricavati con query overpass:

```
( area[name=Cuneo]; )->.searchArea;
(
  nwr["delivery"][delivery!=no]["name"!="La cantinetta"]["name"!="Tokyo Fusion Restaurant"](area.searchArea);
);
out body center;
>;

```

per attivare le icone:

```
https://raw.githubusercontent.com/fansanelli/delivery-cuneo/master/markers/{amenity}{office}{shop}.png
```

TUTTI I DIRITTI SULLE ICONE SONO DI PROPRIETA' DI ICON FINDER (https://www.iconfinder.com/)
