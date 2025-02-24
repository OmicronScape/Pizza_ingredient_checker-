# Program that checks which pizzas have the requested ingredients.

# List of available ingredients.
ingridients = ["gouda", "tomato_sauce", "carbonara_sauce", "cold_cut", "chicken", "mushrooms", "vegetables"]

# Each pizza with its ingredients from the list (ingridients) we created.
p1 = {ingridients[0], ingridients[1], ingridients[3], ingridients[5]}
p2 = {ingridients[0], ingridients[1], ingridients[3], ingridients[5]}
p3 = {ingridients[0], ingridients[1], ingridients[3], ingridients[5]}
p4 = {ingridients[0], ingridients[1], ingridients[3]}
p5 = {ingridients[0], ingridients[1], ingridients[4]}
p6 = {ingridients[0], ingridients[1], ingridients[6]}
p7 = {ingridients[0], ingridients[1], ingridients[6]}
p8 = {ingridients[0], ingridients[1]}
p9 = {ingridients[0], ingridients[2], ingridients[3]}
p10 = {ingridients[0], ingridients[2], ingridients[4], ingridients[5]}

# List of pizzas.
pizzas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------|
#-----------------------------------------------------------------------------------------------------------------------------------------------------------|
# General instructions for all sub-questions:                                                                                                               |
# ---Create a set with the ingredients of the question (question).                                                                                          |
# ---Create a list (solution) that contains the names of the pizzas that meet the criteria of the question (the solution method is inside the list).        |
# ---Use a list of pizzas (p1, p2, ...) that we have to check if the ingredients of the question are a subset of the ingredients of the pizza.              |
# ---f"p{i+1}" creates the name of the pizza (e.g., "p1", "p2") by adding 1 to the index.                                                                   |
# ---If the subset of the ingredients of the question is a subset of the ingredients of the pizza, then we add the pizza to the solution list (solution).   |
# ---Enumerate(pizzas) returns pairs (index, pizza) for each pizza in the list (index is the position number of an element in a list. It starts from 0).    |
# ---We use the issubset method of sets to check if the ingredients of the question (question) are a subset of the ingredients of the pizza.              
#   |
#-----------------------------------------------------------------------------------------------------------------------------------------------------------|
#-----------------------------------------------------------------------------------------------------------------------------------------------------------|


question1 = {ingridients[0], ingridients[1], ingridients[6]}
solution1 = [f"p{i+1}" for i, pizza in enumerate(pizzas) if question1.issubset(pizza)]

print("[Question 1]: The pizzas with gouda cheese, tomato sauce, and vegetables are:")
if solution1:
    print("Pizza", " and pizza ".join(solution1)) 
else:
    print("No pizzas found with these ingredients")


question2 = {ingridients[0], ingridients[1]}
solution2 = [f"p{i+1}" for i, pizza in enumerate(pizzas) if question2.issubset(pizza) and (ingridients[3] in pizza or ingridients[4] in pizza)]

print("\n[Question 2]: The pizzas with gouda cheese, tomato sauce, and either chicken or cold cuts are:")
if solution2:
    print("Pizzas", ", ".join(solution2), "!", "You have many options!") 
else:
    print("No pizzas found with these ingredients")


solution3 = [f"p{i+1}" for i, pizza in enumerate(pizzas) if question3.issubset(pizza) and ingridients[1] not in pizza]

print("\n[Question 3]: The pizzas with gouda cheese, chicken but not tomato sauce are:")
if solution3:
    print("Pizza", ", ".join(solution3)) 
else:
    print("No pizzas found with these ingredients")


question4 = {ingridients[0], ingridients[2], ingridients[6]}
solution4 = [f"p{i+1}" for i, pizza in enumerate(pizzas) if question4.issubset(pizza)]

print("\n[Question 4]: The pizzas with gouda cheese, vegetables, and carbonara sauce are:")
if solution4:
    print(", ".join(solution4)) 
else:
    print("No pizzas found with these ingredients!")


question5 = {ingridients[0]}
solution5 = [f"p{i+1}" for i, pizza in enumerate(pizzas) if question5.issubset(pizza) and ((ingridients[3] in pizza) ^ (ingridients[5] in pizza))]

print("\n[Question 5]: The pizzas with gouda cheese and either cold cuts or mushrooms but not both are:")
if solution5:
    print("Pizzas", ", ".join(solution5)) 
else:
    print("No pizzas found with these ingredients")

#-----------------------------------------------------------------------------------------------------------------------------------------------------|
# ----------------------------------------------------------------------------------------------------------------------------------------------------|
#-----------------------------------------------------***END OF PROGRAM***------------------------------------------------------------------------|
