"""
File: rotten_tomato.py
Name:
-------------------------------
This file shows basic AI in classification task:
movie review classification.
First, tokenize the review
Second, count each token and give them corresponding scores
Finally, calculate the score for each word such that we can
predict a movie review by summing over the scores
"""


# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	word_d={}
	with open(FILENAME,'r') as f:
		for line in f:
			elements =line.split(':')
			score= elements[0]
			score=int(score[1:3])
			review= elements[1]
			tokens=review.split()
			for token in tokens:
				token = token.lower()
				new_token = ''
				for ch in token:
					if ch.isalpha():    #ch is 字母

						new_token += ch
					#Case insensitive $no punctuation
				if new_token not in word_d:   #如果token 第一次出現
					word_d[new_token]=score      #
				else:
					word_d[new_token]+=score     #相加
	print(word_d)
	all_d = {'positive':[],'neutral':[],'negative':[]}

	for key,value in word_d.items():    #key = word, value = score
		if value>0:
			all_d['positive'].append(key)
		elif value ==0:
			all_d['neutral'].append(key)
		else:
			all_d['negative'].append(key)
	print(all_d)


if __name__ == '__main__':
	main()
