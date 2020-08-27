probs = [0.2, 0.3, 0.5]
dscores = probs
dscores[range(3),y] -= 1
print(dscores)
dscores /= num_examples