class Solution:
	def removeCoveredIntervals(self, intervals):
		intervals.sort(key=lambda x: (x[0], -x[1]))
		result = [intervals[0]]
		for interval in intervals[1:]:
			if result[-1][0] <= interval[0] and result[-1][1] >= interval[1]:
				continue
			result.append(interval)
		return len(result)