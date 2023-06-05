Keszitsen programot C++ nyelven, mely egy GPS track osztalyt valosit meg. 

Az osztalynak legyen egy `record(double x, double y, int seconds)` metodusa, mely egy poziciot es timestampet kap, es egy ujabb GPS vetelt tarol el. Az `x` es `y` meterben kifejezett relativ szelessegi es hosszusagi koordinatak egy alap ponthoz viszonyitva. 

A feladat idejere tetelezzuk fel, hogy a Fold lapos.

Az osztalynak legyen meg `totalDistance` es `totalTime` metodusa, melyek `double` / `int` tipusuan, meterben illetve masodpercben kifejezve visszaadjak az eddigi teljes tavot, idot. 

Az osztaly konstruktora varjon egy `maxSpeed` erteket, mely m/s-ban kifejezve ad meg egy maximalis sebesseget. Ha ket egymast koveto pont kozott a sebesseg ennel nagyobb, akkor ne rogzitse, hanem dobjon egy tetszoleges kivetelt. 

Az osztalynak ezzel a koddal egyutt kell tudnia mukodni:

```cpp
Track t(6.7);
t.record(0,0,0);
t.record(1,2.3,4);
...
t.record(12.3,46.7,108);
std::cout << t.totalDistance() << " " << t.totalTime << std::endl;
```

