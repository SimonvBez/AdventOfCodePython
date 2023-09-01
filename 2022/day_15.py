import re


class IntervalTree:
    def __init__(self):
        self.intervals = []

    def add_interval(self, interval):
        self.intervals.append(interval)

    def merge_intervals(self):
        self.intervals.sort()
        i = 0
        while i < len(self.intervals)-1:
            left = self.intervals[i]
            right = self.intervals[i+1]
            if right[0] <= left[1]:
                self.intervals[i:i+2] = [[left[0], max(left[1], right[1])]]
            else:
                i += 1


class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.sensor_x = sensor_x
        self.sensor_y = sensor_y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
        self.distance_to_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    def get_coverage_range_in_row(self, y):
        distance_to_row = abs(self.sensor_y - y)
        row_half_length = (self.distance_to_beacon - distance_to_row)
        if row_half_length >= 0:
            row_start = self.sensor_x - row_half_length
            row_end = self.sensor_x + row_half_length
            return [row_start, row_end]


def main():
    sensors = []
    beacons = set()
    with open("day_15_input", "r") as f:
        for line in (x.strip() for x in f):
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r"-?\d+", line))
            sensors.append(Sensor(sensor_x, sensor_y, beacon_x, beacon_y))
            beacons.add((beacon_x, beacon_y))

    no_beacon_ranges = IntervalTree()
    for sensor in sensors:
        if interval := sensor.get_coverage_range_in_row(2000000):
            no_beacon_ranges.add_interval(interval)
    no_beacon_ranges.merge_intervals()

    coverage_sum = sum(interval[1] - interval[0] + 1 for interval in no_beacon_ranges.intervals)
    beacon_count = sum(1 for beacon in beacons if beacon[1] == 2000000)

    print(coverage_sum - beacon_count)

    for y in range(4000001):
        coverage = IntervalTree()
        for sensor in sensors:
            if interval := sensor.get_coverage_range_in_row(y):
                coverage.add_interval(interval)
        coverage.merge_intervals()
        if len(coverage.intervals) > 1:
            coverage_gap_x = coverage.intervals[0][1] + 1
            if 0 <= coverage_gap_x <= 4000000:
                print()
                print(coverage_gap_x * 4000000 + y)
                break


if __name__ == "__main__":
    main()
