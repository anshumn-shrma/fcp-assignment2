import random
file=open("fortune.txt").read()
lines=file.split("%")
print(random.choice(lines))
