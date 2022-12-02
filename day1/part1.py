import os


def local_file(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


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


assert run(local_file('example.txt')) == 24000

print(run(local_file('input.txt')))
