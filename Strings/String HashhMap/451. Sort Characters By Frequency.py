class Solution:
    def frequencySort(self, s):

        # Step 1: Count the frequency of each character
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Step 2: Convert dictionary into (character, frequency) pairs
        pairs = list(count.items())

        # Step 3: Sort by frequency, highest → lowest
        pairs.sort(key=lambda x: x[1], reverse=True)

        # Step 4: Build the answer
        answer = ""

        for ch, frequency in pairs:
            # Repeat each character according to its frequency
            answer += ch * frequency

        return answer
        #leave