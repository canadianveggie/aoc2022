
def run(filename):
    with open(filename) as f:
        elf_total = 0
        max_total = 0
        top3 = []
        for line in f.readlines():
            if line.strip() == '':
                elf_total = 0
            else:
                val = int(line)
                elf_total += val
                top3.append(elf_total)
                top3.sort()
                top3 = top3[-3:]


assert run('day1/example.txt') == 45000

print(run('day1/input.txt'))
