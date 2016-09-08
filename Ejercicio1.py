def binsearchR(A,key,lo,hi):
	if lo > hi:
		return 0
	mid = lo + (hi-lo)//2
	if A[mid] < key:
		return binsearchR(A,key,mid+1,hi)
	elif A[mid] >key:
		return binsearchR(A,jey,lo,mid-1)
	else:
		return mid

def binary_searchR(A,key):
	return binsearchR(A,key,0,len(A) -1)

def SUM3N2LOGN(A):
	A.sort()
	N=len(A)
	count = 0
	for i in range(N):
		for j in range(i+1,N):
			if binary_searchR(A,-(A[i]+A[j])):
				count = count + 1
	return count


def SUM3N2(A):
	A.sort()
	h=hash(A)
	N=len(A)
	count = 0
	for i in range(N):
		for j in range(i+1, N):
			if hash(-(A[i]+A[j])):
				count = count + 1
	return count

if __name__ == '__main__':
	from timeit import Timer
	from sys import stdin
	A=[]
	for line in stdin:
		num = int(line)
		A.append(num)
	samples = 10
	t = Timer("SUM3N2","from __main__ import SUM3N2, A")
	t1 = Timer("SUM3N2LOGN","from __main__ import SUM3N2LOGN, A")
	took = t.timeit(samples)/samples
	took1 = t.timeit(samples)/samples
	print("SUM3N2 for {} integers took {} secs".format(len(A), took))