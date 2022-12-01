
def run(filename):
    with open(filename) as f:
        elf_total = 0
        top3 = []
        for line in f.readlines():
            if line.strip() == '':
                top3 = adjust_top3(top3, elf_total)
                elf_total = 0
            else:
                val = int(line)
                elf_total += val
        top3 = adjust_top3(top3, elf_total)
        return sum(top3)


def adjust_top3(top3, elf_total):
    top3.append(elf_total)
    top3.sort()
    return top3[-3:]


assert run('day1/example.txt') == 45000

print(run('day1/input.txt'))
