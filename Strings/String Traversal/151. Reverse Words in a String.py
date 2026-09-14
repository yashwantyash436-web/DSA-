class Solution:
    def reverseWords(self, s) :

        # Split the sentence into individual words
        split = s.split()

        # Reverse the list of words in-place
        split.reverse()

        # Join the reversed words with a single space
        answer = " ".join(split)

        # Return the final string
        return answer

       # class Solution:
    #def reverseWords(self, s: str) -> str:

        #result = []
       # word = ""

        # Traverse from right to left
        #for i in range(len(s) - 1, -1, -1):
            #ch = s[i]

            #if ch != ' ':
             #   word += ch
            #else:
                # Space means the current word is complete
               # if word:
                  #  result.append(word)
                  #  word = ""

        # Add the first word
      #  if word:
           # result.append(word)

        # Join words with a single space
        #answer = ""
        #for i in range(len(result)):
           # answer += result[i]

            #if i < len(result) - 1:
               # answer += " "

       # return answer


        #leave(2)