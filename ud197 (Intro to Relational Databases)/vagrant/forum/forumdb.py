#
# Database access functions for the web forum.
# 

import time
import psycopg2

## Database connection
DB = psycopg2.connect("dbname=forum")

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    c = DB.cursor()
    c.execute("Select * from posts order by time desc")
    return c.fetchall()

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())
    cursor = DB.execute("insert into posts(content, current_timestamp)")
    DB.commit()
