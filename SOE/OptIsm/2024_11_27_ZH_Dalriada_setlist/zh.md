# Optimalizálási ismeretek ZH
2024.11.26.

## Elméleti kérdések

 - Hány fázisa van a szimplex módszernek?
 - Milyen relációk megengedettek MILP modellek korlátozásaiban, amik LP-ben nem?
 - Milyen veszélye van, ha az big `M` értéket túl nagyra választjuk?
 - Igaz / Hamis?
    * LP modellnek lehet pontosan megszámlálhatóan végtelen optimális megoldása.
    * MILP modellnek lehet pontosan 2 optimális megoldása.
    * A szimplex harmadik fázisa a megtalált optimális megoldás mellé második optimális megoldást keres.
    * A `solve;` előtt nem szerepelhetnek a változók értékeire vonatkozó szűrések.

## Gyakorlati feladat: Dalriada set list

A méltán híres soproni banda, Dalriada következő koncertjén eljátszandó számok listáját kell összeállítanunk. A koncert mindenképpen 10 számból fog állni, és a hosszának 60 és 80 perc közöttinek kell lennie, a számok között fél percnyi szünettel. 

Minden számról ismert a hossza, a népszerűsége, valamint hogy a banda mely tagjai számára "megterhelő" eljátszani. A célunk, hogy az eljátszott számok össznépszerűsége minél több legyen, de nem követhet egymást három szám úgy, hogy bármelyik zenész/énekes számára mindegyik nehéz legyen.

<table>
    <tr>
        <td rowspan = 3>Szám</td>
        <td rowspan = 3>Hossz</td>
        <td rowspan = 3>Popularitás</td>
        <td rowspan = 3>Album</td>
        <td colspan = 6>Nehézség</td>
    </tr>
    <tr>
        <td>Ficzek András</td>
        <td>Binder Laura</td>
        <td>Németh-Szabó Mátyás</td>
        <td>Molnár István </td>
        <td>Szabó „Szög” Gergely </td>
        <td>Monostori Ádám</td>
    </tr>
    <tr>
        <td>ének, gitár</td>
        <td>ének</td>
        <td>gitár</td>
        <td>basszusgitár</td>
        <td>billentyűs hangszerek</td>
        <td>dob</td>
    </tr>
    <tr>
        <td>A walesi bárdok</td>
        <td>18:40</td>
        <td>61</td>
        <td>Fergeteg</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Téli ének</td>
        <td>5:50</td>
        <td>100</td>
        <td>Jégbontó</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Hajdútánc</td>
        <td>4:58</td>
        <td>87</td>
        <td>Ígéret</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Táltosének</td>
        <td>4:55</td>
        <td>55</td>
        <td>Kikelet</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Virrasztó</td>
        <td>4:50</td>
        <td>70</td>
        <td>Jégbontó</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Hamu és Gyász</td>
        <td>5:51</td>
        <td>87</td>
        <td>Áldás</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Ágnes Asszony</td>
        <td>13:21</td>
        <td>58</td>
        <td>Arany-album</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Napisten hava</td>
        <td>6:44</td>
        <td>58</td>
        <td>Napisten hava</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Galamb</td>
        <td>5:41</td>
        <td>91</td>
        <td>Mesék, Álmok, Regék</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Táltosok álma</td>
        <td>7:32</td>
        <td>71</td>
        <td>Nyárutó</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Tavaszköszöntő</td>
        <td>3:19</td>
        <td>54</td>
        <td>Szelek</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Tűzhozó</td>
        <td>4:00</td>
        <td>66</td>
        <td>Kikelet</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Kinizsi mulatsága</td>
        <td>4:19</td>
        <td>40</td>
        <td>Ígéret</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Hajnalpír</td>
        <td>4:24</td>
        <td>65</td>
        <td>Szelek</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Borivók éneke</td>
        <td>4:33</td>
        <td>57</td>
        <td>Napisten hava</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Világfa</td>
        <td>4:42</td>
        <td>86</td>
        <td>Áldás</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Betyár-altató</td>
        <td>6:24</td>
        <td>90</td>
        <td>Őszelő</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Huszáros</td>
        <td>6:15</td>
        <td>77</td>
        <td>Őszelő</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>A Dudás</td>
        <td>5:32</td>
        <td>87</td>
        <td>Napisten hava</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Hazatérés</td>
        <td>4:43</td>
        <td>56</td>
        <td>Forrás</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
</table>