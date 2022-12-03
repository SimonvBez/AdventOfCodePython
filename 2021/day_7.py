with open("day_7_input", "r") as f:
    positions = [int(num) for num in f.read().split(",")]

positions.sort()

median = positions[len(positions) // 2]
fuel_cost = sum(abs(median - pos) for pos in positions)
print(f"Median: {median}")
print(f"Fuel cost: {fuel_cost}")


def calculate_fuel(movement):
    """Equal to sum(range(1, movement+1))"""
    half = movement / 2
    return int(movement * half + half)


average = sum(positions) // len(positions)

best_fuel_cost = None
best_position = None
for i in range(-2, 3):
    fuel_cost = sum(calculate_fuel(abs(average+i - pos)) for pos in positions)
    if not best_fuel_cost or fuel_cost < best_fuel_cost:
        best_fuel_cost = fuel_cost
        best_position = i


print()
print(f"Best position: {average+best_position} (average{best_position:+})")
print(f"Fuel cost: {best_fuel_cost}")
