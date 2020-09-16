def unit1 (hurs,minute,socund) :
    hurs = int (hurs)
    minute = int (minute)
    socund = int (socund)
    return ((((hurs*60)+minute)*60)+socund*1) 



def multyunit (one):
    one = int (one)
    mu = dict()
    mu ["hurs"] = one // 3600
    mu ["minute"] = (one % 3600) // 60
    mu ["socund"] = ((one % 3600) % 60) // 1
    return mu 


def rounddown (num):
    return num // 1


