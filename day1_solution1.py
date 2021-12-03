from urllib.request import urlopen
data = urlopen('https://raw.githubusercontent.com/tjaanenson/Advent_Of_Code_2021/blob/main/day1_input.txt').read().decode().split('\n')[:-1]

data = [int(x) for x in data]
sum([y - x for x, y in zip(data, data[1:])])
