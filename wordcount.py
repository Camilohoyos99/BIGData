# Lab 1. Basic wordcount
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
# this is a regular expression that finds all the words inside a String
WORD_RE = re.compile(r"\b\w+\b")

# this line declares the class Lab1, that extends the MRJob format.
class Lab1(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,                   
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
            
        ]

    def mapper_get_words(self, _, line):
        # yield each word in the line
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)


    def reducer_count_words(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.

        yield None, (sum(counts), word)

    def reducer_find_max_word(self, _, word_count_pairs):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        yield max(word_count_pairs)

# this part of the python script tells to actually run the defined MapReduce job.
# Note that Lab1 is the name of the class
if __name__ == "__main__":
    Lab1.run()