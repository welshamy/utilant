CREATE EXTERNAL TABLE utilant_food (
    license bigint,
    facility_name string,
    facility_type string,
    risk string,
    zip int,
    inspection_date date,
    inspection_type string,
    results string,
    violations array<string>
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION 's3://utilant-food/normalized';