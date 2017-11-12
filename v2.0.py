#This program is based off the basic model of a perceptron. Since there only needs to be one output
#	there only needs to be one neuron.

from math import exp
import random
import time


############# NEURAL NETWORK CODE
#Dot product function for later. Taken directly from http://stackoverflow.com/questions/5919530/what-is-the-pythonic-way-to-calculate-dot-product
def dot(A, B):
	result = sum([i*j for (i, j) in zip(A, B)])
	return result
	
class MyNeuralNetwork():
	#Constructor: Weights 
	def __init__(self):
		#initialize the input weights for the perceptron to random numbers 
		#input weights will be stored in an array of length 8
		random.seed(time.time())
		for x in range (0,32):
			self.weights = list()
			self.weights.append(2*(random.random()) - 1)
	
	#Define the fire function for whether or not the neuron is a 0 or 1
	def fire_function(self, input):
		#This function is a sigmoid function in the perceptron model. The sigmoid equation is 1/(1+e^-t) according to wikipedia
		return (1/(1+exp(input*(-1))))
		
	#Simple evaluate function. Pass inputs through weights and see where it lies on sigmoid firing curve
	def evaluate(self, input):
		value = self.fire_function(dot(input, self.weights))
		return value
		
	#Learning function. Compares the predicted value with the current weights against the 
	#supervised true value and updates weights respectively
	def learn(self, example_input, example_output):
		predicted = self.evaluate(example_input)
		#Compare to true value
		error = example_output - predicted
		#Multiply this error by the input to make sure only the inputs that were activated are changed.
		weight_update = list()
		##LEARNING RATE!
		learning_rate = 0.1
		for input in example_input:
			weight_update.append(input * error * learning_rate)
		#Apply the updates
		for i in range(len(self.weights)):
			self.weights[i] = self.weights[i] + weight_update[i]
			

########### MAIN FUNCTION
#Design: Have 32 inputs be the inputs to the perceptron, therefore 8 weights.

if __name__ == "__main__":
	#Explain the problem:
	print('This program utilizes a simple neural network to predict user binary inputs')
	print('Enter either a 1 or a 2 for each iteration. The neural network will start predicting you at iteration 64 and the program will last until iteration 96')
	
	#Take in the first 32 values
	user_pattern = list()
	for i in range(32):
		user_input = raw_input((str(i) + ":"))
		user_input = int(user_input)
		if (user_input == 2):
			user_pattern.append(1)
		elif (user_input == 1):
			user_pattern.append(0)
		else:
			print('Invalid input. Iteration will be discarded.')
			user_pattern.append(0)
	
	#Start Training the neural network, deep_thought. 
	deep_thought = MyNeuralNetwork()

	for i in range(32):
		user_input = raw_input((str(i+32) + ":"))
		user_input = int(user_input)
		if (user_input == 2):
			user_input = 1
		elif (user_input == 1):
			user_input = 0
		else:
			print('Invalid input. Iteration will be discarded.')
			user_input = 0
		#Use the user_pattern list of size 32 and compare it against the new supervised user value
		#Go through every iteration 10 times
		for i in range(10):
			deep_thought.learn(user_pattern, user_input)
		
		#Change the user_pattern window to incorporate the new input
		user_pattern.pop(0)
		user_pattern.append(user_input)
	
	print('The network will not try to predict your next choice for the remaining 32 iterations.')
	correct_guesses = 0
	for i in range(32):
		user_input = raw_input((str(i+64) + ":"))
		user_input = int(user_input)
		if (user_input == 2):
			user_input = 1
		elif (user_input == 1):
			user_input = 0
		else:
			print('Invalid input. Iteration will be discarded.')
			user_input = 0
		#Use the user_pattern list of size 32 and compare it against the new supervised user value
		print('Guessed Value: ' + str(1+deep_thought.evaluate(user_pattern)))
		if ((deep_thought.evaluate(user_pattern) <= 0.5) & (user_input == 0)):
			correct_guesses += 1
			print('Computer was right! Number of correct guesses: ' + str(correct_guesses))
		elif((deep_thought.evaluate(user_pattern) > 0.5) & (user_input == 1)):
			correct_guesses += 1
			print('Computer was right! Number of correct guesses: ' + str(correct_guesses))
		else:
			print('Computer was wrong! Whoops.')
			
		for i in range(10):
			deep_thought.learn(user_pattern, user_input)
		
		#Change the user_pattern window to incorporate the new input
		user_pattern.pop(0)
		user_pattern.append(user_input)
		print(str(i) + ":" + str(user_pattern))