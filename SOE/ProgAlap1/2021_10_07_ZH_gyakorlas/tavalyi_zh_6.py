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
annual_call_minutes, annual_message_count = input_annual_usage(month_count)
minute_price,  message_price, monthly_base_fee = input_tariff_fees()
annual_cost = annual_cost_calculation(month_count, annual_call_minutes, annual_message_count,minute_price,message_price, monthly_base_fee)


print("Your total bill for calling is: ", annual_cost)
