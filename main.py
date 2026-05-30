from math import sin
from random import random

class Ai:
	def __init__(self, genes):
		# len(self.genes) = 16
		self.genes = genes

	def answer(self, input_lst):
		genes = self.genes
		input_lst.append(1)
		# len(input_lst) == 3
		A = [0, 0, 0, 0]
		for i in range(4):
			for j in range(3):
				A[i] += genes[3 * i + j] * input_lst[j]
		A = [sin(i) for i in A]
		B = 0
		for i in range(4):
			B += genes[12 + i] * A[i]
		
		return B

	def score(self, d):
		inp, right_output = d
		output = self.answer(inp)
		return (output - right_output) ** 2

	def score_all(self, data):
		return sum([
			self.score(d) for d in data
		])
	def c(self):
		x = random()
		genes1 = self.genes[:]
		for i in range(len(genes1)):
			if random() < 0.2:
				genes1[i] += 0.1 * (random() - 1 / 2)
		return Ai(genes1)

data = []
data.append(([0, 0], 0))
data.append(([0, 1], 1))
data.append(([1, 0], 1))
data.append(([1, 1], 0))

ai = Ai([random() - 1 / 2 for _ in range(16)])
score = ai.score_all(data)
print(score)
best_score = score
for i in range(1000):
	ai_list = [ai.c() for _ in range(10)] + [ai]
	ai = sorted(ai_list, key=lambda ai:ai.score_all(data))[0]
	score = ai.score_all(data)
	if score < best_score:
		print(i, ai.score_all(data))
		best_score = score 

print(ai.score_all(data))
print('>', ai.answer([0, 0]))
print('>', ai.answer([0, 1]))
print('>', ai.answer([1, 0]))
print('>', ai.answer([1, 1]))
