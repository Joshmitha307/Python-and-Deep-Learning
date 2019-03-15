import numpy as np

r = np.random.randint(0, 20, 15)
print(r)
print("Most frequent value in the above array:")
print(np.bincount(r).argmax())
