var Klau_megcsinal_Vallalatiranyirasi_rendszerek_1 binary;
var Klau_megcsinal_Vallalatiranyitasi_rendszerek_2 binary;
var Klau_megcsinal_Termelesinformatika binary;
var Klau_megcsinal_Dontestamogato_rendszerek binary;
var Klau_megcsinal_Vallalati_gazdasagtan binary;
var Dia_megcsinal_Vallalatiranyirasi_rendszerek_1 binary;
var Dia_megcsinal_Vallalatiranyitasi_rendszerek_2 binary;
var Dia_megcsinal_Termelesinformatika binary;
var Dia_megcsinal_Dontestamogato_rendszerek binary;
var Dia_megcsinal_Vallalati_gazdasagtan binary;
var Gellert_megcsinal_Vallalatiranyirasi_rendszerek_1 binary;
var Gellert_megcsinal_Vallalatiranyitasi_rendszerek_2 binary;
var Gellert_megcsinal_Termelesinformatika binary;
var Gellert_megcsinal_Dontestamogato_rendszerek binary;
var Gellert_megcsinal_Vallalati_gazdasagtan binary;


s.t. Klau:
	2 >= 0 + Klau_megcsinal_Vallalatiranyirasi_rendszerek_1  + Klau_megcsinal_Vallalatiranyitasi_rendszerek_2  + Klau_megcsinal_Termelesinformatika  + Klau_megcsinal_Dontestamogato_rendszerek  + Klau_megcsinal_Vallalati_gazdasagtan  >= 1;

s.t. Dia:
	2 >= 0 + Dia_megcsinal_Vallalatiranyirasi_rendszerek_1  + Dia_megcsinal_Vallalatiranyitasi_rendszerek_2  + Dia_megcsinal_Termelesinformatika  + Dia_megcsinal_Dontestamogato_rendszerek  + Dia_megcsinal_Vallalati_gazdasagtan  >= 1;

s.t. Gellert:
	2 >= 0 + Gellert_megcsinal_Vallalatiranyirasi_rendszerek_1  + Gellert_megcsinal_Vallalatiranyitasi_rendszerek_2  + Gellert_megcsinal_Termelesinformatika  + Gellert_megcsinal_Dontestamogato_rendszerek  + Gellert_megcsinal_Vallalati_gazdasagtan  >= 1;

s.t. Vallalatiranyirasi_rendszerek_1:
	0 + Klau_megcsinal_Vallalatiranyirasi_rendszerek_1  + Dia_megcsinal_Vallalatiranyirasi_rendszerek_1  + Gellert_megcsinal_Vallalatiranyirasi_rendszerek_1  = 1;

s.t. Vallalatiranyitasi_rendszerek_2:
	0 + Klau_megcsinal_Vallalatiranyitasi_rendszerek_2  + Dia_megcsinal_Vallalatiranyitasi_rendszerek_2  + Gellert_megcsinal_Vallalatiranyitasi_rendszerek_2  = 1;

s.t. Termelesinformatika:
	0 + Klau_megcsinal_Termelesinformatika  + Dia_megcsinal_Termelesinformatika  + Gellert_megcsinal_Termelesinformatika  = 1;

s.t. Dontestamogato_rendszerek:
	0 + Klau_megcsinal_Dontestamogato_rendszerek  + Dia_megcsinal_Dontestamogato_rendszerek  + Gellert_megcsinal_Dontestamogato_rendszerek  = 1;

s.t. Vallalati_gazdasagtan:
	0 + Klau_megcsinal_Vallalati_gazdasagtan  + Dia_megcsinal_Vallalati_gazdasagtan  + Gellert_megcsinal_Vallalati_gazdasagtan  = 1;

minimize Osszesora:
	0 + 22 * Klau_megcsinal_Vallalatiranyirasi_rendszerek_1  + 13 * Klau_megcsinal_Vallalatiranyitasi_rendszerek_2  + 9 * Klau_megcsinal_Termelesinformatika  + 11 * Klau_megcsinal_Dontestamogato_rendszerek  + 24 * Klau_megcsinal_Vallalati_gazdasagtan  + 12 * Dia_megcsinal_Vallalatiranyirasi_rendszerek_1  + 23 * Dia_megcsinal_Vallalatiranyitasi_rendszerek_2  + 8 * Dia_megcsinal_Termelesinformatika  + 9 * Dia_megcsinal_Dontestamogato_rendszerek  + 34 * Dia_megcsinal_Vallalati_gazdasagtan  + 19 * Gellert_megcsinal_Vallalatiranyirasi_rendszerek_1  + 4 * Gellert_megcsinal_Vallalatiranyitasi_rendszerek_2  + 18 * Gellert_megcsinal_Termelesinformatika  + 19 * Gellert_megcsinal_Dontestamogato_rendszerek  + 14 * Gellert_megcsinal_Vallalati_gazdasagtan ;

end;

