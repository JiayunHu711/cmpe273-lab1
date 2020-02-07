import asyncio
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

loop = asyncio.get_event_loop()

async def createInitialRuns():
	#read unsorted files
	i = 1
	while i <= NUMofFILE:
		#sort files
		#path way could be better
		fileName = "input/unsorted_" + str(i) +".txt"
		newList = [int(line.rstrip('\n')) for line in open(fileName)]
		await asyncio.sleep(0.00001)
		heapq.heapify(newList)
		mergeSort(newList, 0, len(newList) - 1)

		#export files
		outputFileName = "async_sorted_" + str(i) +".txt"
		writeFile(outputFileName, newList)
		await asyncio.sleep(0.00001)
		
		i += 1



def writeFile(fileName, mylist):
	with open(fileName, 'w') as file:
		for num in mylist:
			file.writelines(str(num))
			file.writelines('\n')



async def mergeKFiles():	
	n = 1
	i = 1
	count = 1
	while i <= NUMofFILE - n:
		file1 = "async_sorted_" + str(i) +".txt"
		file2 = "async_sorted_" + str(i + n) +".txt"
		list1 = [int(line.rstrip('\n')) for line in open(file1)]
		list2 = [int(line.rstrip('\n')) for line in open(file2)]
		output = list(heapq.merge(list1,list2))

		fileName = "async_sortedK_" + str(count) +".txt"
		writeFile(fileName, output)
		await asyncio.sleep(0.000001)

		i += 2 * n
		count += 1

	n = 1
	while n < NUMofFILE // 2:
		i = 1
		while i <= NUMofFILE // 2 - n:
			file3 = "async_sortedK_" + str(i) +".txt"
			file4 = "async_sortedK_" + str(i + n) +".txt"
			list3 = [int(line.rstrip('\n')) for line in open(file3)]
			list4 = [int(line.rstrip('\n')) for line in open(file4)]
			newList = list(heapq.merge(list3,list4))

			writeFile(file3, newList)
			await asyncio.sleep(0.00001)
			i = i + 2 * n 

		n = n*2


	os.rename("async_sortedK_1.txt","async_sorted.txt")
	await asyncio.sleep(0.00001)
	os.remove("async_sortedK_2.txt")
	await asyncio.sleep(0.00001)
	os.remove("async_sortedK_3.txt")
	await asyncio.sleep(0.00001)
	os.remove("async_sortedK_4.txt")
	await asyncio.sleep(0.00001)
	os.remove("async_sortedK_5.txt")
	await asyncio.sleep(0.00001)

async def main():
	start = perf_counter() 

	await asyncio.gather(createInitialRuns())
	await asyncio.gather(mergeKFiles())

	stop = perf_counter()
	print(stop - start)
	with open("async_time.txt",'w') as file:
		file.writelines(str(stop - start))

def sort():
	asyncio.run(main())







