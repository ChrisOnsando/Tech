def my_greeting(name, msg, sendoff):
    return("Hello", name + ', ' + msg , ', ' + sendoff)

my_greeting("Chris", "Good morning!", "and have a good day.")

def my_function():
	num1 = 10
	return("The Value is:",num1)
my_function()

def my_number():
	num2 = 20
	return("The Value is:",num2)
my_number()

def add_fish_to_aquarium():
    my_fish = "Shark", "Tuna", "Tilapia", "Mud fish", "Cat Fish", "Dug fish", "Dolphin", "Whale", "Seal", "Turtles"
    if len(my_fish) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"The list is": my_fish}
