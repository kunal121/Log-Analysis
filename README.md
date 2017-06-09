#LOG ANALYSIS

This project is part of Full Stack Nanodegree 

Aim of this project is to print report based on data in database by using python(2.7.10) 
and postgresql

### How To Install
1.Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2.Download or clone from github [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
3.Now we got newsdata.sql in our vagrant directory and now we are good to go.

###How to run
1.change directory to vagrant directory then
2.**vagrant up** command to run the vagrant on vm
3.**vagrant ssh** to login into vm
4.change directory to vagrant
5.use command **psql -d news -f newsdata.sql** to load database
  -use **\c** to connect to database="news"
  -use **\dt** to see the tables in database
  -use **\dv** to see the views in database
  -use **\q** to quit the database
6.use command **python log.py** to run the programm


###PSQL Command Used To create the view
-article_view
```CREATE VIEW article_view AS
SELECT title,
       author,
       count(title) AS views
FROM articles,
     log
WHERE log.path LIKE concat('%',articles.slug)
GROUP BY articles.title,
         articles.author
ORDER BY views DESC;```


1.author_view
``` CREATE VIEW author_view AS
SELECT name,
       sum(article_view.views) AS total
FROM article_view,
     authors
WHERE authors.id=article_view.author
GROUP BY authors.name
ORDER BY total DESC; ```


2.total_request
```
CREATE VIEW total_request AS
SELECT count(*) AS COUNT,
       date(TIME) AS date
FROM log
GROUP BY date
ORDER BY COUNT DESC;
```

3.error_request
```
CREATE VIEW error_request AS
SELECT count(*) AS COUNT,
       date(TIME) AS date
FROM log
WHERE status!='200 OK'
GROUP BY date
ORDER BY COUNT DESC;
```

4.err_perc
```
CREATE VIEW err_perc AS
SELECT total_request.date,
       round((100.0*error_request.count)/total_request.count,2) AS err_prc
FROM error_request,
     total_request
WHERE error_request.date=total_request.date;
```

