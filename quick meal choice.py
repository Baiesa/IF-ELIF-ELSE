current_hour = 15
hunger_level = 7

meal = "snack" if current_hour < 17 and hunger_level < 5 else ("full meal")
print(meal)

       