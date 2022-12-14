SELECT YEAR(DATE_FORMAT(SALES_DATE, '%Y-%m-%d')) AS YEAR
    , MONTH(DATE_FORMAT(SALES_DATE, '%Y-%m-%d')) AS MONTH
    , GENDER
    , COUNT(DISTINCT USER_INFO.USER_ID) USERS
FROM ONLINE_SALE
    LEFT JOIN USER_INFO ON ONLINE_SALE.USER_ID = USER_INFO.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER