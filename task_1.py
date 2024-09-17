import math

num_1 = 3
num_2 = 6

res = num_1 + num_2

print (res)


is_even = True
is_odd = False

and_operation = is_even and is_odd
or_operation = is_even or is_odd
not_even = not is_even
not_odd = not is_odd

print(f"is_even and is_odd: {and_operation}")
print(f"is_even or is_odd: {or_operation}")
print(f"not is_even: {not_even}")
print(f"not is_odd: {not_odd}")


x = 2.735
z = 7.218

sqrt_res = math.sin(x) * math.cos(x)

res = ( (z + x) / math.cos(x) + sqrt_res ) ** 2 + 16 * z

print (res)