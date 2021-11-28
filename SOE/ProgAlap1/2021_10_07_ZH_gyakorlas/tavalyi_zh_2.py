call_minutes = int(input("How many minutes of calls did you have? "))
message_count = int(input("How many SMSs did you send? "))
minute_price = int(input("How much does a minute of call cost you? "))
message_price = int(input("How much does an SMS cost you? "))

cost = call_minutes * minute_price + message_count * message_price

print("Your total bill for calling is: ", cost)
