import random
import math
import csv



Species = input('Pokemon Species: ')
try:
	GenderRatioMales = int(input('Males in gender ratio (1-10, default 1): '))
except ValueError:
	GenderRatioMales = 1
if GenderRatioMales <= 0 or GenderRatioMales > 10:
	GenderRatioMales = 1
try:
	GenderRatioFemales = int(input('Females in gender ratio (1-10, default 1): '))
except ValueError:
	GenderRatioFemales = 1
if GenderRatioFemales <= 0 or GenderRatioFemales > 10:
	GenderRatioFemales = 1
try:
	MinPop = int(input('Minimum Population (1-1000, default 10): '))
except ValueError:
	MinPop = 10
if MinPop <= 0 or MinPop > 1000:
	MinPop = 10

while (MalePop + FemalePop) < 10:
	MalePop += GenderRatioMales
	FemalePop += GenderRatioFemales

try:
	PenaltyTime = int(input('Fertility penalty after x ticks (default 100): '))
except ValueError:
	PenaltyTime = 100
try:
	FertilityPenalty = int(input('Fertility penalty (in percentage, subtracted from 50, default 40): '))
except ValueError:
	FertilityPenalty = 40

tick = 0
Eggs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open(Species + 'Population.csv', 'a', newline='') as csv_file:
		fieldnames = ['tick', 'females', 'males']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		csv_file.close()

while True:
	with open(Species + 'Population.csv', 'a', newline='') as csv_file:
		fieldnames = ['tick', 'females', 'males']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writerow({'tick': tick, 'females': FemalePop, 'males': MalePop})
		csv_file.close()
	tick += 1
	print('Tick: ', tick)
	for x in range(FemalePop):
		death = random.randint(1, 10000)
		if death <= 243:
			FemalePop -= 1

	for x in range(MalePop):
		death = random.randint(1, 10000)
		if death <= 243:
			MalePop += -1

	if Eggs[0] > 0:
		print (Eggs[0], Species + ' Eggs are hatching!')
		for x in range(Eggs[0]):
			sexroll = random.randint(1, GenderRatioFemales + GenderRatioMales)
			if sexroll <= GenderRatioMales:
				MalePop += 1
			else:
				FemalePop += 1

	for x in range(0, 19):
		Eggs[x] = Eggs[x + 1]
	Eggs[19] = 0

	if MalePop >=1 and tick <= PenaltyTime:
		for x in range(FemalePop):
			egg = random.randint(1,100)
			if egg <= 50:
				Eggs[19] += 1
	elif FemalePop >=1:
		for x in range(FemalePop):
			egg = random.randint(1,100)
			if egg <= 50 - FertilityPenalty:
				Eggs[19] += 1

	print('Total Population: ', FemalePop+MalePop)
	print('Females: ', FemalePop)
	print('Males: ', MalePop)
	print('')

	if FemalePop+MalePop >= 20000:
		print('Population max reached')
		break
	elif FemalePop == 0 and (len(list (filter (lambda x : x == 0, Eggs))) == 20):
		print('Extinction')
		break