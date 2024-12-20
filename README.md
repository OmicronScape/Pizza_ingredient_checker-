# Pizza_ingredient_checker-
Program that checks which pizzas have the requested ingredients.  It defines a list of available ingredients and a set of pizzas with their respective ingredients.  The program then answers several questions about which pizzas contain specific combinations of ingredients.

README: Pizza Ingredient Checker Program

Overview

This Python program helps identify pizzas from a menu that match specific ingredient criteria. Each pizza's ingredients are represented as sets, and the program uses set operations to filter pizzas based on various questions.

Features

The program answers the following questions:

Which pizzas have gouda cheese, tomato sauce, and vegetables?

Which pizzas have gouda cheese, tomato sauce, and either chicken or cold cuts?

Which pizzas have gouda cheese, chicken but not tomato sauce?

Which pizzas have gouda cheese, vegetables, and carbonara sauce?

Which pizzas have gouda cheese and either cold cuts or mushrooms but not both?

How It Works

Ingredients

The program uses a list of ingredients:

ingredients = ["gouda", "tomato_sauce", "carbonara_sauce", "cold_cut", "chicken", "mushrooms", "vegetables"]

Each pizza is defined as a set of ingredients:

p1 = {ingredients[0], ingredients[1], ingredients[3], ingredients[5]} # Example: gouda, tomato sauce, cold cut, mushrooms

Pizza List

All pizzas are stored in a list:

pizzas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

Query Logic

For each question, the program:

Defines the required ingredients as a set.

Uses a list comprehension with issubset to check if the required ingredients are present in each pizza.

Returns a list of matching pizzas by their identifiers (e.g., p1, p2).

Example Output

For each question, the program prints the results:

Question 1

Input: Gouda cheese, tomato sauce, and vegetables.

Output:

[Question 1]: The pizzas with gouda cheese, tomato sauce, and vegetables are:
Pizza p6 and pizza p7

Question 5

Input: Gouda cheese and either cold cuts or mushrooms, but not both.

Output:

[Question 5]: The pizzas with gouda cheese and either cold cuts or mushrooms but not both are:
Pizzas p4, p9

Error Handling

If no pizzas match the criteria, the program outputs:

No pizzas found with these ingredients

Requirements

Python 3.x

How to Run

Copy the code into a Python IDE or text editor.

Run the program.

View the results for each question in the terminal.

Notes

The program assumes all pizzas contain gouda cheese as a base ingredient.

Logical operators like issubset and XOR (^) are used for subset and exclusive-or checks, respectively.

Feel free to modify the ingredients list or the pizzas' ingredients to suit your needs.
