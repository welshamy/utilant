SELECT facility_name, inspection_date, results, violations
FROM utilant_food
WHERE inspection_date>='2019-01-01' and results='Fail';