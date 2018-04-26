import numpy as np
import math
from collections import Counter, defaultdict

#def calc_angle(x, y):
 #norm_x = np.linalg.norm(x)
 #norm_y = np.linalg.norm(y)
 #cos_theta = np.dot(x, y) / (norm_x * norm_y)
 #theta = math.degrees(math.acos(cos_theta))
 #return theta

#a = np.array([1,1,0,2,0,0,2,0,2,0,1,0,0,0,0,2])
#b = np.array([0,0,2,0,0,1,0,2,0,1,0,1,1,0,0,0])
#c = np.array([0,0,2,0,1,0,0,0,3,0,0,0,0,2,1,0])
#print("A vs B:", calc_angle(a, b))
#print("B vs C:", calc_angle(b, c))
#print("A vs C:", calc_angle(a, c))


# Given list of lists of words, gets the list IDs in which those words appear
def getInvertedIndex(data):
        idx = defaultdict(list)
        for i, tkns in enumerate(data):
            for tkn in tkns:
                idx[tkn].append(i)
        return idx

# Given file locations, gets the list of unique words per line in a list
def getContent(file):
	content = []
	for line in open(file).read().splitlines():
		content+=[set(line.split())]
	return content

def getDictionary(file):
	content = []
	for line in open(file).read().splitlines():
		content+=line.split()
	return set(content)

def getVector(dictionary, text):
	genList = []
	for word in dictionary:
		genList += text.count(word)
	return np.array(genList)

def calcAngle(x, y):
 	norm_x = np.linalg.norm(x)
 	norm_y = np.linalg.norm(y)
 	cosTheta = np.dot(x, y) / (norm_x * norm_y)
 	theta = math.degrees(math.acos(cosTheta))
 	return theta

def searchDocument(file, queryFile):
	# List of lines
	for line in open(queryFile).read().splitlines():
		print("Query: " + line)
		lineData = set(line.split())
		#Get an int list of IDs for documents in the file that have matching words

		# Strip words out of the query if they're not in the documents' dictionary
		dictionary = getDictionary(file)
		#print("DICT: ", dictionary)
		for datum in lineData:
			if (datum not in dictionary):
				lineData.remove(datum)
		document = getContent(file)
		invertedIndex = getInvertedIndex(document)

		listOfIDs = []
		for datum in lineData:
			if (datum in invertedIndex):
				listOfIDs.extend(invertedIndex[datum])
		print("Relevant documents: ", " ".join(str(s) for s in set(listOfIDs)))

		# get new inverted index for dictionary + query, then go through the previous inverted index and turn each one into a vector and compare
		#queryIndex = getInvertedIndex(lineData + dictionary)
		vectorDoc = getVector(dictionary, document)
		vectorQuery = getVector(dictionary, lineData)


#print(getInvertedIndex([["a", "b"], ["a", "c"], ["a", "c"], ["b", "d"], ["a", "b", "c"]]))

#invertedIndex = getInvertedIndex(getContent("./set1/docs.txt"))
#dictionary = getDictionary("./set1/docs.txt")
searchDocument("./set1/docs.txt", "./set1/queries.txt")

