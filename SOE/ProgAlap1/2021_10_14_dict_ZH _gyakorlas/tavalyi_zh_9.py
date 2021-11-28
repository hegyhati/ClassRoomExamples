def input_mothly_usage(month):
    print("Month",month,":")
    return {
        "minutes": int(input(" How many minutes of calls did you have? ")), 
        "sms" : int(input(" How many SMSs did you send? "))
    }

def input_annual_usage(month_count):
    annual_usage = []
    for month in range(1,month_count+1):
        annual_usage.append(input_mothly_usage(month))
    return annual_usage

def input_tariff_fees():
    print("Tariff fees:")
    return {
        "minute_price": int(input(" How much does a minute of call cost you? ")),
        "message_price": int(input( " How much does an SMS cost you? ")),
        "base_fee": int(input(" How much is your monthly base fee? "))
    }

def month_cost_calculation(usage,tariff):
    month_cost = usage["minutes"] * tariff["minute_price"] + usage["sms"] * tariff["message_price"]
    if month_cost < tariff["base_fee"]:
        return tariff["base_fee"]
    return month_cost

def annual_cost_calculation(annual_usage,tariff):
    annual_cost=0
    for month_usage in annual_usage:
        annual_cost += month_cost_calculation(month_usage,tariff)
    return annual_cost


month_count = 12
annual_usage = input_annual_usage(month_count)

tariff_count = 4
tariffs = []
for i in range(tariff_count):
    tariffs.append(input_tariff_fees(i+1))

annual_costs = []
for i in range(tariff_count):
    annual_costs.append(annual_cost_calculation(annual_usage,tariffs[i]))

min = 0
for i in range(1,tariff_count):
    if annual_costs[i] < annual_costs[0]:
        min = i

print("A legolcsobb a ", min+1,". tarifa volna: ",annual_costs[min],"Ft")



