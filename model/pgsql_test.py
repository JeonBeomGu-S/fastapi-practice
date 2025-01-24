import psycopg
import psycopg_pool
from config import config

pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE
)

# call procedure version
def list_admin():
    with pool_default.connection() as conn:
        cur = conn.cursor(row_factory=psycopg.rows.dict_row)

        try:
            cur.execute("call sp_l_admin('out1')")
            results = cur.execute("fetch all from out1").fetchall()
            conn.commit()
        except psycopg.OperationalError as err:
            print(f'Error querying: {err}')
            results = False
        except psycopg.ProgrammingError as err:
            print(f'Database error via psycopg. {err}')
            results = False
        except psycopg.IntegrityError as err:
            print(f'PostgreSQL integrity error via psycopg {err}')
            results = False

    return results

# direct select query version
# def list_admin():
#     with pool_default.connection() as conn:
#         cur = conn.cursor(row_factory=psycopg.rows.dict_row)
#
#         try:
#             results = cur.execute("select * from tb_admin").fetchall()
#         except psycopg.OperationalError as err:
#             print(f'Error querying: {err}')
#             results = False
#         except psycopg.ProgrammingError as err:
#             print(f'Database error via psycopg. {err}')
#             results = False
#         except psycopg.IntegrityError as err:
#             print(f'PostgreSQL integrity error via psycopg {err}')
#             results = False
#
#     return results

