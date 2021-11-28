annual_call_minutes = []
annual_message_count = []
month_count = 12

for month in range(1,month_count+1):
    print("Month",month,":")
    annual_call_minutes.append(int(input(" How many minutes of calls did you have? ")))
    annual_message_count.append(int(input(" How many SMSs did you send? ")))

print("Tariff fees:")
minute_price = int(input(" How much does a minute of call cost you? "))
message_price = int(input( " How much does an SMS cost you? "))
monthly_base_fee = int(input(" How much is your monthly base fee? "))

annual_cost=0
for month in range(month_count):
    month_cost = annual_call_minutes[month] * minute_price + annual_message_count[month] * message_price
    if month_cost < monthly_base_fee:
        month_cost = monthly_base_fee
    annual_cost+=month_cost

print("Your total bill for calling is: ", annual_cost)
