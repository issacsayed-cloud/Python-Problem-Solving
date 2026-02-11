# Program to create two sets and perform union & intersection manually

# Sample sets representing ages of males and females in VIT AP
male_ages = {18, 19, 20, 21, 22, 23}
female_ages = {20, 21, 22, 24, 25}

# Manual Union (without using | or union())
def manual_union(set1, set2):
    result = set()
    for elem in set1:
        result.add(elem)
    for elem in set2:
        if elem not in result:
            result.add(elem)
    return result

# Manual Intersection (without using & or intersection())
def manual_intersection(set1, set2):
    result = set()
    for elem in set1:
        if elem in set2:
            result.add(elem)
    return result

# Perform operations
union_result = manual_union(male_ages, female_ages)
intersection_result = manual_intersection(male_ages, female_ages)

# Display results
print("Male Ages:", male_ages)
print("Female Ages:", female_ages)
print("Union of Ages:", union_result)
print("Intersection of Ages:", intersection_result)