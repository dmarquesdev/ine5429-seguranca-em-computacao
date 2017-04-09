"""
Comparacao de tempo entre os algoritmos de RNG
"""

import bbs
import xorshift
import datetime

values = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

p = int('19808304910323694059944028233269172479978536927546773407963599\
48301029903018623943075956423005538151164584084168858737466478467458403\
42547693955852514995740708453170756631536942975683717571698162825604298\
86718435640957762668087996788635020548474406364457338806768676240212391\
21269121658383732872481019003446415752208166225382628747177936811402440\
93991613067984867764198230399744414209827651153085455969907872647885873\
49220462213144455274763038686097136897132729589875595766689414082866659\
71885557512402207579275358128238769829082744885662886288881366837876614\
866397152698874547525920699503593642877002933207631120843')

q = int('18048605473664884750157728994834069831280725631208960625174559\
84196942727269686522792419209010708167368296345450336443185779227117152\
44571728174416522529781221024502471619772781144429496523012329871372413\
37942161834644606568113369862087318808407938313860004951764174413181711\
14954663648197837324257768096134481549502503021014855234975857550650876\
46192601451765040471721902692932330786034028451469958936628196662412757\
93895416606899871876157022997813715817002298270987245766678325221879944\
52773550344691990824769863692693621238615137483173025166292383149884271\
466290928615493907860853382292499194215338513556846183299')


def primals():
    for val in values:
        xorshift.init_seed(val)
        bbs.init_seed(val, p, q)
        print '%d bits: ' % val

        start = datetime.datetime.now()
        x = xorshift.xorshift(val)
        end = datetime.datetime.now()
        delta = end - start
        print '\tXorshift: %dms' % (delta.total_seconds() * 1000)

        start = datetime.datetime.now()
        x = bbs.bbs(val)
        end = datetime.datetime.now()
        delta = end - start
        print '\tBBS: %dms' % (delta.total_seconds() * 1000)

def main():
    primals()

if __name__ == '__main__':
    main()
