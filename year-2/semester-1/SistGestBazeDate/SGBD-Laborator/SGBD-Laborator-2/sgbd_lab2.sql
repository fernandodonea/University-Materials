-- SGBD Laborator 2

------------------SQL Recapitulare 2----------------



--ex 4
-- Câte filme (titluri, respectiv exemplare) au fost împrumutate din cea mai cerută categorie?
WITH categoria_cea_mai_ceruta AS (
    SELECT T.CATEGORY
    FROM RENTAL R
    JOIN TITLE T ON R.TITLE_ID = T.TITLE_ID
    GROUP BY T.CATEGORY
    ORDER BY COUNT(*) DESC
    FETCH FIRST 1 ROW ONLY
)
SELECT
    'Număr de titluri diferita' AS TIP,
    COUNT(DISTINCT R.TITLE_ID) AS NUMAR
FROM RENTAL R
JOIN TITLE T ON R.TITLE_id = T.TITLE_id
WHERE T.CATEGORY = (SELECT CATEGORY FROM categoria_cea_mai_ceruta)
UNION ALL
SELECT
    'Numar exemplare imprumutate' AS Tip,
    COUNT(*) AS numar
FROM RENTAL R
JOIN TITLE T ON R.TITLE_id = T.TITLE_id
WHERE T.CATEGORY = (SELECT CATEGORY FROM categoria_cea_mai_ceruta);



-- ex 5
--Câte exemplare din fiecare film sunt disponibile în prezent (considerați că statusul unui exemplar nu
-- este setat, deci nu poate fi utilizat)?
SELECT
    T.TITLE_ID,
    T.TITLE,
    COUNT(TC.COPY_ID) AS Exemplare_disponibile
FROM TITLE T
JOIN TITLE_COPY TC ON T.TITLE_ID = TC.TITLE_ID
LEFT JOIN RENTAL R ON R.COPY_ID = TC.COPY_ID
                   AND R.TITLE_ID = TC.TITLE_ID
                   AND R.ACT_RET_DATE IS NULL
WHERE R.BOOK_DATE IS NULL
GROUP BY T.TITLE_ID, T.TITLE;


-- ex 6
--Afișați următoarele informații: titlul filmului, numărul exemplarului, statusul setat și statusul corect.

SELECT
    T.TITLE,
    TC.COPY_ID,
    TC.STATUS,
    CASE
        WHEN R.BOOK_DATE IS NOT NULL THEN 'RENTED'
        ELSE 'AVAILABLE'
    END AS Status_corect
FROM TITLE T
JOIN TITLE_COPY TC ON T.TITLE_ID = TC.TITLE_ID
LEFT JOIN RENTAL R ON R.COPY_ID = TC.COPY_ID AND R.TITLE_ID=TC.COPY_ID AND R.ACT_RET_DATE IS NULL;


