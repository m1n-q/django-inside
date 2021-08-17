import psycopg2
from datetime import date


def create_movies_table(table):
	try:
		conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
		try:
			cur = conn.cursor()
			cur.execute("""
				CREATE TABLE IF NOT EXISTS %s (
					title			varchar(64) NOT NULL UNIQUE,
					episode_nb		integer,
					opening_crawl	text,
					director		varchar(32) NOT NULL,
					producer		varchar(128) NOT NULL,
					release_date	date NOT NULL,
					PRIMARY KEY		(episode_nb)
				);
				""" % (table, ))
		except Exception as e:
			return ("<ERROR> cannot create table: " + str(e))
		else:
			conn.commit()		# What is commit?
			conn.close()
			cur.close()
			return ("OK")

	except Exception as e:
		return ('<ERROR> connection to postgreSQL failed: ' + str(e))


def insert_into_table(epi_nb: int, title: str, director: str, producer: str, rel_date: date, opening: str ='',):
	try:
		conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
		try:
			cur = conn.cursor()		# how to set %s for table_name
			cur.execute("""
				INSERT INTO ex02_movies (episode_nb, title, opening_crawl, director, producer, release_date)
				VALUES (%(epi_nb)s, %(title)s, %(opening)s, %(director)s, %(producer)s, %(rel_date)s)
				ON CONFLICT (episode_nb) DO NOTHING;
				""",
				{'epi_nb': epi_nb, 'title': title, 'opening' : opening, 'director' : director, 'producer': producer, 'rel_date': rel_date}
				)
		except Exception as e:
			return ("<ERROR> cannot insert into table: " + str(e))
		else:
			conn.commit()
			conn.close()
			cur.close()
			return ("OK")

	except Exception as e:
		return ('<ERROR> connection to postgreSQL failed: ' + str(e))


def select_all_from_table(table):
	try:
		conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
		try:
			cur = conn.cursor()
			cur.execute("""
				SELECT episode_nb, title, opening_crawl, director, producer, release_date FROM %s;
				""" % (table, )
			)
			ret = cur.fetchall()
		except Exception as e:
			return ("<ERROR> cannot select from table: " + str(e))
		else:
			conn.commit()
			conn.close()
			cur.close()
			if len(ret) == 0:
				return ("No data available.")
			return (ret)

	except Exception as e:
		return ('<ERROR> connection to postgreSQL failed: ' + str(e))

