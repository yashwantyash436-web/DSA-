class Solution:
    def topKFrequent(self, words, k):

        # Step 1: Count how many times each word appears
        count = {}

        for word in words:
            count[word] = count.get(word, 0) + 1

        # Step 2: Convert dictionary into (word, frequency) pairs
        pairs = list(count.items())

        # Step 3: Sort using two rules:
        #         1. Higher frequency first
        #         2. If frequency is same, alphabetical order
        pairs.sort(key=lambda x: (-x[1], x[0]))

        # Step 4: Take only the first k words
        result = []

        for word, frequency in pairs[:k]:
            result.append(word)

        return result