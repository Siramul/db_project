
#List of all messages in the system     ***DONE***
sql = """SELECT * FROM message ;"""

#Number of likes to a message       ***DONE***
sql = """SELECT count(like_dislike) FROM like_dislike WHERE message_id = %s GROUP BY like_dislike HAVING like_dislike = TRUE ; """

#List of users who liked a message      ***DONE***
sql = """SELECT user_id, user_name FROM like_dislike natural inner join users WHERE message_id = %S AND like_dislike = TRUE;"""

#Number of dislikes to a message        ***DONE***
sql = """SELECT count(like_dislike) FROM like_dislike WHERE message_id = %s GROUP BY like_dislike HAVING like_dislike = FALSE ; """

#List of users who dislikes a message       ***DONE***
sql = """SELECT user_id, user_name FROM like_dislike natural inner join users WHERE message_id = %s AND like_dislike = FALSE; """

#List of users in the contact list of some user X       ***DONE***
sql = """SELECT users.first_name, users.last_name, users.e_mail, users.phone, users.user_name FROM users, contact WHERE contact.user_id = 1 AND contact.contact_id = users.user_id"""

#List of messages posted to a chat group        ***DONE***
sql = """SELECT * FROM message natural inner join contains WHERE chat_id = %s;"""

#List of users subscribed to a chat group       ***DONE***
sql = """SELECT user_id, user_name FROM users natural inner join member WHERE chat_id = %s"""

#List of users in the system           ***DONE***
sql = """SELECT first_name, last_name, e_mail, phone, user_name From users;"""

#List of chats group in the system      ***DONE***
sql = """Select * FROM chat"""

#Owner of a given chat group        ***DONE***
sql = """Select first_name, last_name, e_mail, phone, user_name FROM chat, users WHERE chat.manager = users.user_id AND chat_id = %s"""

#Information on a given user by id      ***DONE***
sql = """Select * From users WHERE user_id = %s"""

#Information on a given user by username    USER
sql = """Select * from users where user_name = '%s'"""
