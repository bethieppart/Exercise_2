import psycopg2
import sys
import matplotlib.pyplot as plt
import numpy as np

#connect to the database
conn=psycopg2.connect(database='tcount', user="postgres", password="pass", host="localhost", port="5432")
curs=conn.cursor()

sql = "SELECT word, count FROM tweetwordcount ORDER by count DESC LIMIT 20;"
curs.execute(sql)

#put the results in a results array
recs = curs.fetchall()

#print recs

 
words = [x[0] for x in recs]
#print words
counts = [y[1] for y in recs]
#print counts
y_pos = np.arange(len(words))
print y_pos
 
plt.bar(y_pos, counts, alpha=0.5)
plt.xticks(y_pos, words, rotation=90)
plt.ylabel('Count')
plt.title('Top 20 Word Counts')
plt.xlim([0,len(words)])
 
#plt.show()
plt.savefig('barchart.png')

conn.commit()
conn.close()
