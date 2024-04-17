positive = int(input("Enter positive votes: "))
negative = int(input("Enter negative votes: "))
abstention = int(input("Enter abstention votes: "))

totalVotes = positive + negative + abstention

positiveP = positive * 100 / totalVotes
negativeP = negative * 100 / totalVotes
abstentionP = abstention * 100 / totalVotes

result = ""

if positive > negative:
    result = "Approved"
elif positive < negative:
    result = "Not Approved"
else:
    result = "Tie!"

print(f"Results:\nTotal Votes: {totalVotes}\nPositive: {positive} ({positiveP:.2f}%)\nNegative: {negative} ({negativeP:.2f}%)\nAbstention: {abstention} ({abstentionP:.2f}%)\n{result}")