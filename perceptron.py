def step(x):
    return 1 if x >= 0 else 0

def predict(inputs, weights, bias):
    total = sum(w * x for w, x in zip(weights, inputs)) + bias
    return step(total)

def train(data, epochs, lr):
    weights = [0.0] * len(data[0][0])
    bias = 0.0

    for _ in range(epochs):
        for inputs, target in data:
            guess = predict(inputs, weights, bias)
            error = target - guess
            for i in range(len(weights)):
                weights[i] += lr * error * inputs[i]
            bias += lr * error

    return weights, bias


training_data = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1),
]

a, b = train(training_data, 10, 0.1);

print([predict(x, a, b) for x, _ in training_data])
