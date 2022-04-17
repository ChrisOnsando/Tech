def my_func():
	num1 = 10
	print("The Value is:",num1)
my_func()

def my_number():
	num2 = 20
	return("The Value is:",num2)
my_number()

def greet(name, msg, sendoff):
    print("Hello", name + ', ' + msg , ', ' + sendoff)

greet("Chris", "Good morning!", "and have a good day.")

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"The list is": fish_list}