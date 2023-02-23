from mrjob.job import MRJob
import re
import heapq

WORD_REGEX = re.compile('[\W_]+')

class WordCount2(MRJob):

    def mapper(self, _, line):
        words = [WORD_REGEX.sub('', word.lower()) for word in line.split()]
        for word in words:
            yield (word, 1)

    def reducer(self, word, counts):
        counts_sum = sum(counts)
        yield None, (counts_sum, word)

    def reducer_top10(self, _, counts):
        h = []
        for c, w in counts:
            if len(h) < 10:
                heapq.heappush(h, (c, w))
            else:
                heapq.heappushpop(h, (c, w))
        for c, w in sorted(h, reverse=True):
            yield w, c

    def steps(self):
        return [
            self.mrjob(mapper=self.mapper, reducer=self.reducer),
            self.mrjob(reducer=self.reducer_top10)
        ]

if __name__ == '__main__':
    WordCount2.run()
