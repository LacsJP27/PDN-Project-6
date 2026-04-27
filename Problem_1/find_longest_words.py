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
        
    def reducer(self, key, values):
        # reducer logic
        words = list(values)
        maxLen = 0
        res = set()

        for word in words:
            maxLen = max(len(word), maxLen)
        
    
        for word in words:
            if len(word) == maxLen:
                res.add(word)
        yield key, sorted(res)

if __name__ == '__main__':
    FindLongestWord.run()