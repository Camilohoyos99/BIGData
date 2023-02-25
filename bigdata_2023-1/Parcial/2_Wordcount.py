from mrjob.step import MRStep 
from mrjob.job import MRJob
import re
from collections import Counter
from nltk.tokenize import word_tokenize
import string

class BookAnalyzer(MRJob):

    def mapper(self, _, line):
        # Get the title and text fields from the input line
        title_start = line.find("Project Gutenberg eBook of ") + len("Project Gutenberg eBook of ")
        title_end = line.find(",", title_start)
        title = line[title_start:title_end]
        author_start = line.find("by ", title_end) + len("by ")
        author_end = line.find("\n", author_start)
        author = line[author_start:author_end]
        text = line[line.find("*** START OF THIS PROJECT GUTENBERG EBOOK", author_end):]

        # Remove punctuation and convert to lowercase
        text = text.translate(str.maketrans("", "", string.punctuation))
        text = text.lower()

        # Split the text into words and emit each word with a count of 1
        for word in text.split():
            if len(word) > 5:
                yield (word, 1)

        # Emit each title with a count of 1 to keep track of how many books include each word
        for word in set(text.split()):
            if len(word) > 5:
                yield (title + ":" + word, 1)

    def reducer_count_words(self, word, counts):
        # Calculate the total count of each word
        total = sum(counts)

        # If the word appears in all 15 books, emit it with its count
        if total == 15:
            yield None, (total, word)

    def reducer_sort_counts(self, _, word_counts):
        # Sort the word counts by count, in descending order
        sorted_word_counts = sorted(word_counts, reverse=True)

        # Emit the top 20 words
        for i in range(2):
            yield sorted_word_counts[i][1], sorted_word_counts[i][0]

    def steps(self):
        return [
            MRStep(mapper=self.mapper),
            MRStep(reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_sort_counts)
        ]

if __name__ == '__main__':
    BookAnalyzer.run()
