common = (2/5)
common2 = 1/(2+common)
common3 = 1/(2+common2)
common4 = 1/(2+common3)
# The above is the function for finding the repeated fraction

print(1 + common, 1 + common2, 1 + common3, 1 + common4)
# adding 1 at the nth iteration give the final sum

# common - numer: 2, denom: 5
# common2 - numer: 5, denom: 12
# common3 - numer: 12, denom: 29
# common4 - numer: 29, denom: 70

old_num = 1
old_dem = 2

# returns separate new numerator and new denominator or fractional part


def new_frac(old_num, old_dem):
    new_num = old_dem
    new_dem = 2 * old_dem + old_num

    return (new_num, new_dem)


count = 0
it = 0
while (it <= 1000):
    if (len(str(old_num + old_dem)) > len(str(old_dem))):
        count += 1
    (old_num, old_dem) = new_frac(old_num, old_dem)
    it += 1

print(count)
