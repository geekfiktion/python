def intersect(list1, list2):

    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                print(str(l1) + ' ' + str(l2))

    print("\n")




def pair(list1, list2):

    for l in range(len(list1)):
        print(str(list1[l]) + ', ' + str(list2[l]))

    print()
    for (l1, l2) in zip(list1, list2):
        print("{0}, {1}".format(l1, l2))

num1 = [1, 2, 3, 4, 5, 6, 7]
num2 = [1, 2, 3, 4, 7, 8, 9, 10]
fruits = [ "Apples", "Oranges", "Tomatoes"]
veggies = [ "Carrots", "Peas", "Tomatoes"]

#intersect(num1, num2)
#print()
#intersect(fruits, veggies)
#print()
pair(num1, num2)
print()
pair(fruits, veggies)
