
with open('day1/input.txt') as f:
    elf_total = 0
    max_total = 0
    
    for line in f.readlines():
        if line.strip() == '':
            elf_total = 0
        else:
            val = int(line)
            elf_total += val
            max_total = max(max_total, elf_total)

    print(max_total)
