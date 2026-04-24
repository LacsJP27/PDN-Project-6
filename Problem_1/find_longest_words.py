from mrjob.job import MRJob
import string

class FindLongestWord(MRJob):
    def mapper(self, _, line):
        # mapper logic
        translator = str.maketrans('', '', string.punctuation)

        line = line.lower().translate(translator)
        words = line.split(" ")
        for word in words:
            if word:
                yield (word[0], word)
        


        pass
    def reducer(self, key, values):
        # reducer logic
        pass