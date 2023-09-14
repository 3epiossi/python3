class Solution:
    def candy(self, ratings: List[int]) -> int:
      hp = []
      for i, rating in enumerate(ratings):
        hp.append((rating, i))
      heapq.heapify(hp)
      giving = [0 for i in range(len(ratings))]
      while hp:
        rating, i = heapq.heappop(hp)
        noLess = 0
        if i-1 >= 0 and ratings[i-1] < rating:
          noLess = giving[i-1]
        if i+1 < len(ratings) and ratings[i+1] < rating:
          noLess = max(noLess, giving[i+1])
        giving[i] = noLess+1
      return sum(giving)