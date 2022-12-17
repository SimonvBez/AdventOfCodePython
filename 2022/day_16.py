import re


class Valve:
    def __init__(self, flow_rate, tunnels):
        self.flow_rate = flow_rate
        self.tunnels = tunnels
        self.distances = {}


def get_score(all_valves, valves_order, time_left):
    order = iter(valves_order)
    current_location = next(order)
    total_release = 0
    for next_valve in order:
        time_passed = all_valves[current_location].distances[next_valve] + 1
        time_left -= time_passed
        total_release += time_left * all_valves[next_valve].flow_rate
        current_location = next_valve
    return total_release


def get_distance(valve_start, valve_goal, valves):
    distance = 1
    map_queue = {valve_start}
    mapped = set()
    while True:
        new_map_queue = set()
        for map_valve in map_queue:
            for connected_valve in valves[map_valve].tunnels:
                if valve_goal == connected_valve:
                    return distance
                elif connected_valve not in mapped:
                    new_map_queue.add(connected_valve)
        mapped |= new_map_queue
        map_queue = new_map_queue
        distance += 1


def for_each_option(current_valve, option_index, remaining_options, all_valves, time_left, current_flow, total_release):
    next_option = remaining_options.pop(option_index)
    time_passed = all_valves[current_valve].distances[next_option] + 1
    if time_left > time_passed:
        time_left -= time_passed
        total_release += current_flow * time_passed
        current_flow += all_valves[next_option].flow_rate
        return find_best_path(next_option, remaining_options, all_valves, time_left, current_flow, total_release)
    else:
        return total_release + current_flow * time_left


def find_best_path(current_location, remaining_options, all_valves, time_left, current_flow, total_release):
    if remaining_options:
        return max(for_each_option(current_location, i, remaining_options.copy(), all_valves, time_left, current_flow, total_release) for i in range(len(remaining_options)))
    else:
        return total_release + time_left * current_flow


def all_orders(current_order, remaining_options, all_valves, time_left):
    for next_option in remaining_options:
        cost = all_valves[current_order[-1]].distances[next_option] + 1
        if cost < time_left:
            yield from all_orders(current_order + [next_option], remaining_options - {next_option}, all_valves, time_left - cost)

    yield current_order


def main():
    valves = {}

    with open("day_16_input", "r") as f:
        for line in (x.strip() for x in f):
            valve, flow_rate, tunnels = re.match(r"Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line).groups()
            valves[valve] = Valve(int(flow_rate), tunnels.split(", "))

    start_valve = "AA"
    useful_valves = [valve[0] for valve in valves.items() if valve[1].flow_rate]
    for useful_valve in useful_valves + [start_valve]:
        valves[useful_valve].distances = {other_valve: get_distance(useful_valve, other_valve, valves) for other_valve in useful_valves if other_valve is not useful_valve}

    print(find_best_path("AA", useful_valves, valves, 30, 0, 0))

    orders = all_orders(["AA"], set(useful_valves), valves, 26)
    scores_and_orders = [(get_score(valves, order, 26), set(order[1:])) for order in orders]
    scores_and_orders.sort(reverse=True)

    best_score = 0
    for i, (my_score, my_order) in enumerate(scores_and_orders):
        if my_score * 2 < best_score:  # The elephant is guaranteed to score less than my_score, so the current best is the best
            break
        for elephant_score, elephant_order in scores_and_orders[i + 1:]:
            if not my_order & elephant_order:
                score = my_score + elephant_score
                if score > best_score:
                    best_score = score
    print()
    print(best_score)


if __name__ == "__main__":
    main()
