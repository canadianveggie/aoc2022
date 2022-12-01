
def run(filename):
    with open(filename) as f:
        elf_total = 0
        max_total = 0
        
        for line in f.readlines():
            if line.strip() == '':
                elf_total = 0
            else:
                val = int(line)
                elf_total += val
                max_total = max(max_total, elf_total)

        return max_total


assert run('day1/example.txt') == 24000

print(run('day1/input.txt'))
