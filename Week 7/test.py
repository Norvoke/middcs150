colors = {'fish':'orange', 'rocks':'gray', 'water':'blue', 'bubbles':'white'}

colors['fish'] = colors.get('fish', 'red')
print(colors['fish'])