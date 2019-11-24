# permafrost

## Setting Temp
sqlite3 permafrost_db.db
UPDATE config SET value = 50 WHERE key = 'desired_temp';