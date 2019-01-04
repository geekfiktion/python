prem_ground_ship = 125.00

def ground_shipping(weight):
  flat_charge = 20.00
  if weight <= 2:
    cost = (weight * 1.50)
  elif weight <= 6:
    cost = (weight * 3.00)
  elif weight <= 10:
    cost = (weight * 4.00)
  else:
    cost = (weight * 4.75)
  return cost + flat_charge


def drone_shipping(weight):
  flat_charge = 0.00
  if weight <= 2:
    cost = (weight * 4.50)
  elif weight <= 6:
    cost = (weight * 9.00)
  elif weight <= 10:
    cost = (weight * 12.00)
  else:
    cost = (weight * 14.25)
  return cost

def print_ship_and_cost(method, cost):
  print("The cheapest option available is $%.2f with the %s shipping method." % (cost, method))

def best_ship_method(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if ground > drone and prem_ground_ship > drone:
    print_ship_and_cost("Drone", drone)
  elif drone > ground and prem_ground_ship > ground:
    print_ship_and_cost("Ground", ground)
  else:
    print_ship_and_cost("Premium Ground", prem_ground_ship)
#def best_ship_method(weight):
#  if ground_shipping(weight) > drone_shipping(weight) and prem_ground_ship > drone_shipping(weight):
#    return "You're shipping method is Drone Shipping at the cost of: $" + str(drone_shipping(weight)) + ".  Ground shipping would be: $" + str(ground_shipping(weight))
#  elif drone_shipping(weight) > ground_shipping(weight) and prem_ground_ship > ground_shipping(weight):
#    return "You're shipping method is Ground Shipping at the cost of: $" + str(ground_shipping(weight)) + ".  Drone shipping would be: $" + str(drone_shipping(weight))
#  else:
#    return "You're shipping method is Premium Ground Shipping at the cost of: $" + str(prem_ground_ship)

#print(ground_shipping(8.4))
#print(drone_shipping(1.5))

#print(best_ship_method(4.8))
#print(best_ship_method(41.5))

best_ship_method(4.8)
best_ship_method(41.5)
