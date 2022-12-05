import itertools


measurements = []
with open("day_1_input", "r") as f:
    for line in (x.strip() for x in f):
        measurements.append(int(line))

total_increases = 0
for m1, m2 in itertools.pairwise(measurements):
    total_increases += m2 > m1

print(f"Amount of times a measurement increased over the previous measurement: {total_increases}")


sum_measurements = []
for i in range(len(measurements) - 2):
    sum_measurements.append(measurements[i] + measurements[i+1] + measurements[i+2])

total_increases = 0
for m1, m2 in itertools.pairwise(sum_measurements):
    total_increases += m2 > m1

print(f"Amount of times a measurement increased over the previous measurement: {total_increases}")