import numpy as np
marks=np.array([78,85,92,67,88,73])
print("Marks : ",marks)

#statistics
print("Average Marks : ",np.mean(marks))
print("Highest Marks : ",np.max(marks))
print("Lowest Marks : ",np.min(marks))
print("Standard Deviation : ",np.std(marks))

#student scoring above average

above_avg=marks[marks>np.mean(marks)]
print("marks above average : ",above_avg) 