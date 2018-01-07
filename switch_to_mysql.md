# Changes on database
## migrate to mysql
With the following commands executed in mysql3 the data will be exported to  
csv format so we can importe it on the newly create mysql db
 .headers on
 .mode csv
 .output data.csv
 SELECT * from measurements
 .quit
 
