#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:41:21 2022

@author: student
"""

interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0,"Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"), (1,"NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1,"Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3,"Python"), (3, "statistics"), (3, "regression"), (3,"probability"), (4, "machine learning"), (4, "regression"),(4, "decision trees"), (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programminglanguages"), (6, "statistics"), (6, "probability"), (6,"mathematics"), (6, "theory"), (7, "machine learning"), (7,"scikit-learn"), (7, "Mahout"), (7, "neural networks"), (8,"neural networks"), (8, "deep learning"), (8, "Big Data"), (8,"artificial intelligence"), (9, "Hadoop"), (9, "Java"), (9,"MapReduce"), (9, "Big Data") ]


nameDictionary={name[1]:[] for name in interests}
for interest,name in interests:
    nameDictionary[name].append(interest)

print(nameDictionary)
 