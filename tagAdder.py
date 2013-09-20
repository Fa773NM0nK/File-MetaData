import sqlite3

def addTag(tagText):
	conn = sqlite3.connect('.FMD.db')
	c = conn.cursor()
	c.execute('INSERT INTO "tags" ("tagText") VALUES ("' + tagText + '");')
	conn.commit();