with open("day_6_input", "r") as f:
    data_buffer = f.read()

for i in range(4, len(data_buffer)):
    if len(set(data_buffer[i-4:i])) == 4:
        start_of_packet = i
        break

print(start_of_packet)


for i in range(14, len(data_buffer)):
    if len(set(data_buffer[i-14:i])) == 14:
        start_of_message = i
        break

print()
print(start_of_message)
