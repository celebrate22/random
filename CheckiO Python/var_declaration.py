"""
1. In this very first mission you just need to help our bunch of cyborgs to make friends! Look at the example in the editor, declare two variables robots, droids and set their values to integers 2, 5 respectively. If you have any trouble, look at the hints below the description.

2. When done, try to set values for variables from the previous paragraph in a single line like var1, var2 = value1, value2 (first variable gets first value etc.).

While Python remains a dynamically typed language, meaning you don't have to specify types for variables, incorporating type annotations, especially in larger projects or when working in a team, can significantly enhance code quality and maintainability. It's worth noting that type annotations are optional, and Python will not enforce strict typing; they serve primarily as a development aid and documentation tool.

3. For integers use int type. Try to rewrite the task from the first paragraph with type annotations. 
"""
# 1. Declaring variable and setting their values
cyborgs = 10
# write your code here
robots = 2
droids = 5


# 2. Setting values for variables in a single line
# write your code here
robots, droids = 2, 5


# 3. Declaring with type annotation
cyborgs: int = 10

# write your code here
robots: int = 2
droids: int = 5
