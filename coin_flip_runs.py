"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	show the same string together ,if stop string determined by your num_run.
	"""
	print("Let' flip a coin!")
	num_run = int(input('Number of runs:'))
	run_coin=''
	# for _ in range(100):    ＃有限定長度
	while True:   #while True:  一直重相同動作
		run_coin+=r.choice(["H", "T"])
		a=0
		for i in range(len(run_coin)):
			if i!=len(run_coin)-1:
				if run_coin[i] == run_coin[i+1]:
					if i+1 ==len(run_coin)-1:
						a += 1
					elif run_coin[i+1]!=run_coin[i+2]:
						a += 1
		if a == num_run:
			print(run_coin)
			break

# run_coin = r.choice("HT")
###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
