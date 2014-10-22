#! \bin\user\python
import sys,re
alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def edits1(word):
	   l=[]
	   l1=[]
	   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	   deletes    = [a + b[1:] for a, b in splits if b]
	   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	   inserts    = [a + c + b     for a, b in splits for c in alphabet]
	   l=[x[0] for x in splits if len(x[0])>1]
	   l1=[x[1] for x in splits if len(x[1])>1]
	   deletes1=deletes+transposes+replaces+inserts+l+l1
	   upper_list=[x[0].upper()+x[1:] for x in deletes1]
	   #print upper_list
	   insert_comma=[a[:-1]+"'"+a[-1] for a in deletes1 if a[-1]=='s' or a[-1]=='t'] 
	 #  print deletes1
	   return set(deletes + transposes + replaces + inserts + insert_comma + l + l1 + upper_list) 

#def dist_2(word,list):
#	  return (set( a for b in edits1(word) for a in edits1(b) if a in list ))

	   
def final_check(word):
	#print d
	#print d.has_key('dismember')
	arrng=edits1(word)
	#print arrng
	l=[]
	for a in arrng:
		l.append(a)
	#print l
	#print d
	for a in l:
		#print a
		if d.has_key(a):
			#print a
			l_ans.append(a)
	#print l_ans
	return set(l_ans)

	   
list=[]
f=open("words.txt")
while 1:
	x=f.readline()
	#print x
	if len(x)==0:
		break
	x=x.split('\n')
	list.append(x[0])
	   #return a
d={}
#print list
list.sort()
for i in range(len(list)):
	d[list[i]]=i
#print d
del d['']
#print d
l=[]
l_ans=[]
l_ans1=[]
l_ans2=[]
#print d.has_key('ts')
y=sys.argv[1]
x=d.has_key(y)
#print x
if x:
	print "The word is correctly spelt."
	exit()
else:
	print "The word is incorrectly spelt. The nearest options are :"
	word=y
	word=re.sub('[0-9]|[!,@,#,$,%,^,&,*,(,),<,>,?,/]','',word)
	word=word.lower()
#	print word
	set_ans=final_check(word)
#	print set_ans
#	print set_ans
	for a in set_ans:
		l_ans1.append(a)
	if len(l_ans1)>=5:
		for i in range(5):
			print l_ans1[i]
		#	print "hi"
		exit()
	if len(l_ans)< 5:
	  set_ans1=set([])
	  for a in l_ans1:
		set_ans1=set_ans1.union(final_check(a))
	  for x in set_ans:
		set_ans1.discard(x)
	  
	  n=5-len(l_ans1)
	  for x in set_ans1:
		l_ans2.append(x)
	  if len(l_ans2)>=n:
                l_ans1=l_ans1+map(lambda i:l_ans2[i],range(n))
	if len(l_ans1)>=5:
		for i in range(5):		
			print l_ans1[i]
		exit
	if len(l_ans1)==0:
	  	l_ans1.append(word[0])
	  	
	if len(l_ans1)<5:
	  	n=5-len(l_ans1)
	  	#print n
	  	p=d[l_ans1[len(l_ans1)-1]]
		#print p
	  	for i in range(n+1):
			print list[p+i] 
		exit()
	
#	print set_ans
#	print map(lambda i:l_ans[i],range(13))
	
