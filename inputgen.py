k=1000
l = [i for i in range(1, k+1)]
li = []
for n in l:
	for m in (l):
		li.append( str(n) + " "+ str(m)+ " "+ str (abs(n-m))+"\n")
#li.pop()
#li.append("467 500 2\n")
pi = []
for n in l:
	pi.append(str (n) + " " + str(n*2)+ "\n")

v = k*(k+1)/2
fname = "input4.txt"
fo = open(fname, 'w')
fo.write("DFS\n")
fo.write('1\n')
fo.write('999\n')
fo.write(str(k*k)+'\n')
fo.writelines(li)
fo.write(str(k)+'\n')
fo.writelines(pi)