from bokeh.plotting import figure, output_file, show

output_file('budget.html')
month = [0, 1, 2, 3, 4, 5, 6, 7]
month_text = ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'May', 'Apr']
bills = [1801, 2016, 1478, 1914, 1778, 2215, 1796, 1559]
income = [2671, 2817, 2509, 2688, 2843, 2762, 2949, 2712]
savings = [870, 801, 1030, 774, 1065, 546, 1153, 1152]

line_graph = figure(title="Presupuesto", x_range=month_text)
line_graph.line(month, bills, line_color="red", legend_label="Gastos")
line_graph.line(month, income, line_color="green", legend_label="Ingresos")
line_graph.line(month, savings, line_color="blue", legend_label="Ahorros")

show(line_graph)