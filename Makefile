days := $(wildcard *.c)

day%: day%/solve.py ;

day%/solve.py: FORCE
	poetry run python $@

FORCE: ;
