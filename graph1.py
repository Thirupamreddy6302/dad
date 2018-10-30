import matplotlib.pyplot as plot

#x-coordinates of left sides of bars
left=[1,2,3,4,5]

#heightof bars
height=[10,24,36,44,50]


tick=['one','two','three','four','five']

#plottng a bar chart 
plot.bar(left,height,tick_label=tick,width=0.8,color=['red','green']) 


plot.xlabel('x-axis')

plot.ylabel('y-axis')

plot.title('bar graph')

plot.show()


