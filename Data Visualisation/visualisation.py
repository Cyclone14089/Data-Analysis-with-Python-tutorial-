import matplotlib.pyplot as plt 

# We need to prove the x-axis/y-axis in the form of lists, range, or panda series
x_axis = [2016, 2017, 2018, 2019, 2020]
y_axis = [190, 213, 182, 196, 201]

#####  Bar plot  #####
plt.bar(x_axis, y_axis)
plt.show(block=True)

#####  Scatter plot  #####
plt.figure(figsize=(16, 8)) # custom size for the figure
plt.scatter(x_axis, y_axis)
plt.show(block=True)

plt.figure(figsize=(12, 6))
plt.scatter(x_axis, y_axis)
plt.xticks(x_axis, rotation=30)
plt.show(block=True)