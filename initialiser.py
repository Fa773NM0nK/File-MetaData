def init():
	import os
	if os.path.exists('.FMD.db'):
		os.remove('.FMD.db')
	import sqlite3
	conn = sqlite3.connect('.FMD.db')
	c = conn.cursor()
	c.execute('CREATE TABLE "tags" ( "id" INTEGER PRIMARY KEY, "tagText" VARCHAR(50) );')
	conn.commit();