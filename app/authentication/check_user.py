from flask import session, g
#importacion de la conexion a la base de datos
from app.db import get_db

def user_in_g():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user= None
    else:
        db, c = get_db()
        query = 'SELECT * FROM user WHERE id = %s'
        c.execute(query,[user_id])
        g.user = c.fetchone()