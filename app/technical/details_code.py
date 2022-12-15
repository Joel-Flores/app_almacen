from flask import g
from app.db import get_db
def details_code(id):
    db, c = get_db()
    query = '''SELECT c.code,
            w.work_order,
            s.cm_mac, s.cm_mac_two, s.card_number,
            e.name,
            m.cable_hdmi , m.cable_rca, m.spliter_two, m.spliter_three,
            m.remote_control, m.connector_int, m.connector_ext, m.power_supply,
            m.q_span, m.cp_black, m.sp_black, m.sp_withe, m.satellite_dish, m.lnb,
            t.type_work
        FROM codes AS c
        LEFT JOIN work_orders AS w
            ON c.id = w.code_id AND  c.technical_id = w.technical_id
        INNER JOIN code_type_works AS ct
            ON c.id = ct.code_id
        INNER JOIN type_works AS t
            ON t.id = ct.type_works_id
        INNER JOIN serials AS s
            ON s.id = w.serials_id
        INNER JOIN equipment AS e
            ON e.id = s.equipment_id
        INNER JOIN materials AS m
            ON m.id = w.materials_id
        WHERE c.technical_id = %s 
            AND ct.id = %s;
    '''
    c.execute(query, [g.user['id'], id])
    
    detail_code = c.fetchall()
    return detail_code