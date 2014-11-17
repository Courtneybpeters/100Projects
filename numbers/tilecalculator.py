# Calculate the cost to tile aroom (or any flooring for that matter.)

print "Use this program to calculate the cost of flooring a room.", '\n'

price = float(raw_input("Please enter the cost of the material/square foot: "))

width = float(raw_input("Width of the room: "))
height = float(raw_input("Length of the room: "))

cost =(width * height) * price

print "The cost to floor this room would be: $%r" % round(cost, 2)
