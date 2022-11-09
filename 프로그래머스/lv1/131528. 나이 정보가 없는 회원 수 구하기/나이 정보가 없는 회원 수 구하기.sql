-- 코드를 입력하세요
SELECT COUNT(IF (AGE is null, 1, null)) AS USERS
FROM USER_INFO