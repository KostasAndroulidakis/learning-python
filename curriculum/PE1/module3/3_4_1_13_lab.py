# step 1
beatles=[]
print("Step 1:", beatles)

# step 2
members=["John Lennon", "Paul McCartney", "George Harrison"]
for element in members:
    if element not in beatles:
        beatles.append(element)
print("Step 2:", beatles)

# step 3
print("Step 3:", beatles)

# step 4
print("Step 4:", beatles)

# step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
