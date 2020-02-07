import heapq
import os
from time import perf_counter 
NUMofFILE = 10

def merge(array, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * n1
	R = [0] * n2

	# temp arrays
	for i in range(0, n1):
		L[i] = array[l + i]

	for j in range(0, n2):
		R[j] = array[m + 1 + j]

	#initial index
	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		array[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		array[k] = R[j]
		j += 1
		k += 1

def mergeSort(array, l, r):
	if l < r:
		m = (l + (r-1)) // 2

		mergeSort(array, l, m)
		mergeSort(array, m + 1, r)

		merge(array,l, m, r)



def createInitialRuns():
	#read unsorted files
	i = 1
	while i <= NUMofFILE:
		#sort files
		#path way could be better
		fileName = "input/unsorted_" + str(i) +".txt"
		newList = [int(line.rstrip('\n')) for line in open(fileName)]
		heapq.heapify(newList)
		mergeSort(newList, 0, len(newList) - 1)

		#export files
		outputFileName = "sorted_" + str(i) +".txt"
		writeFile(outputFileName, newList)
		
		i += 1

def writeFile(fileName, mylist):
	with open(fileName, 'w') as file:
		for num in mylist:
			file.writelines(str(num))
			file.writelines('\n')

def mergeKFiles():	
	n = 1
	i = 1
	count = 1
	while i <= NUMofFILE - n:
		file1 = "sorted_" + str(i) +".txt"
		file2 = "sorted_" + str(i + n) +".txt"
		list1 = [int(line.rstrip('\n')) for line in open(file1)]
		list2 = [int(line.rstrip('\n')) for line in open(file2)]
		output = list(heapq.merge(list1,list2))

		fileName = "sortedK_" + str(count) +".txt"
		writeFile(fileName, output)
		i += 2 * n
		count += 1

	n = 1
	while n < NUMofFILE // 2:
		i = 1
		while i <= NUMofFILE // 2 - n:
			file3 = "sortedK_" + str(i) +".txt"
			file4 = "sortedK_" + str(i + n) +".txt"
			list3 = [int(line.rstrip('\n')) for line in open(file3)]
			list4 = [int(line.rstrip('\n')) for line in open(file4)]
			newList = list(heapq.merge(list3,list4))

			writeFile(file3, newList)
			i = i + 2 * n 

		n = n*2

	os.rename("sortedK_1.txt","sorted.txt")
	os.remove("sortedK_2.txt")
	os.remove("sortedK_3.txt")
	os.remove("sortedK_4.txt")
	os.remove("sortedK_5.txt")


def sort():
	start = perf_counter()  

	createInitialRuns()
	mergeKFiles()

	stop = perf_counter()
	print(stop - start)
	with open("time.txt",'w') as file:
		file.writelines(str(stop - start))
		
