computers = {"Google": "Chromebook", "Apple": "Macbook", "Microsoft": "Surface Pro"}

# if 'Lenovo' not in computers:
#     computers['Lenovo'] = 'Thinkpad'
    
# print(computers)

computers.setdefault('Lenovo', 'Thinkpad')
print(computers)