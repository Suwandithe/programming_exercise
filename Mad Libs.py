template = "A shinigami [verb] my [adjective] [noun] out of the [noun] as if he were a vegetarian fishing a [noun] out of his salad"
print(template)

verb =input("enter a verb:")
adjective =input("enter a adjective:")
noun1 =input("enter 1st noun:")
noun2=input("enter 2nd noun:")
noun3 = input("enter 3rd noun:")

output = template.replace("[verb]", verb)
output = output.replace("[adjective]", adjective)
output = output.replace("[noun]",noun1,1)
output = output.replace("[noun]",noun2,1)
output = output.replace("[noun]",noun3,1)
print(output)






