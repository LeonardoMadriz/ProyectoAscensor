def interpolacion(sup1,sup2,inf1,inf2,nom):
    result=(((inf2-sup2)*(nom-sup1))/(inf1-sup1)) + sup2
    result = round(result,2)
    return result

