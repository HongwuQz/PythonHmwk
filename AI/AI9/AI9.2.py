import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np

with open('walterMelonData.txt','r') as f:
    data = []
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line.split(' '))
    data = np.array(data,dtype=float)
    watermelon_data = np.array(data[:,:8])
    watermelon_target = np.array(data[:,8])

watermelon_tree = tree.DecisionTreeClassifier(criterion='entropy')
watermelon_tree = watermelon_tree.fit(watermelon_data,watermelon_target)
plt.figure(1)
tree.plot_tree(watermelon_tree)
plt.show()