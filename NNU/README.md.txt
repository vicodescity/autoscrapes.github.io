This was my very first webscraping project with python.
The project was for a website called NNu.ng
This is the full link ---->https://www.nnu.ng

So the site pays you for every posts you open(The ones that have a time text attached to it), since there are alot of posts,
he wanted to automate it. So i divided the project into three steps.

Step 1 --- A text file where the post links would be stored.

Step 2 --- A script/python file which would scrape all the links for the posts(This is the generate file).
  By links i am referring to the href attributes, since the link texts where divided into a list and span tag, i decided to 
  generate all href values on the front page(i know not the best option, but that was the most logical way to get it) and then write it to the file  
  we created.

step 3 --- The main script that automates the whole process. First of all it enters the login page, and then inputs his username and password and then
  clicks the login button, then  after that it clicks the link to the Front Page, and then it opens the text file that the posts links where generated
  to.
  It creates a for loop and reads the lines from the text file.
  To fix the issue from step 2 where it generated all the links from the front page, it simply reads from the line where the posts that which is 63 to
  where it stoppd at -17.
  And then it goes back to the front page and then reads another line from the text file.
  It does until the last post.