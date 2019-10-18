target = 53000.00
print('-proft target:',target)
starting_balance = 50000
current_balance = 49116.57
sim_balance = 51000
print('-current balance:',current_balance)
loss = starting_balance - current_balance
sim_loss = starting_balance-sim_balance
print('-loss:',loss)
total_contracts = 3
print('-total_contracts:',total_contracts)
# contracts = {'cl':54.06,
#               'es':2980.00,
#               'rty':1526.90}
# print('-contracts:',contracts)
# contracts_price_10 = 54.06
# print('-contracts_price:',contracts_price_10)
max_risk = current_balance*.01
print('----max risk: ${}'.format(max_risk))
contracts_tick_value_12 = 12.50 * total_contracts
contracts_tick_value_10 = 10.00 * total_contracts
contracts_tick_value_5 = 5.00 *total_contracts
print('-contracts_tick_value 12:',contracts_tick_value_12)
print('-contracts_tick_value 10:',contracts_tick_value_10)
print('-contracts_tick_value 5:',contracts_tick_value_5)



if current_balance <starting_balance:
    print('-current balance is Less than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-loss
    print('-current_balance:',current_balance)
    current_target_loss = target - current_balance
    print('-current loss from target profit:', current_target_loss)
    daily_target = current_target_loss/15
    print('-daily target:',daily_target)
    hourly_target = daily_target/4
    print('-hourly target',hourly_target)
#     for contract in contracts:
    print('-Target contract size in each market to reach daily target')
    profit_size12 = daily_target/contracts_tick_value_12
    print('-profit size for $12 tick size:',profit_size12)
    max_loss12 = profit_size12 *.015
    print('max loss:',max_loss12)
    profit_size10 = daily_target/contracts_tick_value_10
    print('-profit size for $10 tick size:',profit_size10)
    max_loss10 = profit_size10 *.015
    print('max loss:',max_loss10)
    profit_size5 = daily_target/contracts_tick_value_5
    print('-profit size for $5 tick size:',profit_size5)
    max_loss5 = profit_size5 *.015
    print('max loss:',max_loss5)

elif current_balance == starting_balance:
    print('-current balance is Equal than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-loss
    print('-current_balance:',current_balance)
    current_target_loss = target - current_balance
    print('-current loss from target profit:', current_target_loss)
    daily_target = current_target_loss/15
    print('-daily target:',daily_target)
    hourly_target = daily_target/4
    print('-hourly target',hourly_target)
#     for contract in contracts:
    print('-Target contract size in each market to reach daily target')
    profit_size12 = daily_target/contracts_tick_value_12
    print('-profit size for $12 tick size:',profit_size12)
    profit_size10 = daily_target/contracts_tick_value_10
    print('-profit size for $10 tick size:',profit_size10)
    profit_size5 = daily_target/contracts_tick_value_5
    print('-profit size for $5 tick size:',profit_size5)

elif current_balance >= starting_balance:
    print('-current balance is Greater than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-sim_loss
    print('-current_balance:',current_balance)
    current_target_loss = target - current_balance
    print('-current loss from target profit:', current_target_loss)
    daily_target = current_target_loss/15
    print('-daily target:',daily_target)
    hourly_target = daily_target/4
    print('-hourly target',hourly_target)
#     for contract in contracts:
    print('-Target contract size in each market to reach daily target')
    profit_size12 = daily_target/contracts_tick_value_12
    print('-profit size for $12 tick size:',profit_size12)
    profit_size10 = daily_target/contracts_tick_value_10
    print('-profit size for $10 tick size:',profit_size10)
    profit_size5 = daily_target/contracts_tick_value_5
    print('-profit size for $5 tick size:',profit_size5)
