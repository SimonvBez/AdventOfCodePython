with open("day_10_input", "r") as f:
    lines = [x.strip() for x in f]


chunk_chars = ["()", "[]", "{}", "<>"]
chunk_closer_to_opener = {closer: opener for opener, closer in chunk_chars}
corrupt_point_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
missing_point_values = {"(": 1, "[": 2, "{": 3, "<": 4}

corrupt_point_sum = 0
incomplete_scores = []
for line in lines:
    chunk_stack = []
    for c in line:
        if c in chunk_closer_to_opener:
            if not chunk_stack or chunk_closer_to_opener[c] != chunk_stack.pop():
                corrupt_point_sum += corrupt_point_values[c]
                break
        else:
            chunk_stack.append(c)
    else:
        score = 0
        for c in reversed(chunk_stack):
            score *= 5
            score += missing_point_values[c]
        incomplete_scores.append(score)

incomplete_scores.sort()

print(corrupt_point_sum)
print()
print(incomplete_scores[len(incomplete_scores) // 2])
