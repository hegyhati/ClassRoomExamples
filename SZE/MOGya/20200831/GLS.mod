/*

Feladatunk automata postacsomag atveteli pontok optimalis helyet megtervezni egy hosszu utcaban.

Adott egy utca (leagazo utak nincsenek), valamint ezen tarsashazak.

Minden tarsashazrol tudjuk, hogy az utca elejetol szamitva milyen messze van, illetve hogy hanyan laknak ott.

Feltetelezheto, hogy minden lakos nagyjabol ugyanakkora intenzitassal rendel valamit maganak valamilyen webshopbol, amiert aztan a mi valamelyik atveteli pontunkba kell elsetalnia.

Nekunk most azt kell megtervezni, hogy hova telepitsuk le ezeket az atvevo pontokat ugy, hogy az utca lakosainak koreben az atvetelhez szukseges atlagos setalasi tavolsag minimalis legyen.

Parameterben adott, hogy hany pont telepitesere van koltsegvetesunk, valamint egy lista a lehetseges telepitesi pontok helyerol (utca elejetol vett tavolsagarol). 

Az egyszeruseg kedveert feltetelezheto, hogy mindenki "visszafele" (az utca eleje fele) a legkozelebbi pontra fogja kerni a csomagjat.

Keszitsunk egy olyan MILP modellt, mely megmondja, hogy melyik pontokra telepitsunk atvevo automatatat, hogy az atlagos setalasi tav minimalis legyen.

*/





/*

Jobb jegyert:

Nem adottak a lehetseges automata helyek, ezeket szabadon eldonthetjuk, valamint a lakok mindig a legkozelebbi ponthoz mennek, akkor is, ha az az utca eleje vagy vege fele van. 

A cel pedig nem az atlagos setalasi tavolag, hanem a maximalis setalasi tavolsag minimalizalasa.

*/
