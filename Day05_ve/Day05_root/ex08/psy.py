import psycopg2
from datetime import date
from pathlib import Path

CSV_DIR = Path(__file__).resolve().parent.parent / 'Day05/static/csv/'

def create_planets_table(table):
    try:
        conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS %s (
                    id              serial,
                    name			varchar(64) NOT NULL UNIQUE,
                    climate	    	varchar,
                    diameter	    integer,
                    orbital_period	integer,
                    population		bigint,
                    rotation_period	integer,
                    surface_water   numeric,
                    terrain         varchar(128),
                    PRIMARY KEY		(id)
                );
                """ % (table, ))
        except Exception as e:
            return ("<ERROR> cannot create table %s: " % table + str(e))
        else:
            conn.commit()		# What is commit?
            conn.close()
            cur.close()
            return ("OK")

    except Exception as e:
        return ('<ERROR> connection to postgreSQL failed: ' + str(e))

def create_people_table(table):
    try:
        conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS %s (
                    id              serial,
                    name			varchar(64) NOT NULL UNIQUE,
                    birth_year	    varchar(32),
                    gender	        varchar(32),
                    eye_color   	varchar(32),
                    hair_color		varchar(32),
                    height	        integer,
                    mass            numeric,
                    homeworld       varchar(64),
                    PRIMARY KEY		(id),
                    FOREIGN KEY     (homeworld) REFERENCES ex08_planets (name)
                );
                """ % (table, ))
        except Exception as e:
            return ("<ERROR> cannot create table %s: " % table + str(e))
        else:
            conn.commit()		# What is commit?
            conn.close()
            cur.close()
            return ("OK")

    except Exception as e:
        return ('<ERROR> connection to postgreSQL failed: ' + str(e))


def file_to_table():

    try:
        f1 = open(CSV_DIR / 'planets.csv', 'r')
        f2 = open(CSV_DIR / 'people.csv', 'r')
    except Exception as e:
        return ("<ERROR> cannot open file: " + str(e))

    try:
        conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
        try:
            cur = conn.cursor()		# how to set %s for table_name
            cur.copy_from(
                file=f1,
                table='ex08_planets',
                null='NULL',
                columns=(
                    'name',
                    'climate',
                    'diameter',
                    'orbital_period',
                    'population',
                    'rotation_period',
                    'surface_water',
                    'terrain',
                ))
            cur.copy_from(
                file=f2,
                table='ex08_people',
                null='NULL',
                columns=(
                    'name',
                    'birth_year',
                    'gender',
                    'eye_color',
                    'hair_color',
                    'height',
                    'mass',
                    'homeworld',
                ))
        except Exception as e:
            return ("<ERROR> cannot insert into table: " + str(e))
        else:
            conn.commit()
            conn.close()
            cur.close()
            return ("OK")

    except Exception as e:
        return ('<ERROR> connection to postgreSQL failed: ' + str(e))


def get_column_names_from_table(table):
    try:
        conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS
                WHERE table_name = '%s';
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


def join_table():
    try:
        conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
        try:
            cur = conn.cursor()
            cur.execute("""
                select (ex08_people.name, homeworld, climate)
                from ex08_people join ex08_planets
                on ex08_people.homeworld = ex08_planets.name
                where ex08_planets.climate like '%windy%';
            """
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
            return ret

    except Exception as e:
        return ('<ERROR> connection to postgreSQL failed: ' + str(e))





def select_all_from_table(table):
    try:
        conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT * FROM %s;
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

