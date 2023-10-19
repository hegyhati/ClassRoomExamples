\* Problem: clever *\

Minimize
 Transportation_cost: + 150 transport(Sopron,Veszprem)
 + 80 transport(Sopron,Gyor) + 380 transport(Sopron,Pecs)
 + 70 transport(Sopron,Szombathely) + 350 transport(Pecs,Sopron)
 + 250 transport(Pecs,Veszprem) + 300 transport(Pecs,Gyor)
 + 280 transport(Pecs,Szombathely) + 200 transport(Nagykanizsa,Sopron)
 + 140 transport(Nagykanizsa,Veszprem) + 220 transport(Nagykanizsa,Gyor)
 + 150 transport(Nagykanizsa,Pecs)
 + 90 transport(Nagykanizsa,Szombathely)

Subject To
 Max_Supply(Sopron): + transport(Sopron,Sopron)
 + transport(Sopron,Veszprem) + transport(Sopron,Gyor)
 + transport(Sopron,Pecs) + transport(Sopron,Szombathely) <= 1000
 Max_Supply(Pecs): + transport(Pecs,Sopron) + transport(Pecs,Veszprem)
 + transport(Pecs,Gyor) + transport(Pecs,Pecs)
 + transport(Pecs,Szombathely) <= 500
 Max_Supply(Nagykanizsa): + transport(Nagykanizsa,Sopron)
 + transport(Nagykanizsa,Veszprem) + transport(Nagykanizsa,Gyor)
 + transport(Nagykanizsa,Pecs) + transport(Nagykanizsa,Szombathely)
 <= 200
 Min_Demand(Sopron): + transport(Sopron,Sopron) + transport(Pecs,Sopron)
 + transport(Nagykanizsa,Sopron) >= 250
 Min_Demand(Veszprem): + transport(Sopron,Veszprem)
 + transport(Pecs,Veszprem) + transport(Nagykanizsa,Veszprem) >= 350
 Min_Demand(Gyor): + transport(Sopron,Gyor) + transport(Pecs,Gyor)
 + transport(Nagykanizsa,Gyor) >= 500
 Min_Demand(Pecs): + transport(Sopron,Pecs) + transport(Pecs,Pecs)
 + transport(Nagykanizsa,Pecs) >= 500
 Min_Demand(Szombathely): + transport(Sopron,Szombathely)
 + transport(Pecs,Szombathely) + transport(Nagykanizsa,Szombathely)
 >= 100

End
