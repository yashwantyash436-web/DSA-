class Solution:
    def maxDivScore(self, nums, divisors):
        max_score = -1
        answer = float('inf')

        for divisor in divisors:
            score = 0

            for num in nums:
                if num % divisor == 0:
                    score += 1

            if score > max_score:
                max_score = score
                answer = divisor
            elif score == max_score:
                answer = min(answer, divisor)

        return answer