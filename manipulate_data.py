import read_data as rd
import numpy as np
from classification import DecisionTreeClassifier
from classificationV2 import ImprovedDecisionTreeClassifier
from evaluation import accuracy

file_name = "data/train_sub.txt"

(x, y, classes) = rd.read_dataset(file_name)

print("For train_sub.txt") 
rd.display_data_information(x, y, classes)

# ===== ------- TRY FIT METHOD OF CLASSIFIER V1 ---- ======

y_letters = []
for i in y:
    y_letters.append(classes[i])
y_letters = np.array(y_letters)
print("Trying fit method")
classifier = DecisionTreeClassifier()
classifier.fit(x, y_letters)

# # ===== ------- TRY PREDICT METHOD OF CLASSIFIER V1 ---- ======

# print("Trying predict method on train_full dataset")
# (x_full, y_full, classes_full) = rd.read_dataset("data/train_full.txt")
# ypred=classifier.predict(x_full)
# print(ypred)

# # ===== ------- TRY PRUNING THE TREE ---- ======

print("Trying to fit for improved classifier")
improved_classifier = ImprovedDecisionTreeClassifier()
improved_classifier.fit(x, y_letters)
print("Making predictions on the validation dataset.")
(x_val, y_val, classes_val) = rd.read_dataset("data/validation.txt")
improved_predictions = improved_classifier.predict(x_val)
improved_accuracy = accuracy(y_val, improved_predictions)
print("The accuracy of improved classifier prior to pruning is ", improved_accuracy)
print("Now, trying to prune the improved classifier")
pruned_accuracy = improved_classifier.test_pruning_tree(improved_classifier.DecisionTree, x_val, y_val, improved_accuracy)
print("The accuracy of the pruned classifier is ", pruned_accuracy)


