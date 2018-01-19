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
 - I need to find out why running migrate_db does not populate the db
 - Create command to create db
 - Test migrations work
 - Deploy to wayreth
