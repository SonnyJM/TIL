numbers = [
    {'가' : 30, '나' : 135, '다' : 30},
    {'가' : 20, '나' : 120, '다' : 30},
    {'가' : 10, '나' : 76, '다' : 30},
    {'가' : 60, '나' : 535, '다' : 30},
    ]
sorted(numbers, key=lambda x: x['가'])

print(numbers)