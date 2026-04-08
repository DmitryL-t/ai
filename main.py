from math import sin
from random import random

class Ai:
	def __init__(self, genes):
		self.genes = genes

	def answer(self, input_lst):
		genes = self.genes
		input_lst += [1, -1]
		A = [0, 0, 0, 0]
		for i in range(4):
			for j in range(4):
				A[i] += genes[4 * i + j] * input_lst[j]
		A = [sin(i) for i in A]
		B = 0
		for i in range(4):
			B += genes[16 + i] * A[i]
		
		return B

	def how_good(self, d):
		inp, right_output = d
		output = self.answer(inp)
		return (output - right_output) ** 2

	def how_good_all(self, data):
		return sum([
			self.how_good(d) for d in data
		])
	def c(self):
		x = random()
		genes1 = self.genes[:]
		for i in range(len(genes1)):
			if random() < 0.25:
				genes1[i] += 0.1 * random()
		return Ai(genes1)

data = []
data.append(([0, 0], 0))
data.append(([0, 1], 1))
data.append(([1, 0], 1))
data.append(([1, 1], 0))

ai = Ai([random() - 1 / 2 for _ in range(20)])
for i in range(100):
	if i % 10 == 0:
		print(i, ai.how_good_all(data))
	ai_list = [ai.c() for _ in range(10)] + [ai]
	ai = sorted(ai_list, key=lambda ai:ai.how_good_all(data))[0]

print(ai.how_good_all(data))
print('>', ai.answer([0, 0]))
print('>', ai.answer([0, 1]))
print('>', ai.answer([1, 0]))
print('>', ai.answer([1, 1]))
