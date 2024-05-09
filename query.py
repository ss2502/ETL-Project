SELECT location, MAX(total_vaccinations) AS max_vaccinations
FROM covid_stats
GROUP BY location
ORDER BY max_vaccinations DESC;
