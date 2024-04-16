var Kapuvar_to_Sopron >= 0;
var Kapuvar_to_Gyor >= 0;
var Kapuvar_to_Budapest >= 0;
var Kapuvar_to_Nagykanizsa >= 0;

var Sarvar_to_Sopron >= 0;
var Sarvar_to_Gyor >= 0;
var Sarvar_to_Budapest >= 0;
var Sarvar_to_Nagykanizsa >= 0;

var Kaposvar_to_Sopron >= 0;
var Kaposvar_to_Gyor >= 0;
var Kaposvar_to_Budapest >= 0;
var Kaposvar_to_Nagykanizsa >= 0;

s.t. Kapuvar_supply:
     Kapuvar_to_Sopron +
     Kapuvar_to_Gyor + 
     Kapuvar_to_Budapest +
     Kapuvar_to_Nagykanizsa <= 75;

s.t. Sarvar_supply:
     Sarvar_to_Sopron +
     Sarvar_to_Gyor + 
     Sarvar_to_Budapest +
     Sarvar_to_Nagykanizsa <= 125;

s.t. Kaposvar_supply:
     Kaposvar_to_Sopron +
     Kaposvar_to_Gyor + 
     Kaposvar_to_Budapest +
     Kaposvar_to_Nagykanizsa <= 150;

s.t. Sopron_demand:
      Kapuvar_to_Sopron +
       Sarvar_to_Sopron +
     Kaposvar_to_Sopron >= 30;


s.t. Gyor_demand:
      Kapuvar_to_Gyor +
       Sarvar_to_Gyor +
     Kaposvar_to_Gyor >= 60;


s.t. Budapest_demand:
      Kapuvar_to_Budapest +
       Sarvar_to_Budapest +
     Kaposvar_to_Budapest >= 120;


s.t. Nagykanizsa_demand:
      Kapuvar_to_Nagykanizsa +
       Sarvar_to_Nagykanizsa +
     Kaposvar_to_Nagykanizsa >= 40;

minimize Transportation_cost :
    30  * Kapuvar_to_Sopron + 40  * Kapuvar_to_Gyor + 170 * Kapuvar_to_Budapest + 150 * Kapuvar_to_Nagykanizsa + 
    80  * Sarvar_to_Sopron + 100  * Sarvar_to_Gyor + 200 * Sarvar_to_Budapest + 110 * Sarvar_to_Nagykanizsa + 
    240  * Kaposvar_to_Sopron + 210  * Kaposvar_to_Gyor + 180 * Kaposvar_to_Budapest + 70 * Kaposvar_to_Nagykanizsa; 