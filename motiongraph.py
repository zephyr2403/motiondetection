import matplotlib.pyplot as plt

fig = plt.figure()
plot1 = fig.add_subplot(1,1,1)

def plotter(DetectionList):

	plt.xticks(range(1,DetectionList[-1]+1),range(1,DetectionList[-1]+1))
	plt.yticks([0,1],['No Motion','Detected',])
	plot1.hist(DetectionList,bins=range(1,DetectionList[-1]+2),rwidth=.98)
	plt.xlabel('Time in Seconds')
	plt.ylabel('Detection')
	plt.show()
