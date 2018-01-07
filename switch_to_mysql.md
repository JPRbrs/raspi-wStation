# Changes on database
## Migrate to mysql
With the following commands executed in mysql3 the data will be exported to  
csv format so we can importe it on the newly create mysql db  

```
 .headers on  
 .mode csv  
 .output data.csv  
 SELECT * from measurements  
 .quit  
```
 
## Next steps
 - We need to create tables before import with db.create_all()
 - Data from Instant is stored in instant table, I need to define the table name as instants
 - I need to delete the User model
 - I need to find out why running migrate_db does not populate the db
