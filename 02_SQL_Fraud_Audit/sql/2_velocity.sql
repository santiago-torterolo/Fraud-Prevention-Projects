-- DETECTING HIGH VELOCITY (BOTS)
-- Logic: Users with > 15 transactions in a single hour (step)
SELECT nameOrig,
    step as hour_step,
    COUNT(*) as velocity_count
FROM paysim_transactions
GROUP BY nameOrig,
    step
HAVING velocity_count > 15
ORDER BY velocity_count DESC;