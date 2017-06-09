#! /usr/bin/env
#PROJECT:-LOG ANALYSIS
import psycopg2
import time
def connect():
    return psycopg2.connect("dbname=news")

query1="select title,views from article_view limit 3"
query2="select * from author_view"
query3="select to_char(date,'Mon DD,YYYY') as date,err_prc from err_perc where err_prc>1.0"

def popular_article(query1):
    db=connect()
    c=db.cursor()
    c.execute(query1)
    results=c.fetchall()
    for i in range(len(results)):
        title=results[i][0]
        views=results[i][1]
        print("%s--%d" % (title,views))
    db.close()

def popular_authors(query2):
    db=connect() 
    c=db.cursor()
    c.execute(query2)
    results=c.fetchall()
    for i in range(len(results)):
        name=results[i][0]
        views=results[i][1]
        print("%s--%d" % (name,views))
    db.close()

def error_percent(query3):
    db=connect()
    c=db.cursor()
    c.execute(query3)
    results=c.fetchall()
    for i in range(len(results)):
        date=results[i][0]
        err_prc=results[i][1]
        print("%s--%.1f %%" %(date,err_prc))

if __name__ == "__main__":
  print("THE LIST OF POPULAR ARTICLES ARE:")
  popular_article(query1)
  print("\n")
  print("THE LIST OF POPULAR AUTHORS ARE:")
  popular_authors(query2)
  print("\n")
  print("PERC ERROR MORE THAN 1.0:")
  error_percent(query3)
    
    
