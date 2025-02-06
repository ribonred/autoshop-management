from django.db import connections
from psycopg2.extras import NamedTupleCursor


def entity_properties_keys() -> list[str]:
    conn = connections["default"]
    conn.ensure_connection()
    with conn.connection.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(
            """
            select jsonb_object_keys(properties) as keylist from ledger_entity
            """
        )
        rows = cursor.fetchall()
    return [row.keylist for row in rows]
