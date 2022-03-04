# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, something):
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']
    
def is_in_drink(drink):
    return('strawberry milkshake' in drink)

def make_drink(drink, addons):
    mix = []
    if is_in_drink(drink):
        mix = mixer_ice_with_cream()
        mix = add(mix, 'strawberry')
    else:
        mix = add(mix, 'coffee')
    mix = add(mix, addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk','sugar'])
print(final_drink)
