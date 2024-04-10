# introducing library
# from codecarbon import EmissionsTracker
# intialize it
def transport_footprint(transport_method, num_of_ppl):
# customize your function
  if transport_method == 'car':
    transport_carbonft = num_of_ppl * 3.0
  elif transport_method == 'bus':
    transport_carbonft == num_of_ppl * 1.2
  elif transport_method == 'lorry':
    transport_carbonft = num_of_ppl * 0.5
  else:
    transport_carbonft = 0
  
  return transport_carbonft
  
def electricity_footprint(usage):
# customize the function
  if usage is None:
    return 0
  else:
    electric_carbonft = usage * 0.5
    return  electric_carbonft

  
def food_footprint(category, num_of_meals):
# customize the function
  if category == 'beef':
    food_carbonft = num_of_meals * 5.0
  elif category == 'pork':
    food_carbonft = num_of_meals * 3.0
  elif category == 'chicken':
    food_carbonft = num_of_meals * 2.0
  else:
    food_carbonft = num_of_meals * 1.0

  return food_carbonft

# calculate the total individual carbon footprint
def calculate_total_carbon_footprint(transport_method, num_of_ppl, usage, category, num_of_meals):
  individual_transportation_carbon = transport_footprint(transport_method, num_of_ppl)
  individual_electricity_carbon = electricity_footprint(usage)
  individual_food_carbon = food_footprint(category, num_of_meals)

  total_individual_carbon_footprint = individual_transportation_carbon + individual_electricity_carbon + individual_food_carbon
  return total_individual_carbon_footprint

# inputs
transport_method = input('enter your transport method:')
num_of_ppl = float(input('enter the number of people:'))
usage = float(input('enter the electric usage:'))
category = input('enter your food category:')
num_of_meals = float(input('enter the num of meals:'))





total_individual_carbon_footprint = calculate_total_carbon_footprint(transport_method, num_of_ppl, usage, category, num_of_meals)

print("Total Individual Carbon Footprint: {} tons CO2e".format(total_individual_carbon_footprint))

