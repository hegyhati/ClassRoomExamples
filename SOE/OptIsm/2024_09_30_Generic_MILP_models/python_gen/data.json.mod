var transport_from_Sopron_to_Sopron >= 0;
var transport_from_Sopron_to_Veszprem >= 0;
var transport_from_Sopron_to_Gyor >= 0;
var transport_from_Sopron_to_Pecs >= 0;
var transport_from_Sopron_to_Budapest >= 0;
var transport_from_Sopron_to_Szeged >= 0;
var transport_from_Sopron_to_Debrecen >= 0;
var transport_from_Sopron_to_Miskolc >= 0;
var transport_from_Kobanya_to_Sopron >= 0;
var transport_from_Kobanya_to_Veszprem >= 0;
var transport_from_Kobanya_to_Gyor >= 0;
var transport_from_Kobanya_to_Pecs >= 0;
var transport_from_Kobanya_to_Budapest >= 0;
var transport_from_Kobanya_to_Szeged >= 0;
var transport_from_Kobanya_to_Debrecen >= 0;
var transport_from_Kobanya_to_Miskolc >= 0;
var transport_from_Pecs_to_Sopron >= 0;
var transport_from_Pecs_to_Veszprem >= 0;
var transport_from_Pecs_to_Gyor >= 0;
var transport_from_Pecs_to_Pecs >= 0;
var transport_from_Pecs_to_Budapest >= 0;
var transport_from_Pecs_to_Szeged >= 0;
var transport_from_Pecs_to_Debrecen >= 0;
var transport_from_Pecs_to_Miskolc >= 0;
var transport_from_Nagykanizsa_to_Sopron >= 0;
var transport_from_Nagykanizsa_to_Veszprem >= 0;
var transport_from_Nagykanizsa_to_Gyor >= 0;
var transport_from_Nagykanizsa_to_Pecs >= 0;
var transport_from_Nagykanizsa_to_Budapest >= 0;
var transport_from_Nagykanizsa_to_Szeged >= 0;
var transport_from_Nagykanizsa_to_Debrecen >= 0;
var transport_from_Nagykanizsa_to_Miskolc >= 0;


s.t. Sopron_supply_constraint:
	transport_from_Sopron_to_Sopron + transport_from_Sopron_to_Veszprem + transport_from_Sopron_to_Gyor + transport_from_Sopron_to_Pecs + transport_from_Sopron_to_Budapest + transport_from_Sopron_to_Szeged + transport_from_Sopron_to_Debrecen + transport_from_Sopron_to_Miskolc <= 6000;

s.t. Kobanya_supply_constraint:
	transport_from_Kobanya_to_Sopron + transport_from_Kobanya_to_Veszprem + transport_from_Kobanya_to_Gyor + transport_from_Kobanya_to_Pecs + transport_from_Kobanya_to_Budapest + transport_from_Kobanya_to_Szeged + transport_from_Kobanya_to_Debrecen + transport_from_Kobanya_to_Miskolc <= 12000;

s.t. Pecs_supply_constraint:
	transport_from_Pecs_to_Sopron + transport_from_Pecs_to_Veszprem + transport_from_Pecs_to_Gyor + transport_from_Pecs_to_Pecs + transport_from_Pecs_to_Budapest + transport_from_Pecs_to_Szeged + transport_from_Pecs_to_Debrecen + transport_from_Pecs_to_Miskolc <= 8000;

s.t. Nagykanizsa_supply_constraint:
	transport_from_Nagykanizsa_to_Sopron + transport_from_Nagykanizsa_to_Veszprem + transport_from_Nagykanizsa_to_Gyor + transport_from_Nagykanizsa_to_Pecs + transport_from_Nagykanizsa_to_Budapest + transport_from_Nagykanizsa_to_Szeged + transport_from_Nagykanizsa_to_Debrecen + transport_from_Nagykanizsa_to_Miskolc <= 1000;



s.t. Sopron_demand_constraint:
	transport_from_Sopron_to_Sopron + transport_from_Kobanya_to_Sopron + transport_from_Pecs_to_Sopron + transport_from_Nagykanizsa_to_Sopron >= 500;

s.t. Veszprem_demand_constraint:
	transport_from_Sopron_to_Veszprem + transport_from_Kobanya_to_Veszprem + transport_from_Pecs_to_Veszprem + transport_from_Nagykanizsa_to_Veszprem >= 2000;

s.t. Gyor_demand_constraint:
	transport_from_Sopron_to_Gyor + transport_from_Kobanya_to_Gyor + transport_from_Pecs_to_Gyor + transport_from_Nagykanizsa_to_Gyor >= 1500;

s.t. Pecs_demand_constraint:
	transport_from_Sopron_to_Pecs + transport_from_Kobanya_to_Pecs + transport_from_Pecs_to_Pecs + transport_from_Nagykanizsa_to_Pecs >= 3000;

s.t. Budapest_demand_constraint:
	transport_from_Sopron_to_Budapest + transport_from_Kobanya_to_Budapest + transport_from_Pecs_to_Budapest + transport_from_Nagykanizsa_to_Budapest >= 10000;

s.t. Szeged_demand_constraint:
	transport_from_Sopron_to_Szeged + transport_from_Kobanya_to_Szeged + transport_from_Pecs_to_Szeged + transport_from_Nagykanizsa_to_Szeged >= 4000;

s.t. Debrecen_demand_constraint:
	transport_from_Sopron_to_Debrecen + transport_from_Kobanya_to_Debrecen + transport_from_Pecs_to_Debrecen + transport_from_Nagykanizsa_to_Debrecen >= 3500;

s.t. Miskolc_demand_constraint:
	transport_from_Sopron_to_Miskolc + transport_from_Kobanya_to_Miskolc + transport_from_Pecs_to_Miskolc + transport_from_Nagykanizsa_to_Miskolc >= 2500;



minimize Trasportation_cost: 0 * transport_from_Sopron_to_Sopron + 145 * transport_from_Sopron_to_Veszprem + 90 * transport_from_Sopron_to_Gyor + 275 * transport_from_Sopron_to_Pecs + 220 * transport_from_Sopron_to_Budapest + 390 * transport_from_Sopron_to_Szeged + 450 * transport_from_Sopron_to_Debrecen + 400 * transport_from_Sopron_to_Miskolc + 220 * transport_from_Kobanya_to_Sopron + 125 * transport_from_Kobanya_to_Veszprem + 130 * transport_from_Kobanya_to_Gyor + 200 * transport_from_Kobanya_to_Pecs + 0 * transport_from_Kobanya_to_Budapest + 170 * transport_from_Kobanya_to_Szeged + 220 * transport_from_Kobanya_to_Debrecen + 180 * transport_from_Kobanya_to_Miskolc + 275 * transport_from_Pecs_to_Sopron + 160 * transport_from_Pecs_to_Veszprem + 250 * transport_from_Pecs_to_Gyor + 0 * transport_from_Pecs_to_Pecs + 200 * transport_from_Pecs_to_Budapest + 185 * transport_from_Pecs_to_Szeged + 410 * transport_from_Pecs_to_Debrecen + 425 * transport_from_Pecs_to_Miskolc + 160 * transport_from_Nagykanizsa_to_Sopron + 130 * transport_from_Nagykanizsa_to_Veszprem + 175 * transport_from_Nagykanizsa_to_Gyor + 140 * transport_from_Nagykanizsa_to_Pecs + 210 * transport_from_Nagykanizsa_to_Budapest + 310 * transport_from_Nagykanizsa_to_Szeged + 440 * transport_from_Nagykanizsa_to_Debrecen + 420 * transport_from_Nagykanizsa_to_Miskolc;

end;
