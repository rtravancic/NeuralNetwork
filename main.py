import numpy as np
import random


def relu(x):
    return max(x, 0)


class Neuron:
    def __init__(self):
        self.weight = random.randint(0,1)
        self.bias = random.randint(0,1)

    def forward(self, x):
        total = x * self.weight + self.bias
        return relu(total)


