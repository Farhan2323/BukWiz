# Reference

This document is only for referencing triggers, procedures, etc. that are used in the backend API.

```
CREATE TRIGGER HandleReservation
AFTER INSERT ON Transaction
FOR EACH ROW
BEGIN
    DECLARE curReservationUsername VARCHAR(32);
    DECLARE curReservationDate DATE;
    
    IF NEW.type = 'return' THEN
        IF 0 < (
            SELECT COUNT(bookId)
            FROM Reservation
            WHERE bookId = NEW.bookId 
        ) THEN
            START TRANSACTION;
            SELECT TOP 1
                curReservationUsername = username,
                curReservationDate = reservationDate
            FROM Reservation
            WHERE bookId = NEW.bookId
            ORDER BY reservationDate ASC;

            INSERT INTO Transaction
            VALUES (NEW.bookId, curReservationUsername, NEW.transactionDate, 1, 'borrow');

            UPDATE Stock
            SET quantity = MAX((0, quantity - 1))
            WHERE bookId = NEW.bookId;

            DELETE
            FROM Reservation
            WHERE username = curReservationUsername AND reservationDate = curReservationDate AND bookId = NEW.bookId;
        END IF;
    END IF;
END;
```

```
CREATE PROCEDURE GetFavoriteAuthors (IN inputUsername VARCHAR(32))
BEGIN
    SELECT author, COUNT(bookId)
    FROM Book b NATURAL JOIN (
        SELECT DISTINCT t.bookId
        FROM Transactions t
        WHERE t.username = inputUsername
    ) r
    GROUP BY author
    ORDER BY COUNT(bookId) DESC;
END;
```

```
CREATE PROCEDURE GetFavoriteGenres (IN inputUsername VARCHAR(32))
BEGIN
    SELECT genres, COUNT(bookId)
    FROM Book b NATURAL JOIN (
        SELECT DISTINCT t.bookId
        FROM Transactions t
        WHERE t.username = inputUsername
    ) r
    GROUP BY genres
    ORDER BY COUNT(bookId) DESC;
END;
```

```
CREATE PROCEDURE NewBorrow (IN IbookId INT UNSIGNED, Iusername VARCHAR(32), ItransactionDate DATE, Iquantity INT UNSIGNED)
BEGIN
    START TRANSACTION;
    INSERT INTO Transactions
    VALUES (IbookId, Iusername, ItransactionDate, Iquantity, 'borrow');

    IF (SELECT quantity FROM Stock WHERE bookId = IbookId) > 0 THEN
        UPDATE Stock
        SET quantity = quantity - 1
        WHERE bookId = IbookId;
    END IF;
END;
```

```
CREATE PROCEDURE NewReturn (IN IbookId INT UNSIGNED, Iusername VARCHAR(32), ItransactionDate DATE, Iquantity INT UNSIGNED)
BEGIN
    START TRANSACTION;
    INSERT INTO Transactions
    VALUES (IbookId, Iusername, ItransactionDate, Iquantity, 'return');

    UPDATE Stock
    SET quantity = quantity + 1
    WHERE bookId = IbookId;
END;
```
