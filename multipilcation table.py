for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        if product == 50:
            continue
        if product > 72:
            break
        print(i, "x", j, "=", product)