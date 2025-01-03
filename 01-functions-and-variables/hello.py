# Ask user for their name.
# name = input("What's your name?  : ").strip().title();
name = "Foo Bar";
# say hello to user.
print("Hello, " + name);
print("Hello,",name); #Function arguments

"""
Comments: serves as a pseudocode.
print is a function ..that prints Hello, World!! on to screen.
displaying in the screen is a side Effect.
bugs : is a mistake in program.
return values , varaiables
"""
# knowing print function paramenters
print("Hello, ", end="???");
print(name);
print(f"Hello, {name}");


# string --> str
 
    #  Remove white space from string
# name = name.strip();
# name = name.capitalize();
# name = name.title();
name = name.strip().title();
# Split users name into firstName and lastName
firstName, lastName = name.split(" ");
print(f"Hello, {name}");
print(firstName);
print(lastName);

"""
Integers : int
"""
# Operators
#    + - * / %
x = input("x: ");
y = input("y: ");

z = int(x) + int(y);
print(z);