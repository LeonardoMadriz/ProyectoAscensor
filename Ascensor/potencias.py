def box_power(nom,vn,radio, angular_velocity ):
    torque = (9.8)*0.5*nom*radio
    pulley_power = torque*angular_velocity
    box_p = pulley_power/0.8
    box_p = round(box_p,2)
    return box_p

def engine_power(box_p):
    engine_p = box_p/0.9
    engine_p = round(engine_p,2)
    return engine_p
