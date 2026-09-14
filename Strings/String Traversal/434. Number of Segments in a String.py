class Solution:
    def countSegments(self, s) :
        
        segments = s.split()
        
        count = len(segments)
        
        return count

        #class Solution:
   # def countSegments(self, s: str) -> int:

        #count = 0
        #inside_segment = False

        #for ch in s:

            #if ch == ' ':
               # inside_segment = False

           # elif not inside_segment:
               # count += 1
               # inside_segment = True

       # return count