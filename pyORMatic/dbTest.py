import databaseobject
import table
import pickledatabase

db = pickledatabase.PickleDatabase("test", "db")
tab = table.Table(db, "test")
dbObj = databaseobject.DatabaseObject(test="test", test2="test")
dbObj2 = databaseobject.DatabaseObject(blah="blah", bar="bar")
tab.put(dbObj)
for row in tab:
    print(str(row))
