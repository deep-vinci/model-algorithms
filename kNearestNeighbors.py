import math

def compute_distances(x_params, y_params, query_point):
    distance_label_pairs = []
    for i in range(len(x_params)): 
        distance = calculate_distance(x_params[i], query_point)
        label = y_params[i]
        distance_label_pairs.append([distance, label])

    distance_label_pairs.sort(key=lambda x: x[0])
    return distance_label_pairs

def calculate_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def majority_label(k_neighbors):
    label_counts = {}  
    for _, label in k_neighbors:
        label_counts[label] = label_counts.get(label, 0) + 1

    max_count = 0
    majority_class = None
    for label, count in label_counts.items():
        if count > max_count:
            max_count = count
            majority_class = label

    return majority_class


X_data = [    
    [1, 2],  
    [2, 3],  
    [3, 1],  
    [6, 5],  
    [7, 6],  
    [5, 7]   
]

y_data = [0, 0, 0, 1, 1, 1]
labels = ["A", "B"]
x_new = [4, 3]
k = 3

sorted_neighbors = compute_distances(X_data, y_data, x_new)
k_nearest_neighbors = sorted_neighbors[:k]
predicted_label = majority_label(k_nearest_neighbors)

print("Predicted target:", predicted_label, "\nLabel:", labels[predicted_label])
