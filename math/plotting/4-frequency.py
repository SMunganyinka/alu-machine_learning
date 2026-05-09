#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# bins every 10 on x-axis
bins = np.arange(0, 101, 10)

plt.hist(student_grades, bins=bins, edgecolor="black")

plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Project A")

# x-axis range and ticks (step of 10)
plt.xlim(0, 100)
plt.xticks(np.arange(0, 101, 10))

# y-axis range and ticks (step of 5)
plt.ylim(0, 25)
plt.yticks(np.arange(0, 26, 5))

plt.show()
