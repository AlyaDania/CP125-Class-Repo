# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient_calculate (one_way_km,bugdet):
    total_distance = one_way_km * 2
    litres = total_distance / 10
    total_cost = litres * 2.00

    if total_cost <= bugdet:
        return True
    else:
        return False
print(is_budget_sufficient_calculate(100,39))

