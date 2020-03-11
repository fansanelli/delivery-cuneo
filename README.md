dati ricavati con query overpass:

```
[out:json];
( area[name=Cuneo]; )->.searchArea;
(
  nwr["delivery"][delivery!=no](area.searchArea);
);
out body;
>;
out skel qt;
```
