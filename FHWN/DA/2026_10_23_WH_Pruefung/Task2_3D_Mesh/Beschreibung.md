# Aufgabe 2 – 3D-Mesh

## Hintergrund

In der 3D-Computergrafik werden Objekte häufig durch eine Sammlung zusammenhängender Dreiecke dargestellt.
Beim Rendern dieser Dreiecke (mit ihren Texturen) muss die Engine geschickt entscheiden, welche Dreiecke die Kamera tatsächlich sehen kann. Anschließend folgen zahlreiche Matrixmultiplikationen.

Unser Ziel ist es, eine sehr einfache Lösung für diesen ersten Filterungsschritt bereitzustellen.

## Hauptziel

Die Hauptaufgabe besteht darin, diese Funktion zu implementieren:

```c
const Mesh closest_triangles(const Mesh mesh, const Point p, const size_t count);
```

Dabei gilt:
 - `mesh` enthält alle Dreiecke.
 - `p` ist der Punkt, an dem sich der Betrachter befindet.
 - `count` ist die Anzahl der Dreiecke, die unsere GPU auf dem Bildschirm darstellen kann, damit eine Bildwiederholrate von 120 Hz beibehalten wird.
 - Die Funktion soll eine Teilmenge der `count` Dreiecke zurückgeben, die dem Betrachter am nächsten liegen.
 - Damit die gewünschte Bildwiederholrate eingehalten wird, darf unser Filteralgorithmus nicht langsamer als $O(n\log{n})$ sein, wobei $n$ die Anzahl der Dreiecke in `mesh` ist.

## Technische Details

### Beispieldaten

Die Beispieldaten befinden sich in [bunny.txt](bunny.txt):

```
144046
-0.630100 1.499700 -0.541100 -0.620500 1.505400 -0.542300 -0.621000 1.497800 -0.541700 
-0.621000 1.497800 -0.541700 -0.620500 1.505400 -0.542300 -0.615700 1.499800 -0.538700 
-0.621000 1.497800 -0.541700 -0.615700 1.499800 -0.538700 -0.615400 1.491800 -0.537400 
-0.615400 1.491800 -0.537400 -0.615700 1.499800 -0.538700 -0.614100 1.498600 -0.532500 
-0.615400 1.491800 -0.537400 -0.614100 1.498600 -0.532500 -0.613800 1.489000 -0.528000 
```

Die erste Zeile enthält die Anzahl der Dreiecke. Jede weitere Zeile enthält die Koordinaten der drei Eckpunkte eines Dreiecks im Format `x1 y1 z1 x2 y2 z2 x3 y3 z3`.

In der Funktion `main` (die nicht geändert werden darf) werden für zwei Betrachterpositionen: $(1,1,1)$ und $(-1,-1,-1)$ die jeweils nächsten 1, 5, 10, 100, 1000, 10000 und 10000 Dreiecke gefiltert.
Die erwarteten Ausgabedateien sind ebenfalls vorhanden. Sie werden von `main` überschrieben. Speichere sie daher vorher an einem anderen Ort, falls du sie zum Vergleich mit deinen Ergebnissen verwenden möchtest.

### Datentypen

Die Typen für `Point` und `Triangle` sind vorgegeben. Das Design von `Mesh` ist deine Aufgabe.

```c
typedef struct {
    float x;
    float y;
    float z;
} Point;

typedef Point Triangle[3];

typedef struct {
    // TODO
} Mesh;
```

Hinweis: Da `Triangle` ein Array ist, kannst du dafür nicht den Zuweisungsoperator verwenden; stattdessen musst du `memcpy` verwenden.
Wenn du diese Typen ändern möchtest (zum Beispiel `Triangle` stattdessen als `struct` definieren, um das oben genannte Problem zu umgehen), kannst du das gerne tun. Achte dabei aber auf die bereits implementierten Funktionen, die diese Typen verwenden.

Die Grundgerüste für die Funktionen zum Einlesen und Exportieren von `Mesh` sind vorhanden, müssen aber zusammen mit der Funktion zur Speicherfreigabe vervollständigt werden:

### Zusätzliche Hilfsfunktionen, die zu vervollständigen sind

```c
const Mesh load_mesh(const char* filename) {
    // TODO
    size_t c;
    float x,y,z;
    FILE* f = fopen(filename, "r");
    fscanf(f, "%lu", &c);
    for(size_t i=0; i<c; ++i)
        for(size_t p=0; p<3; ++p)
            fscanf(f, "%f %f %f", &x, &y, &z);
    fclose(f);
}

void free_mesh(Mesh* pmesh) {
    // TODO
}

void save_to_file(const Mesh mesh, const char* filename) {
    FILE* f = fopen(filename, "w");
    fprintf(f, "%lu\n", 0 /* number of triangles here*/);
    
    /* for all triangles */
    fprintf(f, "%.6f %.6f %.6f %.6f %.6f %.6f %.6f %.6f %.6f \n", 
        1,2,3,4,5,6,7,8,9 /* the actual coordinates of the triangle*/)
        
    fclose(f);
}
```

### Distanzfunktionen

Sehr einfache Distanzfunktionen sind vorgegeben:

```c
float distance_PP(const Point p1, const Point p2) {
    return sqrtf(
        (p1.x-p2.x) * (p1.x-p2.x) +
        (p1.y-p2.y) * (p1.y-p2.y) +
        (p1.z-p2.z) * (p1.z-p2.z)
    );
}

float distance_PT(const Point p, const Triangle t) {
    return fminf(fminf(distance_PP(p,t[0]), distance_PP(p,t[1])),distance_PP(p,t[2]));
}
```

### `main`

`main` lädt den Hasen, filtert anschließend für alle Betrachterpositionen und alle `count`-Werte die Dreiecke und speichert sie in Dateien mit dem Namen `player_{player-number}_count_{count}.mesh`.

## Zusatzaufgabe

Vermeide es, unnötig Dreiecke zu sortieren, die zu weit entfernt sind.
