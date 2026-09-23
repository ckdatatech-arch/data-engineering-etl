-- Query 1: Count total users and recent signups
SELECT 
    COUNT(*) AS total_users,
    COUNT(*) FILTER (WHERE is_recent_signup = TRUE) AS recent_users
FROM dim_users;

-- Query 2: Top 5 countries by user signups
SELECT 
    country, 
    COUNT(*) AS user_count
FROM dim_users
GROUP BY country
ORDER BY user_count DESC
LIMIT 5;