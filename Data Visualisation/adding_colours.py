import matplotlib.pyplot as plt 

# We need to prove the x-axis/y-axis in the form of lists, range, or panda series
x_axis = [2016, 2017, 2018, 2019, 2020]
y_axis = [190, 213, 182, 196, 201]

# plt.figure(figsize=(10, 5))
# plt.bar(x_axis, y_axis, color = ['red', 'blue', 'purple', 'green', 'orange'])
# plt.show(block=True)

#####  Conditional colouring  #####

colors = []

for i in y_axis:
    if i < 190:
        colors.append('red')
    elif i >= 200:
        colors.append('green')
    else:
        colors.append('orange')

plt.figure(figsize=(10, 4))
plt.bar(x_axis, y_axis, color = colors)
plt.show(block=True)