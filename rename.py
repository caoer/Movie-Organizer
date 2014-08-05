import re
fr= open('filenameslist.txt','r')
fw= open('movienames.txt','w')
for line in fr:
    text =line.strip()
    text1 = re.search('([^\\\]+)\.(avi|mkv|mpeg|mpg|mov|mp4)$',text)
    if text1:
        text = text1.group(1)
    text=text.replace('.',' ').lower()
    text2= re.search('(.*?)(dvdrip|xvid| cd[0-9]|dvdscr|brrip|divx|[\{\(\[]?[0-9]{4}).*',text)
    if text2:
        text =text2.group(1)
    text3= re.search('(.*?)\(.*\)(.*)',text)
    if text3:
            text =text3.group(1)
    #print text
    fw.write(text+'\n')
fr.close()
fw.close()
