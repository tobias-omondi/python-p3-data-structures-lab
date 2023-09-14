spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
# Returns names of each spcy food
def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names

names = get_names(spicy_foods)
print(names)






# returns a list of dict where heat level of food is greater 
def get_spiciest_foods(spicy_foods):
    x = []
    for food in spicy_foods:
       if food ['heat_level'] > 5:
           x.append(food)
           return x
       x = get_spiciest_foods(spicy_foods)
       print (x)




# it output to the terminal should have print():buffalo wings.
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        
        # Create a string of "🌶" emojis based on the heat level
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spicy_foods(spicy_foods)





def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  
american_food = get_spicy_food_by_cuisine(spicy_foods, "American")
print(american_food)

thai_food = get_spicy_food_by_cuisine(spicy_foods, "Thai")
print(thai_food)

def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest.append(food)
    return spiciest




def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)  
    for food in spiciest:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = "🌶" * food['heat_level']  
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

print_spiciest_foods(spicy_foods)




def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return None
    
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return int(average)

average = get_average_heat_level(spicy_foods)
print(average)




def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods



