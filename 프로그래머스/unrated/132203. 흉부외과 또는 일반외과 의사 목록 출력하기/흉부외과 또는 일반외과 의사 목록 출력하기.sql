-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, DATE_FORMAT(hire_ymd, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY hire_ymd DESC, dr_name