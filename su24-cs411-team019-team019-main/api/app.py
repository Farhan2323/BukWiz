from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import string
import datetime
import pymysql

app = Flask(__name__)
CORS(app)

sessions = {}

connection = pymysql.connect(host='35.224.70.186',
                             user='root',
                             password='/Gh8#1g/6VS`c]>q',
                             database='bukwiz',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route("/getPosts", methods=["GET"])
def getPosts():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        sql = """
            SELECT *
            FROM Post
            ORDER BY postDate DESC
            LIMIT 5;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

@app.route("/getBookInfo", methods=["POST"])
def getBookInfo():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        sql = """
            SELECT *
            FROM Book
            WHERE bookId = %s;
        """
        bookId = request.form.get("bookId")
        cursor.execute(sql, (bookId))
        result = cursor.fetchone()
    return jsonify(result)

@app.route("/getBooks", methods=["POST"])
def getBooks():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        sortBy = request.form.get("sortBy")
        genres = request.form.get("genres", None)
        title = request.form.get("title", None)
        inStock = request.form.get("inStock", False)
        if inStock == "true":
            inStock = True
        else:
            inStock = False
        if inStock:
            if genres is not None:
                if title is not None:
                    sql = """
                        SELECT *
                        FROM Book NATURAL JOIN Stock
                        WHERE genres = %s AND title LIKE CONCAT('%%', %s, '%%') AND quantity > 0
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (genres, title, sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
                else:
                    sql = """
                        SELECT *
                        FROM Book NATURAL JOIN Stock
                        WHERE genres = %s AND quantity > 0
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (genres, sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
            else:
                if title is not None:
                    sql = """
                        SELECT *
                        FROM Book NATURAL JOIN Stock
                        WHERE title LIKE CONCAT('%%', %s, '%%') AND quantity > 0
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (title, sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
                else:
                    sql = """
                        SELECT *
                        FROM Book NATURAL JOIN Stock 
                        WHERE quantity > 0
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
        else:
            if genres is not None:
                if title is not None:
                    sql = """
                        SELECT *
                        FROM Book
                        WHERE genres = %s AND title LIKE CONCAT('%%', %s, '%%')
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (genres, title, sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
                else:
                    sql = """
                        SELECT *
                        FROM Book
                        WHERE genres = %s
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (genres, sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
            else:
                if title is not None:
                    sql = """
                        SELECT *
                        FROM Book
                        WHERE title LIKE CONCAT('%%', %s, '%%')
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (title, sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
                else:
                    sql = """
                        SELECT *
                        FROM Book
                        ORDER BY %s DESC
                        LIMIT 1000;
                    """
                    sql = cursor.mogrify(sql, (sortBy))
                    sql = sql.replace(f"'{sortBy}'", sortBy)
                    cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

@app.route("/getSeries", methods=["POST"])
def getSeries():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        sortBy = request.form.get("sortBy")
        series = request.form.get("title", None)
        inStock = request.form.get("inStock", True)
        if inStock == "true":
            inStock = True
        else:
            inStock = False
        if inStock:
            if series is not None:
                sql = """
                    SELECT b.series, AVG(b.rating) AS avgRating
                    FROM Book b NATURAL JOIN Stock s
                    GROUP BY b.series
                    HAVING b.series LIKE CONCAT('%%', %s, '%%') AND SUM(s.quantity) >= COUNT(s.quantity)
                    ORDER BY %s DESC
                    LIMIT 1000;
                """
                sql = cursor.mogrify(sql, (series, sortBy))
                sql = sql.replace(f"'{sortBy}'", sortBy)
                cursor.execute(sql)
            else:
                sql = """
                    SELECT b.series, AVG(b.rating) AS avgRating
                    FROM Book b NATURAL JOIN Stock s
                    GROUP BY b.series
                    HAVING SUM(s.quantity) >= COUNT(s.quantity)
                    ORDER BY %s DESC
                    LIMIT 1000;
                """
                sql = cursor.mogrify(sql, (sortBy))
                sql = sql.replace(f"'{sortBy}'", sortBy)
                cursor.execute(sql)
        else:
            if series is not None:
                sql = """
                    SELECT b.series, AVG(b.rating) AS avgRating
                    FROM Book b
                    GROUP BY b.series
                    HAVING b.series LIKE CONCAT('%%', %s, '%%')
                    ORDER BY %s DESC
                    LIMIT 1000;
                """
                sql = cursor.mogrify(sql, (series, sortBy))
                sql = sql.replace(f"'{sortBy}'", sortBy)
                cursor.execute(sql)
            else:
                sql = """
                    SELECT b.series, AVG(b.rating) AS avgRating
                    FROM Book b
                    GROUP BY b.series
                    ORDER BY %s DESC
                    LIMIT 1000;
                """
                sql = cursor.mogrify(sql, (sortBy))
                sql = sql.replace(f"'{sortBy}'", sortBy)
                cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

@app.route("/login", methods=["POST"])
def login():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        username = request.form.get("username")
        password = request.form.get("password")
        sql = """
            SELECT *
            FROM User
            WHERE username = %s AND password = %s;
        """
        cursor.execute(sql, (username, password))
        result = cursor.fetchall()
        cookie = None
        if len(result) > 0:
            cookie = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=16))
            sessions[cookie] = result[0]["username"]
    return jsonify({"cookie": cookie})

@app.route("/getUserInfo", methods=["POST"])
def getUserInfo():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        sql = """
            SELECT *
            FROM User
            WHERE username = %s;
        """
        cursor.execute(sql, (username))
        result = cursor.fetchone()
    return jsonify(result)

@app.route("/post", methods=["POST"])
def post():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        bookId = request.form.get("bookId", None)
        content = request.form.get("content")
        sql = """
            INSERT INTO Post 
            VALUES ((SELECT MAX(t.postId) FROM Post t) + 1, %s, %s, %s, %s);
        """
        postDate = datetime.datetime.utcnow()
        postDate = postDate.strftime(r'%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (bookId, username, postDate, content))
    connection.commit()
    return "OK", 200

@app.route("/incrementScore", methods=["POST"])
def incrementScore():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        sql = """
            UPDATE User
            SET score = score + 3
            WHERE username = %s;
        """
        cursor.execute(sql, (username))
    connection.commit()
    return "OK", 200

@app.route("/getLeaderboard", methods=["GET"])
def getLeaderboard():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        sql = """
            SELECT username, score
            FROM User
            ORDER BY score DESC
            LIMIT 5;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)

@app.route("/getRandomBookInfo", methods=["POST"])
def getRandomBookInfo():
    connection.ping(reconnect=True)
    count = request.form.get("count")
    with connection.cursor() as cursor:
        sql = """
            SELECT *
            FROM Book;
        """
        cursor.execute(sql)
        result = random.sample(cursor.fetchall(), int(count))
    return jsonify(result)

@app.route("/borrowBook", methods=["POST"])
def borrowBook():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        bookId = request.form.get("bookId")
        transactionDate = datetime.datetime.utcnow()
        transactionDate = transactionDate.strftime(r'%Y-%m-%d %H:%M:%S')
        quantity = 1
        sql = """
            CALL NewBorrow(%s, %s, %s, %s);
        """
        cursor.execute(sql, (bookId, username, transactionDate, quantity))
    connection.commit()
    return "OK", 200

@app.route("/returnBook", methods=["POST"])
def returnBook():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        bookId = request.form.get("bookId")
        transactionDate = datetime.datetime.utcnow()
        transactionDate = transactionDate.strftime(r'%Y-%m-%d %H:%M:%S')
        quantity = 1
        sql = """
            CALL NewReturn(%s, %s, %s, %s);
        """
        cursor.execute(sql, (bookId, username, transactionDate, quantity))
    connection.commit()
    return "OK", 200

@app.route("/reserveBook", methods=["POST"])
def reserveBook():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        bookId = request.form.get("bookId")
        reservationDate = datetime.datetime.utcnow()
        reservationDate = reservationDate.strftime(r'%Y-%m-%d %H:%M:%S')
        quantity = 1
        sql = """
            INSERT INTO Reservation
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(sql, (bookId, username, reservationDate, quantity))
    connection.commit()
    return "OK", 200

@app.route("/getFavoriteGenres", methods=["POST"])
def getFavoriteGenres():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        sql = """
            CALL GetFavoriteGenres(%s);
        """
        cursor.execute(sql, (username))
        result = cursor.fetchall()
    return jsonify(result)

@app.route("/getFavoriteAuthors", methods=["POST"])
def getFavoriteAuthors():
    connection.ping(reconnect=True)
    with connection.cursor() as cursor:
        cookie = request.form.get("cookie")
        username = sessions[cookie]
        sql = """
            CALL GetFavoriteAuthors(%s);
        """
        cursor.execute(sql, (username))
        result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=False, processes=1)
