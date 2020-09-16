import time 


def nowunit ():
    return time.time ()



def unit1 (socond10,socund,minute,hurs,day) :
    hurs = int (hurs)
    minute = int (minute)
    socund = int (socund)
    day = int (day)
    return (((((((((day)*24)+hurs)*60)+minute)*60)+socund)*10)+socond10) 



def multyunit (one):
    one = int (one)
    mu = dict()
    mu ["day"] = one // 864000
    mu ["hurs"] = ( one % 864000 ) // 36000
    mu ["minute"] = (one % 36000) // 600
    mu ["socund"] = (one %  600) // 10
    mu ["socund10"] = one  % 10
    return mu 


def rounddown (num):
    return num // 1




