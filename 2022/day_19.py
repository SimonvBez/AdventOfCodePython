import re
from math import ceil
from dataclasses import dataclass
from operator import mul
from functools import reduce


NO_GOAL = 0
ORE_ROBOT = 1
CLAY_ROBOT = 2
OBSIDIAN_ROBOT = 3
GEODE_ROBOT = 4


@dataclass
class Blueprint:
    blueprint_id: int
    ore_robot_cost_ore: int
    clay_robot_cost_ore: int
    obsidian_robot_cost_ore: int
    obsidian_robot_cost_clay: int
    geode_robot_cost_ore: int
    geode_robot_cost_obsidian: int
    current_best: int = 0

    def __post_init__(self):
        self.max_ore_robots = max(self.ore_robot_cost_ore, self.clay_robot_cost_ore, self.obsidian_robot_cost_ore, self.geode_robot_cost_ore)
        self.max_clay_robots = self.obsidian_robot_cost_clay

    def find_best_geode_count(self, ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geodes, time_left, goal):
        if goal == ORE_ROBOT:
            time_passed = ceil((self.ore_robot_cost_ore - ore) / ore_robots)
        elif goal == CLAY_ROBOT:
            time_passed = ceil((self.clay_robot_cost_ore - ore) / ore_robots)
        elif goal == OBSIDIAN_ROBOT:
            time_passed = ceil(max((self.obsidian_robot_cost_ore - ore) / ore_robots, (self.obsidian_robot_cost_clay - clay) / clay_robots))
        elif goal == GEODE_ROBOT:
            time_passed = ceil(max((self.geode_robot_cost_ore - ore) / ore_robots, (self.geode_robot_cost_obsidian - obsidian) / obsidian_robots))
        else:
            time_passed = 0

        time_passed = min(time_left, max(time_passed, 0)+1)
        time_left -= time_passed

        ore += ore_robots * time_passed
        clay += clay_robots * time_passed
        obsidian += obsidian_robots * time_passed
        geodes += geode_robots * time_passed

        if time_left:
            if goal == ORE_ROBOT:
                ore_robots += 1
                ore -= self.ore_robot_cost_ore
            elif goal == CLAY_ROBOT:
                clay_robots += 1
                ore -= self.clay_robot_cost_ore
            elif goal == OBSIDIAN_ROBOT:
                obsidian_robots += 1
                ore -= self.obsidian_robot_cost_ore
                clay -= self.obsidian_robot_cost_clay
            elif goal == GEODE_ROBOT:
                geode_robots += 1
                ore -= self.geode_robot_cost_ore
                obsidian -= self.geode_robot_cost_obsidian
                self.current_best = max(self.current_best, geodes + geode_robots*time_left)

            possible_best_this_branch = geodes + geode_robots*time_left + ((time_left-1) * time_left) // 2
            if self.current_best > possible_best_this_branch:
                return 0

            next_goals = []
            if obsidian_robots:
                next_goals.append(GEODE_ROBOT)
            if clay_robots:
                next_goals.append(OBSIDIAN_ROBOT)
            if clay_robots < self.max_clay_robots:
                next_goals.append(CLAY_ROBOT)
            if ore_robots < self.max_ore_robots:
                next_goals.append(ORE_ROBOT)

            return max(self.find_best_geode_count(ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geodes, time_left, goal) for goal in next_goals)
        else:
            return geodes

    def calculate_max_geodes(self, minutes):
        return self.find_best_geode_count(1, 0, 0, 0, 0, 0, 0, 0, minutes, NO_GOAL)

    def calculate_quality_level(self, minutes):
        return self.blueprint_id * self.calculate_max_geodes(minutes)


def main():
    blueprints = []
    with open("day_19_input", "r") as f:
        data = re.findall(r"Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.", f.read())
        for blueprint_data in data:
            blueprints.append(Blueprint(*map(int, blueprint_data)))

    print(sum(blueprint.calculate_quality_level(24) for blueprint in blueprints))
    print()
    print(reduce(mul, (blueprint.calculate_max_geodes(32) for blueprint in blueprints[:3])))


if __name__ == "__main__":
    main()
