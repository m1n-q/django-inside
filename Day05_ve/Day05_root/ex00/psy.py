import psycopg2

def create_movies_table():
	try:
		conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
		try:
			cur = conn.cursor()
			cur.execute("""
				CREATE TABLE IF NOT EXISTS ex00_movies (
					title			varchar(64) NOT NULL UNIQUE,
					episode_nb		integer,
					opening_crawl	text,
					director		varchar(32) NOT NULL,
					producer		varchar(128) NOT NULL,
					release_date	date NOT NULL,
					PRIMARY KEY		(episode_nb)
				);
				""")
		except Exception as e:
			print("<ERROR> cannot create table: ", e)
		else:
			conn.commit()		# What is commit?
			conn.close()
			cur.close()
			print("OK")

	except Exception as e:
		print('<ERROR> connection to postgreSQL failed: ', e)

