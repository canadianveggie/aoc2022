days := $(wildcard *.c)

day%: day%/part1.py day%/part2.py ;

day%/part1.py: FORCE
	poetry run python $@

day%/part2.py: FORCE
	poetry run python $@

FORCE: ;
