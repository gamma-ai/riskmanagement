target = 53000.00 
print('-proft target:',target)
starting_balance = 50000
current_balance = 49074.18 
sim_balance = 51000
print('-current balance:',current_balance) 
loss = starting_balance - current_balance 
sim_loss = starting_balance-sim_balance
print('-loss:',loss)
total_contracts = 3
print('-total_contracts:',total_contracts) 
contracts = ['cl'] 
print('-contracts:',contracts)
contracts_price = 54.06
print('-contracts_price:',contracts_price)
contracts_tick_value = 10.00 * total_contracts 
print('-contracts_tick_value:',contracts_tick_value) 
new_max_loss = 275 
print('-new_max_loss:',new_max_loss)
if current_balance <starting_balance:
    print('-current balance is Less than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-loss
    print('-current_balance:',current_balance)  
    current_target_loss = target - current_balance
    print('-current loss from target profit:', current_target_loss)
    daily_target = current_target_loss/15
    print('-daily target:',daily_target)
    hourly_target = daily_target*.1
    print('-hourly target',hourly_target)  
    
elif current_balance == starting_balance:
    print('-current balance is Equal than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-loss
    print('-current_balance:',current_balance)  
    current_target_loss = target - current_balance
    print('-current loss from target profit:', current_target_loss)
    daily_target = current_target_loss/15
    print('-daily target:',daily_target)
    hourly_target = daily_target*.1
    print('-hourly target',hourly_target)  
    
elif current_balance >= starting_balance:
    print('-current balance is Greater than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-sim_loss
    print('-current_balance:',current_balance)  
    current_target_loss = target - current_balance
    print('-current loss from target profit:', current_target_loss)
    daily_target = current_target_loss/15
    print('-daily target:',daily_target)
    hourly_target = daily_target*.1
    print('-hourly target',hourly_target)  
