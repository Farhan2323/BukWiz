# Database Implementation

We created our database on Google Cloud Platform.

![connection](/img/connection.png)

## Tables

We implemented six tables in our database: User, Book, Stock, Transaction, Post, and Reservation. We used the following SQL DDL commands to do so.

### User
```
CREATE TABLE User(
    username VARCHAR(32),
    password VARCHAR(32),
    score INT,
    PRIMARY KEY(username)
);
```

![user_count](/img/user_count.png)

### Book
```
CREATE TABLE Book(
    bookId INT UNSIGNED,
    title VARCHAR(256),
    series VARCHAR(256),
    author VARCHAR(256),
    rating REAL UNSIGNED,
    description TEXT,
    language VARCHAR(256),
    isbn BIGINT UNSIGNED,
    genres VARCHAR(256),
    characters TEXT,
    bookFormat VARCHAR(256),
    edition VARCHAR(256),
    pages INT UNSIGNED,
    publisher VARCHAR(256),
    publishDate DATE,
    firstPublishDate DATE,
    awards TEXT,
    numRatings INT UNSIGNED,
    ratingsByStars VARCHAR(256),
    likedPercent REAL,
    setting TEXT,
    coverImg VARCHAR(256),
    bbeScore INT,
    bbeVotes INT,
    price REAL UNSIGNED,
    PRIMARY KEY(bookId)
);
```

![book_count](/img/book_count.png)

### Stock
```
CREATE TABLE Stock(
    bookId INT UNSIGNED,
    quantity INT UNSIGNED,
    FOREIGN KEY(bookId) REFERENCES Book(bookId),
    PRIMARY KEY(bookId)
);
```

![stock_count](/img/stock_count.png)

### Transaction
```
CREATE TABLE Transaction(
    bookId INT UNSIGNED,
    username VARCHAR(32),
    transactionDate DATE,
    quantity INT UNSIGNED,
    type VARCHAR(32),
    FOREIGN KEY(bookId) REFERENCES Book(bookId),
    FOREIGN KEY(username) REFERENCES User(username),
    PRIMARY KEY(bookId, username, transactionDate)
);
```

![transaction_count](/img/transaction_count.png)

### Post
```
CREATE TABLE Transaction(
    bookId INT UNSIGNED,
    username VARCHAR(32),
    transactionDate DATE,
    quantity INT UNSIGNED,
    type VARCHAR(32),
    FOREIGN KEY(bookId) REFERENCES Book(bookId),
    FOREIGN KEY(username) REFERENCES User(username),
    PRIMARY KEY(bookId, username, transactionDate)
);
```

![post_count](/img/post_count.png)

### Reservation
```
CREATE TABLE Reservation(
    bookId INT UNSIGNED,
    username VARCHAR(32),
    reservationDate DATE,
    quantity INT UNSIGNED,
    FOREIGN KEY(bookId) REFERENCES Book(bookId),
    FOREIGN KEY(username) REFERENCES User(username),
    PRIMARY KEY(bookId, username, reservationDate)
);
```

![reservation_count](/img/reservation_count.png)

## Advanced Queries

### Advanced Query 1
```
SELECT title, r.popularity
FROM Book b NATURAL JOIN (
    SELECT t.bookId, COUNT(t.transactionDate) AS popularity
    FROM Transaction t
    GROUP BY t.bookId
) r
ORDER BY r.popularity DESC;
```

We implemented a query to find the popularity of a book by the number of times it was part of a transaction. To do so, we had to use a join and a subquery.

![adv_qry_1_1](/img/adv_qry_1_1.png)
![adv_qry_1_2](/img/adv_qry_1_2.png)
![adv_qry_1_3](/img/adv_qry_1_3.png)
![adv_qry_1_4](/img/adv_qry_1_4.png)

### Advanced Query 2
```
SELECT genres
FROM Book b NATURAL JOIN (
    SELECT DISTINCT t.bookId
    FROM Transaction t
    WHERE t.username = name
) r;
```

We implmented a query to find the genres of books a person reads. Replacing 'name' by the username of the person of interest gets the list of genres they read.

![adv_qry_1_1](/img/adv_qry_2_1.png)
![adv_qry_1_2](/img/adv_qry_2_2.png)

In this query, we used ```name = "Aaliyah Nelson"```. Since the sample person only read four genres of books that we have data on, it listed only four named genres. Aaliyah Nelson also read a book that we do not have genre data on, so it lists 'null' as well.

### Advanced Query 3
```
SELECT b.title, p.popularity
FROM Book b NATURAL JOIN (
    SELECT p.bookId, COUNT(p.post) AS popularity
    FROM Post p
    GROUP BY p.bookId
) p
ORDER BY p.popularity DESC;
```

We implemented a query to find the most discussed books in our posts system.

![adv_qry_1_1](/img/adv_qry_3_1.png)
![adv_qry_1_2](/img/adv_qry_3_2.png)
![adv_qry_1_1](/img/adv_qry_3_3.png)
![adv_qry_1_2](/img/adv_qry_3_4.png)

### Advanced Query 4
```
SELECT b.series, AVG(b.rating) AS avg_rating
FROM Book b NATURAL JOIN Stock s
WHERE SUM(b.quantity) > 0
GROUP BY b.series
ORDER BY AVG(b.rating) DESC;
```

We implemented a query to find the average rating of books in each book series that has at least one book currently available in the library.

![adv_qry_1_1](/img/adv_qry_4_1.png)
![adv_qry_1_2](/img/adv_qry_4_2.png)
![adv_qry_1_1](/img/adv_qry_4_3.png)
![adv_qry_1_2](/img/adv_qry_4_4.png)

## Indexing

### Advanced Query 1

We start the with only the default indexing.

![adv_qry_1_no_idx](/img/adv_qry_1_no_idx.png)

We then index by 'bookId' in the 'Transaction' table.

![adv_qry_1_bookId_idx](/img/adv_qry_1_bookId_idx.png)

We then index by 'title' in the 'Book' table.

![adv_qry_1_title_idx](/img/adv_qry_1_title_idx.png)

Finally we index on both 'bookId' in the 'Transaction' table and 'title' in the 'Book' table.

![adv_qry_1_bookId_title_idx](/img/adv_qry_1_bookId_title_idx.png)

None of the indexes provided any benefit to our first advanced query. The most natural candidates for indexing are 'bookId' for both the 'Book' table and the 'r' table since we join by that, but 'bookId' is the pimary key for 'Book' and 'r' is generated by a subquery, meaning we can't apply an indexing to it. We could index by 'bookId' in the 'Transaction' table since we use group by bookId in the subsquery, but that also did not provide any benefit, potentially because we have to look at all bookIds. The only remaining attribute of interest is 'title' in the 'Book' table, but indexing by this also did not provide any benefit, most likely because we are only selecting the title and not using it for anything else. As such, we will maintain with the default indexing.

### Advanced Query 2

We start with only the default indexing.

![adv_qry_2_no_idx](/img/adv_qry_2_no_idx.png)

We then index by 'username' in the 'Transaction' table.

![adv_qry_2_username_idx](/img/adv_qry_2_username_idx.png)

We then index by 'genres' in the 'Book' table.

![adv_qry_2_genres_idx](/img/adv_qry_2_genres_idx.png)

Finally we index on 'bookId' in the 'Transaction' table.

![adv_qry_2_bookId_idx](/img/adv_qry_2_bookId_idx.png)

Like for the last query, the most natural candidates for indexing are 'bookId' for the 'Book' and 'r' table, but 'r' was generated by a subquery and 'bookId' is the primary key for 'Book'. So, we choose to index by 'username' in 'Transaction' since it is used in the where statement in the subquery, but this did not provide any benefit, in fact, the query did not appear to even use the indexing. We also try indexing 'genre' from the 'Book' table and 'bookId' from the 'Transaction' table, but these also do not provide benefit, likely because they are only used in the select statement. As such, we will maintain with the default indexing.

### Advanced Query 3

We start with only the default indexing.

![adv_qry_3_no_idx](/img/adv_qry_3_no_idx.png)

We then index by 'bookId' in the 'Post' table.

![adv_qry_3_bookId_idx](/img/adv_qry_3_bookId_idx.png)

We then index by 'title' in the 'Book' table.

![adv_qry_3_title_idx](/img/adv_qry_3_title_idx.png)

Finally we index on 'bookId' in the 'Post' table and 'title' in the 'Book' table.

![adv_qry_3_bookId_title_idx](/img/adv_qry_3_bookId_title_idx.png)

This query has the same natural candidate problem like in the first and second query. We group by 'bookId', so we index it on the 'Post' table. The explain analyze shows that we do use this index, but it does provide any benefit to do so. Since we are not choosing a range or specific bookId, this might be why it provided us with no benefit. We also index on the 'title' in the 'Book' table, which makes this query more expensive. Indexing both also causes the same cost increase as indexing on 'title' alone. Note that 'Post_ibfk_1' is the same as 'bookId' in the explain analyze. The name change occured due to having to drop and re-add the foreign key property to 'bookId' in the 'Post' table in order to remove our indexing. As such, we will maintain with the default indexing.

### Advanced Query 4

We start with only the default indexing.

![adv_qry_4_no_idx](/img/adv_qry_4_no_idx.png)

We then index by 'series' in the 'Book' table.

![adv_qry_4_series_idx](/img/adv_qry_4_series_idx.png)

We then index by 'quantity' in the 'Stock' table.

![adv_qry_4_quantity_idx](/img/adv_qry_4_quantity_idx.png)

Finally we index by 'rating' in the 'Book' table.

![adv_qry_4_rating_idx](/img/adv_qry_4_rating_idx.png)

A natural candidate for indexing is 'series' in the 'Book' table since it is used a group by statement, but this provided no benefit. This might be because we are still looking at all series, and not choosing a specific one. A second natural candidate is 'quantity' in the 'Stock' table since it is used in a where statement. This indexing does provide a benefit, but only slightly so. We also attempted to index by 'rating' in the 'Book' table, but this did not provide a benefit, likely since we are not using rating directly, but rather in an aggregation function. As such, we will use an indexing of 'quantity' on the 'Stock' table.
