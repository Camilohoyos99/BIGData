from mrjob.job import MRJob
import re
import heapq
from mrjob.step import MRStep as mr
WORD_REGEX=re.compile(r"\b\w+\b")
class WordCount(MRJob):
# basic function of mapper, travers all the words that the method word_regex give 
	def mapper(self, _, line):
		words=WORD_REGEX.findall(line)
		for word in words:
			if len(word)>5:
				yield (word.lower(),1)
	
	def reducer (self, word, counts):# el reduce works word by word (but in box of the key)
		counts_sum = sum(counts)
		yield None, (counts_sum, word)
		
	def reducer_top10(self, _, counts):
		h = []
		for c, w in counts:
			if len(h) < 20:
				
					
				heapq.heappush(h, (c, w))
			else:
				heapq.heappushpop(h, (c, w))
				
		for c, w in sorted(h, reverse=True):
			yield w, c
	def steps(self):
		return [mr(mapper=self.mapper, reducer=self.reducer),
				mr(reducer=self.reducer_top10)
        ]

if __name__== "__main__":
	WordCount.run()


#python 2_Wordcount.py input/11 input/1497 input/1661 input/174 input/2147 input/2680 input/3207 input/70108 input/1228 input/1524 input/1727 input/2000 input/2148 input/3176 input/42671 >out.txt
