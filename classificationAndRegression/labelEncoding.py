import numpy as np
from sklearn import preprocessing
from time import perf_counter

#sample output labels
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# Create label encoder and fit the labels
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

print("\nLabel mapping:")
#start = perf_counter()
for i, item in enumerate(encoder.classes_):
    print(item, "-->", i)
#print("\ntime taken: %f" %(perf_counter()-start))

"""print('\nSet')
start = perf_counter()
for i, item in enumerate(sorted(set(input_labels))):
    print(item, "-->", i)
print("\ntime taken: %f"  %(perf_counter()-start))"""

# Encode a set of labels using the encoder
test_labels = ["green", "red", "black"]
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)
print("Encoded values =", encoded_values)

# Decode a set of values using the encoder
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list(decoded_list))