def input_mothly_usage(month):
    print("Month",month,":")
    call_minutes = int(input(" How many minutes of calls did you have? "))
    message_count = int(input(" How many SMSs did you send? "))
    return {"minutes": call_minutes, "sms" : message_count}

def input_annual_usage(month_count):
    annual_usage = []
    for month in range(1,month_count+1):
        month_usage = input_mothly_usage(month)
        annual_usage.append(month_usage)
    return annual_usage

def input_tariff_fees():
    print("Tariff fees:")
    minute_price = int(input(" How much does a minute of call cost you? "))
    message_price = int(input( " How much does an SMS cost you? "))
    monthly_base_fee = int(input(" How much is your monthly base fee? "))
    return {
        "minute_price": minute_price,
        "message_price": message_price,
        "base_fee": monthly_base_fee
    }

def month_cost_calculation(usage,tariff):
    month_cost = usage["minutes"] * tariff["minute_price"] + usage["sms"] * tariff["message_price"]
    if month_cost < tariff["base_fee"]:
        month_cost = tariff["base_fee"]
    return month_cost

def annual_cost_calculation(annual_usage,tariff):
    annual_cost=0
    for month_usage in annual_usage:
        annual_cost += month_cost_calculation(month_usage,tariff)
    return annual_cost


month_count = 2
annual_usage = input_annual_usage(month_count)

tariff1 = input_tariff_fees(1)
tariff2 = input_tariff_fees(2)


annual_cost_1 = annual_cost_calculation(annual_usage,tariff1)
annual_cost_2 = annual_cost_calculation(annual_usage,tariff2)

if annual_cost_1 < annual_cost_2:
    print("Tariff 1 is better: ",annual_cost_1)
else:
    print("Tariff 2 is better: ",annual_cost_2)
