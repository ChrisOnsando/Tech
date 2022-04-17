import json

a ={"name":"CHRIS",
"age":21,
	"Salary":20000}

# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print(b)

# list conversion to Array
print(json.dumps(['Welcome', "to", "MY GITHUB"]))

# tuple conversion to Array
print(json.dumps(("Welcome", "to", "MY GITHUB")))

# string conversion to String
print(json.dumps("Hi"))


