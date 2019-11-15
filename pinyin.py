import pypinyin
f = open("name.txt","r")
f1 = open("pinyin_name.txt","a+")
for i in f.readlines():
	aa = pypinyin.lazy_pinyin(i)
	bb = ""
	for j in aa:
		bb +=str(j).strip("\n")
	# print(bb)
	f1.write(bb+"\n")
