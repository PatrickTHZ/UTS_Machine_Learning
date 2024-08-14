import random
import matplotlib.pyplot as plt


# Step 1: Define the Hypothesis Set
def generate_hypothesis_set(num_rectangles, x_range, y_range):
    hypothesis_set = []
    for _ in range(num_rectangles):
        x1, x2 = sorted(random.sample(range(x_range), 2))
        y1, y2 = sorted(random.sample(range(y_range), 2))
        hypothesis_set.append((x1, y1, x2, y2))
    return hypothesis_set


# Step 2: Generate Training Samples
def generate_samples(num_samples, target_rectangle, x_range, y_range):
    samples = []
    x1, y1, x2, y2 = target_rectangle
    for _ in range(num_samples):
        x, y = random.randint(0, x_range), random.randint(0, y_range)
        label = 'in' if x1 <= x <= x2 and y1 <= y <= y2 else 'out'
        samples.append((x, y, label))
    return samples


# Step 3: Select a Hypothesis
def select_best_hypothesis(hypothesis_set, samples):
    best_hypothesis = None
    best_score = -1
    for hypothesis in hypothesis_set:
        score = sum(1 for x, y, label in samples if
                    (hypothesis[0] <= x <= hypothesis[2] and hypothesis[1] <= y <= hypothesis[3]) == (label == 'in'))
        if score > best_score:
            best_score = score
            best_hypothesis = hypothesis
    return best_hypothesis


# Step 4: Evaluate the Selected Hypothesis
def evaluate_hypothesis(hypothesis, test_samples):
    correct = sum(1 for x, y, label in test_samples if
                  (hypothesis[0] <= x <= hypothesis[2] and hypothesis[1] <= y <= hypothesis[3]) == (label == 'in'))
    return correct / len(test_samples)


# Visualization
def plot_rectangles(hypothesis_set, target_rectangle, samples, selected_hypothesis):
    plt.figure(figsize=(10, 10))

    # Plot target rectangle
    plt.plot([target_rectangle[0], target_rectangle[0], target_rectangle[2], target_rectangle[2], target_rectangle[0]],
             [target_rectangle[1], target_rectangle[3], target_rectangle[3], target_rectangle[1], target_rectangle[1]],
             'g-', label='Target Rectangle')

    # Plot selected hypothesis
    if selected_hypothesis:
        plt.plot([selected_hypothesis[0], selected_hypothesis[0], selected_hypothesis[2], selected_hypothesis[2],
                  selected_hypothesis[0]],
                 [selected_hypothesis[1], selected_hypothesis[3], selected_hypothesis[3], selected_hypothesis[1],
                  selected_hypothesis[1]],
                 'r--', label='Selected Hypothesis')

    # Plot samples
    for x, y, label in samples:
        color = 'blue' if label == 'in' else 'red'
        marker = 'o' if label == 'in' else 'x'
        plt.scatter(x, y, c=color, marker=marker)

    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.legend()
    plt.show()


# Parameters
num_rectangles = 1000
num_training_samples = 100
num_test_samples = 100
x_range, y_range = 100, 100
target_rectangle = (20, 30, 80, 70)

# Generate hypothesis set
hypothesis_set = generate_hypothesis_set(num_rectangles, x_range, y_range)

# Generate training and test samples
training_samples = generate_samples(num_training_samples, target_rectangle, x_range, y_range)
test_samples = generate_samples(num_test_samples, target_rectangle, x_range, y_range)

# Select the best hypothesis
selected_hypothesis = select_best_hypothesis(hypothesis_set, training_samples)

# Evaluate the selected hypothesis
accuracy = evaluate_hypothesis(selected_hypothesis, test_samples)

print(f"Selected Hypothesis: {selected_hypothesis}")
print(f"Accuracy on Test Data: {accuracy:.2f}")

# Plot the results
plot_rectangles(hypothesis_set, target_rectangle, test_samples, selected_hypothesis)
