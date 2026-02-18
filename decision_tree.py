#-------------------------------------------------------------------------
# AUTHOR: Luis Felix
# FILENAME: decision_tree.py
# SPECIFICATION: Python Program that will classify contact lens prescriptions using a decision tree.
# FOR: CS 4210- Assignment #1
# TIME SPENT: 2 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#encode the original categorical training features into numbers and add to the 4D array X.
#--> add your Python code here
# X =
ageDictionary = {'Young':0,'Prepresbyopic': 1, 'Presbyopic': 2}
spectacleDictionary = {'Myope': 0,'Hypermetrope': 1}
astigmatismDictionary = {'No': 0,'Yes': 1}
tearDictionary = {'Reduced': 0,'Normal': 1}

for row in db:
   
   age = ageDictionary[row[0]]
   spectacle = spectacleDictionary[row[1]]
   astigmatism = astigmatismDictionary[row[2]]
   tear = tearDictionary[row[3]]

   X.append([age,spectacle,astigmatism,tear])

#encode the original categorical training classes into numbers and add to the vector Y.
#--> addd your Python code here
# Y =
classDictionary = {'Yes':0,'No':1}

for row in db:
  Y.append(classDictionary[row[4]])

#fitting the depth-2 decision tree to the data using entropy as your impurity measure
#--> addd your Python code here
#clf =

clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=2,random_state=42)
clf = clf.fit(X,Y)

#plotting decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()