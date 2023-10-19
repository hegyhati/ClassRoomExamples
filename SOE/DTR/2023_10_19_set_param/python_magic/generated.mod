var transport_Sopron_Sopron >= 0;
var transport_Sopron_Veszprem >= 0;
var transport_Sopron_Gyor >= 0;
var transport_Sopron_Pecs >= 0;
var transport_Sopron_Szombathely >= 0;
var transport_Pecs_Sopron >= 0;
var transport_Pecs_Veszprem >= 0;
var transport_Pecs_Gyor >= 0;
var transport_Pecs_Pecs >= 0;
var transport_Pecs_Szombathely >= 0;
var transport_Nagykanizsa_Sopron >= 0;
var transport_Nagykanizsa_Veszprem >= 0;
var transport_Nagykanizsa_Gyor >= 0;
var transport_Nagykanizsa_Pecs >= 0;
var transport_Nagykanizsa_Szombathely >= 0;


s.t. Max_supply_at_Sopron:
	transport_Sopron_Sopron + transport_Sopron_Veszprem + transport_Sopron_Gyor + transport_Sopron_Pecs + transport_Sopron_Szombathely <= 1000;
s.t. Max_supply_at_Pecs:
	transport_Pecs_Sopron + transport_Pecs_Veszprem + transport_Pecs_Gyor + transport_Pecs_Pecs + transport_Pecs_Szombathely <= 500;
s.t. Max_supply_at_Nagykanizsa:
	transport_Nagykanizsa_Sopron + transport_Nagykanizsa_Veszprem + transport_Nagykanizsa_Gyor + transport_Nagykanizsa_Pecs + transport_Nagykanizsa_Szombathely <= 200;


s.t. Min_demand_at_Sopron:
	transport_Sopron_Sopron + transport_Pecs_Sopron + transport_Nagykanizsa_Sopron >= 250;
s.t. Min_demand_at_Veszprem:
	transport_Sopron_Veszprem + transport_Pecs_Veszprem + transport_Nagykanizsa_Veszprem >= 350;
s.t. Min_demand_at_Gyor:
	transport_Sopron_Gyor + transport_Pecs_Gyor + transport_Nagykanizsa_Gyor >= 500;
s.t. Min_demand_at_Pecs:
	transport_Sopron_Pecs + transport_Pecs_Pecs + transport_Nagykanizsa_Pecs >= 500;
s.t. Min_demand_at_Szombathely:
	transport_Sopron_Szombathely + transport_Pecs_Szombathely + transport_Nagykanizsa_Szombathely >= 100;


minimize Transportation_cost:
	0 * transport_Sopron_Sopron + 350 * transport_Pecs_Sopron + 200 * transport_Nagykanizsa_Sopron + 150 * transport_Sopron_Veszprem + 250 * transport_Pecs_Veszprem + 140 * transport_Nagykanizsa_Veszprem + 80 * transport_Sopron_Gyor + 300 * transport_Pecs_Gyor + 220 * transport_Nagykanizsa_Gyor + 380 * transport_Sopron_Pecs + 0 * transport_Pecs_Pecs + 150 * transport_Nagykanizsa_Pecs + 70 * transport_Sopron_Szombathely + 280 * transport_Pecs_Szombathely + 90 * transport_Nagykanizsa_Szombathely;
