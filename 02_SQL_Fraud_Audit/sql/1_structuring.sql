-- DETECTING STRUCTURING (SMURFING)
-- Logic: Users doing CASH_OUT between 9000 and 9999 to avoid 10k threshold
SELECT nameOrig,
    COUNT(*) as tx_count,
    SUM(amount) as total_laundered
FROM paysim_transactions
WHERE type = 'CASH_OUT'
    AND amount BETWEEN 9000 AND 9999
GROUP BY nameOrig
HAVING tx_count >= 3
ORDER BY total_laundered DESC;