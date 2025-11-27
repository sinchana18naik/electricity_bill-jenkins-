import sys
if len(sys.argv) == 2:
    units = float(sys.argv[1])
    print("User provided units:")
else:
    units = 120
    print("No input given - using default units:")

bill = units * 5

print("Electricity Bill:", bill)
