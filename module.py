from pymongo import MongoClient
import re;

#ayy lmao
# hi wayez
# FUNCTIONS TO MONGO

# KATHY
# authenticate
# newUser
# changePassword

# WAYEZ
# makePost
# getPost

# WINTON
# getPoster
# getAllPosts

# JERRY
# addToPost
# removePost

<<<<<<< HEAD
## two collections dbs: logins and posts
=======
## two mongo dbs: logins and posts
<<<<<<< HEAD
#HELLO. PULL REQUESTING

=======
#Winton: I think one db is ok?
>>>>>>> 5a5c72b34ab05435d7459817aad50a884a2571cf

connection = MongoClient()
<<<<<<< HEAD
database = connection['database']
=======
db = connection['db']
>>>>>>> e57053a8e2086e2ce881c0fa5a1ba80dfe0cc96f
>>>>>>> 651b8b77527fe0b7cfd2c2541ca528fa7c28d075

<<<<<<< HEAD
def authenticate(username, password):
    connection = MongoClient() 
    ans = db.logins.find({'username':username},{'password':password})
    for r in ans:
        return r;
    return "Bad";
=======
def sanitize(input):
    return re.sub('"', "  ", input)

def authenticate(username, password):
    username = sanitize(username)
<<<<<<< HEAD
    connection = MongoClient() 
    db = connection['logins']
    ans = db.logins.find({'username':username},{'password':password})
    for r in ans:
=======
"""    conn = sqlite3.connect("myDataBase.db")
    c = conn.cursor()
    ans = c.execute('select * from logins where username = "'+username+'" and password = "'+encrypt(username,password)+'";')
"""
     connection = MongoClient()
     db = connection['logins']
     ans = db.logins.find({'username':"'+username+'"},{'password':"'+encrypt(username,password)+'"})
     for document in ans:
>>>>>>> 651b8b77527fe0b7cfd2c2541ca528fa7c28d075
        return True;
    return False;
>>>>>>> 5a5c72b34ab05435d7459817aad50a884a2571cf
    #returns a boolean that describes whether the user has succesfully logged in.

def newUser(username,password):
    username = sanitize(username)
<<<<<<< HEAD
    ans = database.logins.find({username:True})
    for r in ans:
        return False
    d = {username:password}
    database.logins.insert(d)
=======
    
"""    conn = sqlite3.connect("myDataBase.db")
    c = conn.cursor()
    ans = c.execute('select * from logins where username = "%s";' % username)
"""

    connection = MongoClient()
    db = connection['logins']
    check = db.logins.find({'username':username}).count()
    if check != 0:
        return False

"""    ans = c.execute('insert into logins values("'+username+'","'+encrypt(username,password)+'");')
    conn.commit()
"""

    ans = db.users.insert_one({'username':username} ,{'password':password})
>>>>>>> 651b8b77527fe0b7cfd2c2541ca528fa7c28d075
    return True
    connection.close() 

def changePassword(username, oldPassword, newPassword):
    newPassword = sanitize(newPassword);
    username = sanitize(username);
    if(authenticate(username,oldPassword)):
 """      conn = sqlite3.connect("myDataBase.db")
       c = conn.cursor()
       c.execute('update logins set password = "%s" where username = "%s";' % (encrypt(username,newPassword), username))
       conn.commit()"""
       db = connection['logins']
       db.logins.update(
           {'username': username},
           {
               'username': username,
               'password': newPassword
           },
       )
       #untested
       return True
    return False

def makePost(username, title, contents):
    username = sanitize(username)
    title = sanitize(title)
    contents = sanitize(contents)

    connection = MongoClient()
    db = connection['posts']
    
#    conn = sqlite3.connect("myDataBase.db")
#    c = conn.cursor()
#    ans = c.execute('select * from posts where title = "%s";' % title)

    ans = db.posts.find({'title':title}) 
    for r in ans:
        return False;

   	db,data.insert([{'username':username, 'title':title, 'contents':contents, 'lastPoster':username}])
    return True;
    #adds a post to the databes from username with title = title and contents = contents
    #returns a boolean representing if the operation was successful
    #operation will be unsuccessful if a post with the same title already exists

def getPost(title):
    title = sanitize(title)
    ans = db.data.find({'title': title})
    for r in ans:
        return r[2];
    #returns the content of post with title = title
    #may only be useful for debugging

def getPoster(title):
    ayylmao = sanitize(title)
    ans = db.data.find({'title':ayylmao})
    for r in ans:
        return r[0]
    #returns the original poster of a story


def getAllPosts():
    ans = db.data.find()
    return ans
    #returns a 2d array where the first index represents row id. The second index works as follows:
    #the 0 index store sthe name of the original poster
    #the 1 index represents the title of the post
    #the 2 index stores the contents of the post.
    #the 3 index stores the last user to add to a post

def addToPost(username,title, content):
    title = sanitize(title)
    content = sanitize(content)
    conn = MongoClient()
    dbase = conn['posts']
    newContent = " "+getPost(title)+content
    ans = dbase.posts.find({'username':username,'title':title})
    for r in ans:
        return False
    dbase.data.update({'lastPoster':username, 'title': title})
    dbase.posts.update({'contents': newContent, 'title': title})
    return True;
    #adds content to content of original post and returns a boolean representing wether or not the operation was successful

def removePost(title):
    title = sanitize(title)
    conn = MongoClient()
    dbase = conn['posts']
    dbase.posts.remove({'title':title})
    return True;

    #removes post with tile=title from database if it exists and username = admin
    #returns false if operation failed
