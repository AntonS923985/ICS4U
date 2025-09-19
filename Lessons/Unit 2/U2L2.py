inches = 10 ** 12
(feet, inches) = divmod(inches, 12)
(yards, feet) = divmod(feet, 3)
(miles, yards) = divmod(yards, 1760)
(moon, miles) = divmod(miles, 238855)

print("One trillion inches is the same as going to the moon and back %d  times, plus an extra  %d  miles,  %d  yards,  %d  feet,  and  %d  inches." % (moon, miles, yards, feet, inches))

def toLower(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        return chr(ord(letter) + 32)
    print("The letter is not uppercase.")
    return " "

print(toLower('A'))
print(toLower('a'))
