###1 quater = 25 cents,1
# 1 Dime = 10 cents
# 1 nickel = 5 cents.
# 1 penny = 1 cent
###

def finding_coins(cents):
    Dime = cents/10
    Quater = cents/25
    nickel = cents/5
    penny = cents/1
    print(f"Dime ={Dime}, Quater={Quater}, nickel={nickel}, penny={penny}")


finding_coins(55)