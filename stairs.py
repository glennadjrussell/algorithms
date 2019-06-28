#!/usr/bin/env python

# Friday 28th June lunchtime exercise
#
# O (n^2)
# Some Amazon interview question. Seems like recursive backtracking question
def stairs(number_of_steps, step_set):
	number_of_ways = 0

	if number_of_steps > 0:
		for x in step_set:
			if (x < number_of_steps):
				number_of_ways += stairs(number_of_steps - x, step_set)
			elif (x == number_of_steps):
				number_of_ways += 1

	return number_of_ways

if __name__ == '__main__':
    n = 6
    step_set = (1, 2, 3, 5)

    print(stairs(n, step_set))
