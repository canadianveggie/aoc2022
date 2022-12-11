days := $(wildcard *.c)

day%: day%/solve.py ;

day%/solve.py: FORCE
	python3 $@

FORCE: ;
