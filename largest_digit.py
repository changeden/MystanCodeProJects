"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9
def find_largest_digit(n):
	"""
	:param n: parameter
	:return: max number.
	"""
	return find_largest_digit_helper(n, 0)

def find_largest_digit_helper(n,mx):

	if 0<= n <10:
		if n > mx:
			mx = n
		return mx
	elif n<0:

		return find_largest_digit_helper(-n,0)
	else:
		ans = int(n % 10)
		if ans > mx:
			mx = ans
			# return mx

		return find_largest_digit_helper(int(n/10),mx)



# def find_largest_digit_helper(n):
# 	if n<0:
# 		n=n*(-1)
# 		b=n/10
# 		ans = n-int(b)*10
# 		return ans
# 	else:
# 		b = n / 10
# 		ans = n - int(b) * 10
# 		return ans


# for i in range(4):
# 	ans=a-int(a/10)*10
# 	a=int(a/10)










	# if n<0:
	# 	n=n*(-1)
	# 	# print(n)
	# 	s=str(n)
	# 	if len(s)==1:
	# 		return n
	# 	else:
	# 		if int(s[0])>int(s[len(s)-1]):
	# 			return find_largest_digit(int(s[0:len(s)-1]))  #remove small
	# 		elif int(s[0])<int(s[len(s)-1]):
	# 			return find_largest_digit(int(s[1:len(s)]))   #remove small
	# 		elif int(s[0]) == int(s[len(s)-1]):
	# 			return find_largest_digit(int(s[1:len(s)]))  #去 one number
	# else:
	# 	n=n
	# 	# print(n)
	# 	s = str(n)
	# 	if len(s) == 1:
	# 		return n
	# 	else:
	# 		if int(s[0]) > int(s[len(s) - 1]):
	# 			return find_largest_digit(int(s[0:len(s) - 1]))  # remove small
	# 		elif int(s[0]) < int(s[len(s) - 1]):
	# 			return find_largest_digit(int(s[1:len(s)]))  # remove small
	# 		elif int(s[0]) == int(s[len(s) - 1]):
	# 			return find_largest_digit(int(s[1:len(s)]))  # 去 one number
	#
	# 			# 		return is_palindrome(s[1:len(s)-1])  #去頭去尾


if __name__ == '__main__':
	main()
