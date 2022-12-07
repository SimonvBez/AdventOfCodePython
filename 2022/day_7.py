class Directory:
    def __init__(self, parent):
        self.files = {}
        self.dirs = {}
        self.parent_dir = parent

    def add_file(self, size, filename):
        self.files[filename] = size

    def make_dir(self, dirname):
        if dirname not in self.dirs:
            self.dirs[dirname] = Directory(self)

    def get_dir(self, path: list[str]):
        if not len(path):
            return self

        next_dir_name, *rest = path
        if next_dir_name == "":
            next_dir = root_dir
        elif next_dir_name == "..":
            next_dir = self.parent_dir
        else:
            next_dir = self.dirs[next_dir_name]

        return next_dir.get_dir(rest)

    def get_total_size(self):
        return sum(d.get_total_size() for d in self.dirs.values()) + sum(file for file in self.files.values())

    def print(self, indent_count=2):
        if self.parent_dir is None:
            print("- / (dir)")

        indent = " " * indent_count
        for dirname, subdir in self.dirs.items():
            print(f"{indent}- {dirname} (dir)")
            subdir.print(indent_count + 2)
        for filename, size in self.files.items():
            print(f"{indent}- {filename} (file, {size=})")

    def walk_dirs(self):
        yield self
        for subdir in self.dirs.values():
            yield from subdir.walk_dirs()


root_dir = Directory(None)

with open("day_7_input", "r") as f:
    terminal_output = [x.strip() for x in f]


current_dir = root_dir
for line in terminal_output:
    line_split = line.split()
    if line_split[0] == "$":
        executable, *args = line_split[1:]
        if executable == "cd":
            current_dir = current_dir.get_dir(args[0].split("/"))
    else:
        size_or_dir, name = line_split
        if size_or_dir == "dir":
            current_dir.make_dir(name)
        else:
            current_dir.add_file(int(size_or_dir), name)


size_sum = 0
for directory in root_dir.walk_dirs():
    if (size := directory.get_total_size()) <= 100000:
        size_sum += size

print(size_sum)


total = 70000000
required = 30000000
free_space = total - root_dir.get_total_size()

space_to_free_up = required - free_space

print()
print(min(dir_size for directory in root_dir.walk_dirs() if (dir_size := directory.get_total_size()) >= space_to_free_up))
