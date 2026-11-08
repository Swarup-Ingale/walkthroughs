WITH AnalyzedInsurance AS (
    SELECT 
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) as tiv_count,
        COUNT(*) OVER(PARTITION BY lat, lon) as loc_count
    FROM 
        Insurance
)
SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM 
    AnalyzedInsurance
WHERE 
    tiv_count > 1 
    AND loc_count = 1;
