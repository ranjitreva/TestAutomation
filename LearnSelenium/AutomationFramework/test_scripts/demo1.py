from pyjavaproperties import Properties

# Create object of Properties class
property_file = Properties()

# Open the property file
property_file.load(open("../config.properties"))

# Get the value by specifying the key
value = property_file['city']
print(value)






