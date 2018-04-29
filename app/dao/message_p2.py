from app.config.dbconfig import pg_config
import psycopg2


class MessageDao:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    #List of all messages in the system
    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = """SELECT message.message_id, users.user_name, message.content, message.reply_id, message.time_stamp, message.likes, message.dislikes
                    FROM (SELECT *,
                             (SELECT COUNT(like_dislike)
                              FROM like_dislike
                              WHERE like_dislike = true and message_id = msg.message_id) likes,
                             (SELECT COUNT(like_dislike)
                              FROM like_dislike
                              WHERE like_dislike = false and message_id = msg.message_id) dislikes
                          FROM message msg) message, users
                    WHERE message.sender = users.user_id
                    ORDER BY message.time_stamp DESC;"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Number of likes to a message
    def getNumberOfLikes(self, message_id):
        cursor = self.conn.cursor()
        query = """SELECT COALESCE((SELECT count(like_dislike) FROM like_dislike WHERE message_id = %s GROUP BY like_dislike HAVING like_dislike = TRUE),0) ; """
        cursor.execute(query, (message_id,))
        result = cursor.fetchone()
        return result

    # List of users who liked a message
    def getUsersThatLikeAMessage(self, message_id):
        cursor = self.conn.cursor()
        query = """SELECT user_id, user_name FROM like_dislike natural inner join users WHERE message_id = %s AND like_dislike = TRUE;"""
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Number of dislikes to a message
    def getNumberOfDislikes(self, message_id):
        cursor = self.conn.cursor()
        query = """SELECT COALESCE((SELECT count(like_dislike) FROM like_dislike WHERE message_id = %s GROUP BY like_dislike HAVING like_dislike = FALSE),0) ;"""
        cursor.execute(query, (message_id,))
        result = cursor.fetchone()
        return result


    # List of users who dislikes a message
    def getUsersThatDislikeAMessage(self, message_id):
        cursor = self.conn.cursor()
        query = """SELECT user_id, user_name FROM like_dislike natural inner join users WHERE message_id = %s AND like_dislike = FALSE;"""
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


