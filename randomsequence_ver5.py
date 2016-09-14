#! /usr/bin/env python
#Note, don't forget to change it to be executable using chmod 755 rectangle.py

#Goal is to create a random sequence generator where you tell is how many sequences you want, what length you want and what approximate GC content they are
#So to execute, once you are in the directory, type ./randomsequence.py 20 100 10 this will give you a GC content of about 20 for 10 of length 100

import sys
import random
file = open("randomsequences_practice.txt", "w")

def randomsequence(gccontent, base_length, total):
	bases=['A','G','C','T']
	p=float(gccontent)/100
	q=1-p
	seqcount=0
	while seqcount<total:
		seq=[]
		start=0
		gc_counter=0
		while start<base_length:
			letter=(random.choice(bases))
			if letter=='A':
				if random.random()<q:
					start=start+1
					seq.append(letter)
					my_string=''.join(seq)
			elif letter=='T':
				if random.random()<q:
					start=start+1
					seq.append(letter)
					my_string=''.join(seq)	
			elif letter=='G':
				if random.random()<p:
					start=start+1
					gc_counter=gc_counter+1
					seq.append(letter)
					my_string=''.join(seq)
			elif letter=='C':
				if random.random()<p:
					start=start+1
					gc_counter=gc_counter+1
					seq.append(letter)
					my_string=''.join(seq)
		seqcount=seqcount+1
		gc_proportion=float(gc_counter)/base_length
		header='> sequence.{} gccontent={} total length={}'.format(seqcount,gc_proportion,base_length)
		print(header)
		print(my_string)
		file.write(header +'\n')
		file.write(my_string +'\n')
		

sys.argv[0]  #accessing the name of the function
gccontent = int(sys.argv[1])  #integer part because going to be a string unless change it to define as integer
base_length = int(sys.argv[2])	 
total=int(sys.argv[3])
			
print(randomsequence(gccontent, base_length, total))	
file.close()
       
