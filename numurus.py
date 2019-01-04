def to_val(value):
    numuru = {
    "i": 1,
    "v": 5,
    "x": 10,
    "l": 50,
    "c": 100,
    "d": 500,
    "m": 1000,
    }
    for (numu, val) in numuru.items():
        if value == numu:
            return val
            
#    if value == 'i':
#         return 1
#     elif value == 'v':
#         return 5
#     elif value == 'x':
#         return 10
#     elif value == 'l':
#         return 50
#     elif value == 'c':
#         return 100
#     elif value == 'd':
#         return 500
#     elif value == 'm':
#         return 1000

def numurus(roman):
    total = 0
    prev = 0
    roman = roman.lower()
    for r in roman:
        cur = to_val(r)
        if prev < cur:
            total -= prev
            cur -= prev
        total += cur
        prev = cur
    return total

#print(numurus("xx"))
#print(numurus("xxiv"))
roman = input("Enter a roman numeral:  ")

print(numurus(roman))
