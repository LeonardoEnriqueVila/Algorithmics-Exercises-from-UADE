numOfTests = int(input("Enter number of Tests: "))
ratingsSum = 0
for i in range(1, numOfTests + 1):
    rating = int(input(f"Enter Test {i} rating: "))
    #ratings.append(rating)
    ratingsSum += rating
average = ratingsSum / numOfTests
print(f"Average is: {average}")


