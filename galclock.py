def unit1 (hurs,minute,socund) :
    hurs = int (hurs)
    minute = int (minute)
    socund = int (socund)
    return ((((hurs*60)+minute)*60)+socund*100) 



def multyunit (one):
    one = int (one)
    mu = dict()
    mu ["hurs"] = one // 360000
    mu ["minute"] = (one % 360000) // 6000
    mu ["socund"] = ((one % 360000) % 6000) // 100
    return mu 





