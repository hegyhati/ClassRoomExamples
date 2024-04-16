var Kincso_Optimalizalas binary;
var Kincso_Prognyelvek binary;
var Kincso_Webvizualizalas binary;
var Kincso_PowerBI binary;
var Kincso_Coursera binary;
var Kincso_DataAkarmi binary;

var Halu_Optimalizalas binary;
var Halu_Prognyelvek binary;
var Halu_Webvizualizalas binary;
var Halu_PowerBI binary;
var Halu_Coursera binary;
var Halu_DataAkarmi binary;

var Akos_Optimalizalas binary;
var Akos_Prognyelvek binary;
var Akos_Webvizualizalas binary;
var Akos_PowerBI binary;
var Akos_Coursera binary;
var Akos_DataAkarmi binary;


s.t. Kincso_munkamennyiseg:
Kincso_Optimalizalas + Kincso_Prognyelvek + Kincso_Webvizualizalas + Kincso_PowerBI + Kincso_Coursera + Kincso_DataAkarmi  = 2;

s.t. Halu_munkamennyiseg:
Halu_Optimalizalas + Halu_Prognyelvek + Halu_Webvizualizalas + Halu_PowerBI + Halu_Coursera + Halu_DataAkarmi =2 ;

s.t. Akos_munkamennyiseg:
Akos_Optimalizalas + Akos_Prognyelvek + Akos_Webvizualizalas + Akos_PowerBI + Akos_Coursera + Akos_DataAkarmi  =2;

s.t. Pontosan_egyszer_Optimalizalas:
               Kincso_Optimalizalas +
                 Halu_Optimalizalas + 
                 Akos_Optimalizalas = 1;
s.t. Pontosan_egyszer_Prognyelvek:
               Kincso_Prognyelvek +
                 Halu_Prognyelvek + 
                 Akos_Prognyelvek = 1;
s.t. Pontosan_egyszer_Webvizualizalas:
               Kincso_Webvizualizalas +
                 Halu_Webvizualizalas + 
                 Akos_Webvizualizalas = 1;
s.t. Pontosan_egyszer_PowerBI:
               Kincso_PowerBI +
                 Halu_PowerBI + 
                 Akos_PowerBI = 1;
s.t. Pontosan_egyszer_Coursera:
               Kincso_Coursera +
                 Halu_Coursera + 
                 Akos_Coursera = 1;
s.t. Pontosan_egyszer_DataAkarmi:
               Kincso_DataAkarmi +
                 Halu_DataAkarmi + 
                 Akos_DataAkarmi = 1;



minimize Sorok_szama :
5 * Kincso_Optimalizalas +
2 * Kincso_Prognyelvek +
3 * Kincso_Webvizualizalas +
6 * Kincso_PowerBI +
4 * Kincso_Coursera +
10 * Kincso_DataAkarmi +
0 * Halu_Optimalizalas +
6 * Halu_Prognyelvek +
2 * Halu_Webvizualizalas +
12 * Halu_PowerBI +
34 * Halu_Coursera +
5 * Halu_DataAkarmi +
6 * Akos_Optimalizalas +
4 * Akos_Prognyelvek +
6 * Akos_Webvizualizalas +
4 * Akos_PowerBI +
23 * Akos_Coursera +
2 * Akos_DataAkarmi;


end;
