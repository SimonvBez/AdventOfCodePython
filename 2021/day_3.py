from collections import Counter

byte_strings = []


with open("day_3_input", "r") as f:
    for line in (x.strip() for x in f):
        byte_strings.append(line)


gamma_byte_string = ""
epsilon_byte_string = ""
for bits in zip(*byte_strings):
    most_common_bit, least_common_bit = Counter(bits).most_common(2)
    gamma_byte_string += most_common_bit[0]
    epsilon_byte_string += least_common_bit[0]

gamma_rate = int(gamma_byte_string, 2)
epsilon_rate = int(epsilon_byte_string, 2)
power_consumption = gamma_rate * epsilon_rate
print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumption: {power_consumption}")


remaining_bytes = byte_strings.copy()
current_bit = 0
while len(remaining_bytes) > 1:
    bits = [byte[current_bit] for byte in remaining_bytes]
    most_common = Counter(bits).most_common(2)
    if len(most_common) == 2 and most_common[0][1] == most_common[1][1]:
        most_common_bit = "1"
    else:
        most_common_bit = most_common[0][0]
    remaining_bytes = [byte for byte in remaining_bytes if byte[current_bit] == most_common_bit]
    current_bit += 1
oxygen_generator_rating = int(remaining_bytes[0], 2)

remaining_bytes = byte_strings.copy()
current_bit = 0
while len(remaining_bytes) > 1:
    bits = [byte[current_bit] for byte in remaining_bytes]
    most_common = Counter(bits).most_common(2)
    if len(most_common) == 2 and most_common[0][1] == most_common[1][1]:
        least_common_bit = "0"
    else:
        least_common_bit = most_common[-1][0]
    remaining_bytes = [byte for byte in remaining_bytes if byte[current_bit] == least_common_bit]
    current_bit += 1
co2_scrubber_rating = int(remaining_bytes[0], 2)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating

print("\n")
print(f"Oxygen generator rating: {oxygen_generator_rating}")
print(f"CO2 scrubber rating: {co2_scrubber_rating}")
print(f"Life support rating: {life_support_rating}")
