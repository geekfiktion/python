def igpay(name):
    vowels = 'aeiou'
    name = name.lower()
    if name[0] in vowels:
        print(name + "way")
    else:
        print(name[1:] + name[0] + "ay")

igpay("jason")
igpay("apple")
igpay("steph")
