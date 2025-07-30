--  View Sample Logs (first 10 rows)
SELECT * FROM logs_json
LIMIT 10;


--  View the Most Recent Logs (latest first)
SELECT * FROM logs_json
ORDER BY timestamp DESC
LIMIT 20;


--  Find Logs Containing 'ERROR'
SELECT * FROM logs_json
WHERE message LIKE '%ERROR%'
ORDER BY timestamp DESC
LIMIT 10;


--  Count Number of Errors by Log Group (e.g., Lambda function name)
SELECT logGroup, COUNT(*) AS error_count
FROM logs_json
WHERE message LIKE '%ERROR%'
GROUP BY logGroup;

