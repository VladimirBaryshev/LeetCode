# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

intervals_1 = [[1,3],[2,6],[8,10],[15,18]] # --> [[1,6],[8,10],[15,18]]

intervals_2 = [[1,4],[4,5]] # --> [[1,5]]

# May 12th, interview number 1


# Предложенное решение
'''
	1) [[1,4], [2,3], [9, 11]]
	time O(n*log n)
	space O(n)

	2) [[1, 4], [9, 11]]
	time O(n)
	space O(n)
'''

# Подсказка
'''
arr.sort(key=lambda x:x[0]) # Better way. Inplace operation saves memory
sorted(arr, key=lambda x:x[0])
'''

# Попытка решить

def main(intervals):
	if not intervals:
		return []
	result = []

	intervals.sort(key=lambda x: x[0])

	prev_starti, prev_endi = intervals[0]

	for starti, endi in intervals: # 
		if starti > prev_endi: 
			result.append([starti, endi])
		…
		result[-1] <= starti
		prev_starti, prev_endi = starti, endi

	return ...
			

'''
	sort an array
	2) compare prev_end with curr_start…
	create new array to store result

	time o(nlgn) = onlgn (sort) + o(n) for loop  => onlgn
	space o(n)

'''

# Feedback

'''
	- не спросил про условия оверлаппинга (сказал больше, но по факту надо было уточнить про больше или равно)
	- можно было решить простой тест кейс в начале чтобы лучше понять условия задачи и выявить паттерн
	- не обратил внимания что зашафлены данные (только в конце задачи понял)
	- сортировка неверная сложность
	- не знал деталей использования встроенной функции sort в питоне
	- не добавил условие что массив может быть пустой
	- использование индексов в питоне когда можно обойтиь без них for i in range(len) -> for interval in intervals (или если нужны индексы, то лучше for idx, val in enumerate
	- в for лупе не заметил, что не нужно сравнивать первый элемент с самим собой
	- ошибка в индексации result[-1] < starti, когда надо было result[-1][1]
'''

