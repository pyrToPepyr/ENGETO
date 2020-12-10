colors = ['red', 'blue', 'yellow', 'red', 'green', 'grey', 'white', 'green', 'red', 'blue', 'yellow', 'red']
color = {}

while colors:
	color_test = colors.pop()

	if color_test not in color:
		color[color_test] = 0

	color[color_test] += 1
print(color)



