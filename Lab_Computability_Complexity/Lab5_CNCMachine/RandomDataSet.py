import random
UInput = input("len of dataset :")
jobs = []

for i in range(int(UInput)):
    M = random.randint(1,3)
    T = random.randint(0,60)
    jobs.append(["J" + str(i), "M" + str(M),T])

print(jobs)