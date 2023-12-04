sum = 0

numbers = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


for line in open("input.txt").readlines():
    _, first = min([(line.index(k), numbers[k]) for k in numbers if k in line])
    _, last = min([(line[::-1].index(k[::-1]), numbers[k]) for k in numbers if k in line])
    
        
    
    sum += first * 10 + last
print(sum)