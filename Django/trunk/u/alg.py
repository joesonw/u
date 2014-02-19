
def merge(left,right):
	result=[]
	while len(left)>0 or len(right)>0:
		if len(left)>0 and len(right)>0:
			if left[0] <= right[0]:
				result.append(left[0])
				left = left[1:]
			else:
				result.append(right[0])
				right=right[1:]
		elif len(left)>0:
			result.append(left[0])
			left=left[1:]
		elif len(right)>0:
			result.append(right[0])
			right=right[1:]
	return result
	
def mergeSort(m):
	if len(m) <=1:
		return m
	mid=len(m)/2
	left=[x for x in m[:mid]]
	right=[x for x in m[mid:]]
	left=mergeSort(left)
	right=mergeSort(right)
	return merge(left,right)
	
t=[3,1,6,2,7,32,2,1,58,234,3212,2,13,12,213,21]
print t
t=mergeSort(t)
print t

# 
# function merge_sort(list m)
#     // if list size is 0 (empty) or 1, consider it sorted and return it
#     // (using less than or equal prevents infinite recursion for a zero length m)
#     if length(m) <= 1
#         return m
#     // else list size is > 1, so split the list into two sublists
#     var list left, right
#     var integer middle = length(m) / 2
#     for each x in m before middle
#          add x to left
#     for each x in m after or equal middle
#          add x to right
#     // recursively call merge_sort() to further split each sublist
#     // until sublist size is 1
#     left = merge_sort(left)
#     right = merge_sort(right)
#     // merge the sublists returned from prior calls to merge_sort()
#     // and return the resulting merged sublist
#     return merge(left, right)
			


# function merge(left, right)
#     var list result
#     while length(left) > 0 or length(right) > 0
#         if length(left) > 0 and length(right) > 0
#             if first(left) <= first(right)
#                 append first(left) to result
#                 left = rest(left)
#             else
#                 append first(right) to result
#                 right = rest(right)
#         else if length(left) > 0
#             append first(left) to result
#             left = rest(left)
#         else if length(right) > 0
#             append first(right) to result
#             right = rest(right)
#     end while
#     return result