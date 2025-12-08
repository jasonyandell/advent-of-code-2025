from aoc import read_data_as_char_grid

sample=read_data_as_char_grid("07-sample.txt")
input_text=read_data_as_char_grid("07.txt")

def parse(lines:list[list[str]])->list[list[str]]:
    return lines

def part1(lines:list[list[str]])->tuple[int,int]:
    record = [0 if x == '.' else 1 for x in lines[0]]
    records = [record]
    splits = 0
    for layer in lines[1:]:
        new_splits = 0
        new_record = [x for x in record]
        for i,value in enumerate(layer):
            if value != '.':
                if new_record[i] != 0:
                    new_splits += 1
                new_record[i-1] += record[i]
                new_record[i] = 0
                new_record[i+1] += record[i]
        record = new_record
        records.append(record)
        splits += new_splits
        # print(record, splits, new_splits)
    return splits, sum(record)

print("sample (p1, p2):", part1(sample))
print("input (p1, p2):", part1(input_text))
