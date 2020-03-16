dati ricavati con query overpass:

```
( area[name=Cuneo]; )->.searchArea;
(
  nwr["delivery"][delivery!=no]["name"!="La cantinetta"]["name"!="Tokyo Fusion Restaurant"](area.searchArea);
);
out body center;
>;

```
