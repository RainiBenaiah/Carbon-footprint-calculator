
# def transport_footprint(transport_method, distance):

#   if transport_method == 'car':
#     transport_carbonft = distance * 1.5
#   elif transport_method == 'bus':
#     transport_carbonft == distance * 1.0
#   elif transport_method == 'lorry':
#     transport_carbonft = distance * 2.5
#   else:
#     transport_carbonft = 0
  
#   return transport_carbonft
  
# def electricity_footprint(usage):

#   if usage is None:
#     return 0
#   else:
#     electric_carbonft = usage * 0.5
#     return  electric_carbonft

  
# def food_footprint(category, num_of_meals):

#   if category == 'beef':
#     food_carbonft = num_of_meals * 2.5
#   elif category == 'pork':
#     food_carbonft = num_of_meals * 1.8
#   elif category == 'chicken':
#     food_carbonft = num_of_meals * 1.2
#   else:
#     food_carbonft = num_of_meals * 1.0

#   return food_carbonft

# def calculate_total_carbon_footprint(transport_method, distance, usage, category, num_of_meals):
#   individual_transportation_carbon = transport_footprint(transport_method, distance)
#   individual_electricity_carbon = electricity_footprint(usage)
#   individual_food_carbon = food_footprint(category, num_of_meals)

#   total_individual_carbon_footprint = individual_transportation_carbon + individual_electricity_carbon + individual_food_carbon
#   return total_individual_carbon_footprint

# # inputs
# transport_method = input('enter your transport method:')
# distance = float(input('enter the distance covered:'))
# usage = float(input('enter the electric usage:'))
# category = input('enter your food category:')
# num_of_meals = float(input('enter the num of meals:'))





# total_individual_carbon_footprint = calculate_total_carbon_footprint(transport_method, distance, usage, category, num_of_meals)

# print("Total Individual Carbon Footprint: {} tons CO2e".format(total_individual_carbon_footprint))

