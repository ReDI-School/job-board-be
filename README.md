# Job Board Backend

The BE provides an API to the job board database. It contains the two jobs:
1. Query DB 
2. Provide API  

The API:
- fastapi

The DB:
- The database is a postgresql
- will be fed with job ads from the ReDI staff
- it contains the following columns: 
    - id integer PRIMARY KEY,
    - timestamp text,
    - source text, Where the job ads could be found (link).
    - header text, Title of the job ad.
    - content text, Text of the job ad (details of the ad which includes the job requirement etc.
    - language text, English/German.
    - experience text,
    - employment_time text, full-time, part-time
    - poster text, name of the person who posts
    - application_link text,
    - company_name text,
    - location text,
    - deadline text,
    - community_only text,
    - contact_name text   
                
            
            
            

