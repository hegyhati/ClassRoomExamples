def input_mothly_usage(month):
    print("Month",month,":")
    call_minutes = int(input(" How many minutes of calls did you have? "))
    message_count = int(input(" How many SMSs did you send? "))
    return call_minutes, message_count

def input_annual_usage(month_count):
    annual_call_minutes = []
    annual_message_count = []
    for month in range(1,month_count+1):
        call_minutes, message_count = input_mothly_usage(month)
        annual_call_minutes.append(call_minutes)
        annual_message_count.append(message_count)
    return annual_call_minutes, annual_message_count

def input_tariff_fees():
    print("Tariff fees:")
    minute_price = int(input(" How much does a minute of call cost you? "))
    message_price = int(input( " How much does an SMS cost you? "))
    monthly_base_fee = int(input(" How much is your monthly base fee? "))
    return minute_price,message_price,monthly_base_fee

def month_cost_calculation(call_minutes,message_count,minute_price,message_price, monthly_base_fee):
    month_cost = call_minutes * minute_price + message_count * message_price
    if month_cost < monthly_base_fee:
        month_cost = monthly_base_fee

def annual_cost_calculation(month_count, annual_call_minutes, annual_message_count,minute_price,message_price, monthly_base_fee):
    annual_cost=0
    for month in range(month_count):
        annual_cost += month_cost_calculation(annual_call_minutes[month],annual_message_count[month],minute_price,message_price, monthly_base_fee)
    return annual_cost


month_count = 2
call_minutes, message_count = input_annual_usage(month_count)

minute_price_1,  message_price_1, monthly_base_fee_1 = input_tariff_fees(1)
minute_price_2,  message_price_2, monthly_base_fee_2 = input_tariff_fees(2)


annual_cost_1 = annual_cost_calculation(month_count, call_minutes, 
message_count,minute_price_1,message_price_1, monthly_base_fee_1)
annual_cost_2 = annual_cost_calculation(month_count, call_minutes, 
message_count,minute_price_2,message_price_2, monthly_base_fee_2)

if annual_cost_1 < annual_cost_2:
    print("Tariff 1 is better: ",annual_cost_1)
else:
    print("Tariff 2 is better: ",annual_cost_2)
