secretz = [(1, 2), (2, 3), (8, 13), (4, 29), (130, 191), (343, 397), (652, 691), (858, 1009), (689, 2039), (1184, 4099), (2027, 7001), (5119, 10009), (15165, 19997), (15340, 30013), (29303, 70009), (42873, 160009), (158045, 200009)]

num, n = 0, 1
for (r, m) in secretz:
    n *= m
for (r, m) in secretz:
    left = (n/m) % m
    mul = -1
    for x in range(m):
        if (left * x) % m == r:
            mul = x
            break
    if mul != -1:
        num += (n/m) * mul

num2 = (200009-1)*(160009-1)

print "Congratulations! The flag is: %s_%s" % (num, str(num2))
