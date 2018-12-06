from __future__ import print_function
import argparse
import colorsys
import random
import re
try:
    import configparser
except ImportError:
    import ConfigParser as configparser


shapes = {
    "cigar": "M63.6946983,65.1771149 L67.3620366,36.5718767 C70.4446602,35.9598539 74.150691,35.3794206 78.5614914,34.914682 L74.5262179,67.1968698 C70.1176181,66.5924088 66.5423592,65.879917 63.6946983,65.1771149 Z M60.7709966,64.3904642 C56.1820048,63.0437857 54.3006339,61.9105251 54.3006339,61.9105251 C52.4118936,60.7269306 50.9770409,55.8212605 51.0002783,53.5533968 L51.0002939,49.4466032 C50.9770566,47.1787395 52.3538552,41.8524253 54.2425955,40.6688308 C54.2425955,40.6688308 57.0229145,38.9533218 64.2510537,37.2460195 L60.7709966,64.3904642 Z M77.5026139,67.5724751 L81.6214612,34.6216967 C87.3000878,34.1307397 94.0209239,33.8336387 101.924805,33.8759766 C111.086143,33.8131529 118.538501,34.1899264 124.565693,34.7918344 L120.274292,68.2647583 C115.215052,68.6293956 109.298352,68.8344321 102.397461,68.7871094 C92.288153,68.8412608 84.082156,68.3336438 77.5026139,67.5724751 Z M123.330678,68.0164761 L127.548048,35.1209891 C131.945888,35.6546441 135.478165,36.3067019 138.286414,36.9702112 L134.498159,66.5185976 C131.43863,67.0903622 127.751127,67.6152662 123.330678,68.0164761 Z M137.604976,65.8769499 L141.212962,37.7346577 C146.247507,39.1891891 147.995117,40.4980469 147.995117,40.4980469 C149.779671,41.8354495 151.258116,47.1841661 151.225734,49.4565653 L151.225719,53.5434347 C151.2581,55.8158339 149.837709,60.7439063 148.053156,62.081309 C148.053156,62.081309 145.553354,64.0659553 137.604976,65.8769499 Z",
    "ensign": "M139.283659,33.2039468 L131.357308,50.4135982 L138.488301,66.8899956 L129.446084,66.1710999 L122.642692,50.4516362 L130.248574,33.9377845 L139.283659,33.2039468 Z M142.71492,32.9252567 L152.976562,32.0917969 L143.078125,50 L152.032227,67.9667969 L141.873712,67.1591506 L134.642692,50.4516362 L142.71492,32.9252567 Z M126.817313,34.2164747 L119.357308,50.4135982 L126.060672,65.9019448 L102.064453,63.9941406 L77.8692596,65.9487651 L84.5928874,50.4135982 L76.9908574,33.9081105 L102.008789,36.2314453 L126.817313,34.2164747 Z M73.5403689,33.5876747 L81.3075032,50.4516362 L74.4819025,66.222415 L65.4344894,66.9533162 L72.5928874,50.4135982 L64.4546565,32.7439139 L73.5403689,33.5876747 Z M61.004168,32.4234781 L69.3075032,50.4516362 L62.0471323,67.226966 L50.6044922,68.1513672 L61.6425781,50 L51.3544922,31.5273438 L61.004168,32.4234781 Z",
    "arc": "M67.2669401,37.3136291 C70.4423093,36.0622899 74.2361546,34.8509334 78.6933321,33.8599569 L74.6758267,66 L63.5892003,66 L67.2669401,37.3136291 Z M64.0677274,38.6759644 L60.5646459,66 L54.9973235,66 C52.7896627,66 51,64.2038566 51,62.004402 L51,51.2631761 C51,49.0564683 52.3719502,46.1244571 54.1495514,44.8111267 C54.1495514,44.8111267 57.2209493,41.8223407 64.0677274,38.6759644 Z M81.7956777,33.2279652 C87.4286655,32.1824783 94.0058042,31.502754 101.601563,31.4882813 C110.819518,31.4707177 118.454072,32.4448508 124.683684,33.8715067 L120.564646,66 L77.6991733,66 L81.7956777,33.2279652 Z M127.614616,34.6017587 C131.816908,35.736297 135.291163,37.0638465 138.106072,38.3768774 L134.564646,66 L123.5892,66 L127.614616,34.6017587 Z M140.947022,39.8089923 C145.809753,42.4578485 147.932641,44.714268 147.932641,44.714268 C149.626697,46.1244222 151,49.0637215 151,51.2631761 L151,62.004402 C151,64.2111098 149.20047,66 147.002676,66 L137.5892,66 L140.947022,39.8089923 Z",
    "camera": "M67.4353541,38 L78.4258267,38 L74.6758267,68 L63.5892003,68 L67.4353541,38 Z M64.4107997,38 L60.5646459,68 L54.9973235,68 C52.7896627,68 51,66.2132053 51,64.0007252 L51,41.9992748 C51,39.7905363 52.7953961,38 54.9903426,38 L64.4107997,38 Z M81.4491733,38 L81.5229492,38 L85.1728104,31.533727 C85.9877767,30.0898926 87.9915407,28.9252271 89.6549779,28.9324024 L111.488577,29.026582 C113.149043,29.0337445 115.158547,30.210973 115.976574,31.6553713 L119.569824,38 L124.4108,38 L120.564646,68 L77.6991733,68 L81.4491733,38 Z M127.435354,38 L138.4108,38 L134.564646,68 L123.5892,68 L127.435354,38 Z M141.435354,38 L147.003397,38 C149.21066,38 151,39.7867947 151,41.9992748 L151,64.0007252 C151,66.2094637 149.20047,68 147.002676,68 L137.5892,68 L141.435354,38 Z",
    "slash": "M63.0589938,66 L72.0200328,36 L82.7068149,36 L74.4568149,66 L63.0589938,66 Z M59.9280192,66 L51.0060402,66 C48.7983794,66 47.5255319,64.2132053 48.1654731,62.0007252 L54.5292064,39.9992748 C55.1680653,37.7905363 57.4854927,36 59.6832863,36 L68.8890581,36 L59.9280192,66 Z M77.5681851,66 L85.8181851,36 L126.672246,36 L118.210708,66 L77.5681851,66 Z M121.327754,66 L129.789292,36 L140.672246,36 L132.210708,66 L121.327754,66 Z M135.327754,66 L143.789292,36 L151.688639,36 C153.8963,36 155.169148,37.7867947 154.529206,39.9992748 L148.165473,62.0007252 C147.526614,64.2094637 145.209187,66 143.011393,66 L135.327754,66 Z",
    "diamond": "M67.0726034,35.8294557 L78.4695469,32.650238 L74.7652262,62.2848035 L64.0636167,59.2995517 L67.0726034,35.8294557 Z M63.9358691,36.7044588 L61.1434954,58.4849736 L50.6080358,55.5460699 C48.4773015,54.951694 46.75,52.6798666 46.75,50.4721856 L46.75,45.4961893 C46.75,43.2883363 48.4783428,41.0163904 50.6080358,40.422305 L63.9358691,36.7044588 Z M81.602124,31.7763946 L97.1419642,27.4415012 C99.2726985,26.8471254 102.728343,26.8474158 104.858036,27.4415012 L124.423696,32.8994112 L120.412345,64.187944 L104.858036,68.5268737 C102.727301,69.1212496 99.2716572,69.1209591 97.1419642,68.5268737 L77.6867033,63.0997599 L81.602124,31.7763946 Z M127.343817,33.7139894 L137.940298,36.6699152 L134.931602,60.1377462 L123.54908,63.3129409 L127.343817,33.7139894 Z M140.860419,37.4844933 L151.391964,40.422305 C153.522699,41.0166809 155.25,43.2885083 155.25,45.4961893 L155.25,50.4721856 C155.25,52.6800386 153.521657,54.9519845 151.391964,55.5460699 L138.068336,59.2627431 L140.860419,37.4844933 Z",
    "tab": "M69.3596166,31 L80.341914,31 L74.7704855,70 L63.6721166,70 L69.3596166,31 Z M66.3278834,31 L60.6403834,70 L54.9973235,70 C52.7896627,70 51,68.2100582 51,66.0095952 L51,34.9904048 C51,32.7865651 52.7901313,31 55.0020623,31 L66.3278834,31 Z M83.3674523,31.0344355 C84.884532,31.2463332 86.4298788,32.4100109 86.9630589,33.7966076 L88.6624299,38.2160184 C89.0570502,39.2422741 90.2718301,40.073141 91.3748132,40.0718125 L124.406693,40.032029 L120.564646,70 L77.8009431,70 L83.3674523,31.0344355 Z M127.431715,40.0283856 L138.408856,40.0151648 L134.564646,70 L123.5892,70 L127.431715,40.0283856 Z M141.433877,40.0115214 L147.004221,40.0048125 C149.211029,40.0021546 151,41.7867947 151,43.9992748 L151,66.0007252 C151,68.2094637 149.20047,70 147.002676,70 L137.5892,70 L141.433877,40.0115214 Z",
    "bone": "M64.796766,33.060657 C66.2627354,33.9692752 67.5342252,35.1436865 68.5378011,36.5131763 C68.5396255,36.4819344 71.5480136,37.106413 76.3231197,37.8216554 L72.6433576,67.2597523 C69.7362533,67.7292384 67.7079677,68.1143874 66.9788513,68.2565455 C64.9624899,70.1713846 62.3235219,71.4798415 59.3808334,71.8748409 L64.796766,33.060657 Z M61.9541814,31.7242199 L56.3408581,71.9530366 C49.4276496,71.3921205 44,65.9084326 44,61 C44,58.2066599 46.6430664,55.5834961 46.4718673,51.5 C46.311262,47.6691908 44,44.7933401 44,42 C44,36.8202983 50.0441559,31 57.5,31 C59.0607521,31 60.5596438,31.2550466 61.9541814,31.7242199 Z M79.2936504,38.2441835 C85.2663905,39.0486147 93.0964151,39.8300781 101.119141,39.8300781 C110.578177,39.8300781 119.992334,38.5595199 126.351308,37.4640389 L122.696021,65.975272 C116.671544,65.2570104 109.239521,64.6113281 101.989258,64.6113281 C92.5088791,64.6113281 82.6191346,65.7637709 75.7262956,66.7830217 L79.2936504,38.2441835 Z M129.447884,36.9022702 C131.648795,36.4823161 133.19916,36.1407998 133.867021,35.9891146 C135.949503,33.4295617 139.007011,31.6408876 142.501191,31.141507 L137.318709,70.0101214 C136.255111,69.365476 135.291487,68.581873 134.455308,67.6857669 C132.873431,67.4087791 129.732042,66.8862698 125.672592,66.3495459 L129.447884,36.9022702 Z M145.54156,31.0379092 C152.510708,31.5457576 158,37.0637731 158,42 C158,44.7933401 155.733398,47.2167969 155.528133,51.5 C155.338797,55.450789 158,58.2066599 158,61 C158,66.1797017 151.955844,72 144.5,72 C142.985837,72 141.529896,71.7599526 140.170978,71.3172215 L145.541553,31.0379088 Z",
    "chevron": "M68.2271949,37.623642 L79.4839061,35.5353643 L75.644882,66.2475571 L64.287336,68.3545411 L68.2271949,37.623642 Z M65.1289524,38.1984094 L61.1890935,68.9293085 L55.7794268,69.9328775 C53.5994283,70.3372978 51.84375,68.8724644 51.84375,66.6637259 L51.84375,44.6622755 C51.84375,42.4497954 53.6058125,40.3361134 55.7794268,39.9328775 L65.1289524,38.1984094 Z M82.5790263,34.9611761 L102,31.3583132 L125.444785,35.734918 L121.688529,65.033711 L102,61.3583132 L78.7400022,65.6733689 L82.5790263,34.9611761 Z M128.398644,36.286336 L139.117555,38.2873113 L135.361299,67.5861043 L124.642389,65.5851291 L128.398644,36.286336 Z M142.071414,38.8387293 L147.911787,39.9289931 C150.084425,40.334575 151.84375,42.453537 151.84375,44.6622755 L151.84375,66.6637259 C151.84375,68.8762061 150.08335,70.3343743 147.911787,69.9289931 L138.315159,68.1375223 L142.071414,38.8387293 Z",
    "pointy": "M134.190852,35 L141.307503,50.4516362 L135.010964,65 L126.279886,65 L132.592887,50.4135982 L125.493755,35 L134.190852,35 Z M137.493755,35 L146,35 L154,49.9272461 L146,65 L138.279886,65 L144.592887,50.4135982 L137.493755,35 Z M122.190852,35 L129.307503,50.4516362 L123.010964,65 L78.939231,65 L72.6426921,50.4516362 L79.7593434,35 L122.190852,35 Z M76.4564399,35 L69.3573079,50.4135982 L75.6703097,65 L66.939231,65 L60.6426921,50.4516362 L67.7593434,35 L76.4564399,35 Z M64.4564399,35 L57.3573079,50.4135982 L63.6703097,65 L56,65 L48,50.3076172 L56,35 L64.4564399,35 Z",
    "oval": "M67.3939705,36.3227619 C70.8134594,35.3054224 74.6125392,34.4404187 78.7061187,33.7576146 L74.6767879,65.99231 C70.7465923,65.1810861 67.1469734,64.1937527 63.9659684,63.0612085 L67.3939745,36.3227606 Z M64.2386963,37.3424068 L61.0842094,61.9474047 C53.5403206,58.7800072 49,54.7010919 49,50.25 C49,45.2089293 54.8236998,40.6452357 64.2386963,37.3424068 Z M81.7884263,33.2859643 C87.7317563,32.4561937 94.2140812,32 101,32 C109.523772,32 117.568541,32.7197732 124.667776,33.9955859 L120.412621,67.1857953 C114.414542,68.0334497 107.862514,68.5 101,68.5 C92.5949823,68.5 84.6557145,67.8001431 77.6294965,66.5574144 L81.7884282,33.285961 Z M127.618795,34.5691631 C131.5096,35.3844539 135.071477,36.3730499 138.217904,37.5045857 L134.806,64.1174409 C131.391636,65.1436478 127.593836,66.0172328 123.498421,66.7080755 L127.618795,34.5691631 Z M141.098224,38.6296184 C148.532818,41.7859898 153,45.8349042 153,50.25 C153,55.2550242 147.259288,59.7894739 137.96272,63.0865488 L141.098224,38.6296184 Z",
    "null": "M122.276667,53.7385721 L131.463594,59.0426467 C136.483719,61.9410172 138.203466,68.3607007 135.303334,73.3838774 C132.403839,78.40595 125.974854,80.1224324 120.963594,77.2291802 L101.276667,65.8629277 L81.5897403,77.2291802 C76.5784804,80.1224324 70.1494949,78.40595 67.25,73.3838774 C64.3498675,68.3607007 66.0696154,61.9410172 71.0897403,59.0426467 L80.276667,53.7385721 L71.0897403,48.4344975 C66.0696154,45.536127 64.3498675,39.1164435 67.25,34.0932667 C70.1494949,29.0711942 76.5784804,27.3547118 81.5897403,30.247964 L101.276667,41.6142164 L120.963594,30.247964 C125.974854,27.3547118 132.403839,29.0711942 135.303334,34.0932667 C138.203466,39.1164435 136.483719,45.536127 131.463594,48.4344975 L122.276667,53.7385721 Z",
    "trap": "M67.4291654,36.0482715 L78.4158103,36.0801312 L74.6519445,66.1910573 L63.5672913,66.1708896 L67.4291654,36.0482715 Z M64.4057351,36.039504 L60.60737,65.6667522 C59.1592403,65.0217218 57.8774668,63.8207909 57.3300446,62.447212 L48.2658033,39.7034302 C47.448895,37.6536632 48.5779528,35.9936057 50.7893901,36.0000185 L64.4057351,36.039504 Z M81.4380614,36.0888952 L124.383437,36.2134306 L120.52945,66.2745282 L77.6746037,66.1965568 L81.4380614,36.0888952 Z M127.406867,36.2221982 L138.378234,36.2540135 L134.526185,66.2999942 L123.553299,66.2800299 L127.406867,36.2221982 Z M141.401664,36.2627811 L151.218567,36.2912487 C153.431066,36.2976646 154.538536,37.9572236 153.694541,39.9979844 L144.338807,62.6199429 C143.495628,64.6587307 141.022004,66.3118129 138.815635,66.3077986 L137.550034,66.3054959 L141.401664,36.2627811 Z",
    "tilt": "M73.7133797,28.3621063 L84.1659403,31.7583491 L71.3289685,59.1312308 L60.7849602,55.7052748 L73.7133797,28.3621063 Z M70.8368576,27.4274676 L57.9084381,54.7706362 L52.6135998,53.0502389 C50.5139896,52.3680342 49.3640692,50.1156553 50.0477631,48.0114617 L56.8465852,27.0868389 C57.5291229,24.9862038 59.7938837,23.8393879 61.8841097,24.5185434 L70.8368576,27.4274676 Z M87.0413138,32.6926146 L127.900249,45.9684872 L114.971829,73.3116558 L74.204342,60.0654963 L87.0413138,32.6926146 Z M130.776771,46.9031259 L141.21504,50.2947252 L128.28662,77.6378937 L117.848351,74.2462945 L130.776771,46.9031259 Z M144.091562,51.2293638 L149.3864,52.9497611 C151.48601,53.6319658 152.635931,55.8843447 151.952237,57.9885383 L145.153415,78.9131611 C144.470877,81.0137962 142.206116,82.1606121 140.11589,81.4814566 L131.163142,78.5725324 L144.091562,51.2293638 Z",
    "peanut": "M63.1001888,68.8142896 L67.9305054,31.1378199 C68.7730164,31.0468158 69.6304802,31 70.5,31 C73.3810992,31 76.1298384,31.5139844 78.6408306,32.4463695 C78.674424,32.4554135 78.7080292,32.4644322 78.7416483,32.4734266 L74.0845517,69.7301996 C72.9188374,69.9076396 71.7213109,70 70.5,70 C67.8997597,70 65.4073314,69.581341 63.1001888,68.8142896 Z M60.2269316,67.6341718 C53.5384686,64.328385 49,57.8948975 49,50.5 C49,41.5084478 55.7098739,33.938287 64.8359573,31.6837712 L60.2269316,67.6341718 Z M77.1946583,69.0361198 L81.6754602,33.1897051 C94.9983384,36.142323 110.07994,35.5434454 122.265197,32.8853963 C123.082923,32.532107 123.929128,32.2242788 124.799836,31.9655156 L120.285111,67.1803739 C107.918716,64.4341921 91.4079321,64.2809864 81.5734863,67.2687988 C81.5078827,67.2887299 81.4426169,67.3070308 81.3776891,67.3237212 C80.0659623,68.0228984 78.66524,68.5994833 77.1946583,69.0361198 Z M123.144009,68.4724913 L127.913548,31.2700897 C129.079861,31.0924608 130.278025,31 131.5,31 C134.048704,31 136.493827,31.4022279 138.762412,32.140513 L133.612426,69.9070717 C132.917449,69.9685415 132.212775,70 131.5,70 C128.536385,70 125.71282,69.4561525 123.144009,68.4724913 Z M136.706003,69.4244487 L141.632479,33.2969562 C148.397854,36.5817103 153,43.0534055 153,50.5 C153,59.6413275 146.064727,67.313516 136.706003,69.4244487 Z",
    "cloud": "M69.3535654,35.3423218 C70.3666269,35.118181 71.4195121,35 72.5,35 C74.842782,35 77.0557939,35.5556119 79.0144554,36.5422555 L74.5993334,68 L64.9002457,68 L69.3535654,35.3423218 Z M66.1749484,36.448577 L61.8724816,68 L59,68 C52.9248678,68 48,63.0751322 48,57 C48,51.1189021 52.6152999,46.3157652 58.4215402,46.0149487 C59.4621497,41.7971591 62.3486492,38.3063376 66.1749484,36.448577 Z M81.7880608,38.3648167 C82.3920927,38.8691957 82.9544572,39.4218022 83.4692366,40.0167185 C85.2620334,32.5495514 91.9829331,27 100,27 C106.471451,27 112.098337,30.6160149 114.970378,35.9377663 C117.412097,33.5043228 120.780372,32 124.5,32 C125.148902,32 125.787111,32.0457826 126.411572,32.1342937 L120.785579,68 L77.6287368,68 L81.7880608,38.3648167 Z M129.329774,32.8896221 C132.785656,34.2140377 135.558387,36.9182058 136.973774,40.3279318 C137.268093,40.2630796 137.565887,40.2074886 137.866834,40.1614802 L133.80705,68 L123.822264,68 L129.329774,32.8896221 Z M140.917799,40.0296037 C148.221973,40.502284 154,46.5763767 154,54 C154,61.0529438 148.784588,66.887763 142,67.8582223 L142,68 L136.838783,68 L140.917799,40.0296037 Z",
    "rect": "M67.4353541,36 L78.4258267,36 L74.6758267,66 L63.5892003,66 L67.4353541,36 Z M64.4107997,36 L60.5646459,66 L54.9973235,66 C52.7896627,66 51,64.2132053 51,62.0007252 L51,39.9992748 C51,37.7905363 52.7995299,36 54.9973235,36 L64.4107997,36 Z M81.4491733,36 L124.4108,36 L120.564646,66 L77.6991733,66 L81.4491733,36 Z M127.435354,36 L138.4108,36 L134.564646,66 L123.5892,66 L127.435354,36 Z M141.435354,36 L147.002676,36 C149.210337,36 151,37.7867947 151,39.9992748 L151,62.0007252 C151,64.2094637 149.20047,66 147.002676,66 L137.5892,66 L141.435354,36 Z",
    "flag": "M67.5962,31.1988046 C71.2025068,30.9468941 75.0989446,30.9368915 79.2028037,31.1545446 L74.5335043,62.5055543 C70.5009526,62.3980062 66.7187775,62.516246 63.2748912,62.888402 L67.5962,31.1988046 Z M64.5301204,31.4797846 L60.1902392,63.3055799 C57.0991748,63.8144992 54.3433418,64.5643369 52,65.579813 L52.1713867,34.6296176 C55.5200045,33.068921 59.7157636,32.0321039 64.5301204,31.4797846 Z M82.2065594,31.3515065 C88.2470237,31.8213491 94.6754421,32.7551771 101.245605,34.1105647 C109.749026,35.8647723 117.9328,37.0380244 125.445349,37.4106714 L121.394847,68.4645151 C114.963501,67.9759864 108.106181,66.9925385 101.027344,65.6347554 C92.8135016,64.0592683 84.8291242,63.005484 77.5487691,62.6252411 L82.2065594,31.3515065 Z M128.456838,37.5174144 C132.358298,37.5983742 136.055818,37.4437495 139.496263,37.0203448 L135.369411,68.6595281 C131.913411,68.869107 128.239748,68.8593365 124.395058,68.6577227 L128.456838,37.5174144 Z M142.582379,36.5549309 C145.769729,35.9801942 148.698654,35.141738 151.320312,34.009047 C151.376953,35.4328403 151.06543,65.4782505 151.06543,65.4782505 C147.411841,66.9696271 143.154313,67.9204865 138.427352,68.4101564 L142.582379,36.5549309 Z",
    "light": "M67.8163328,64.0721746 L71.1102981,38.3792453 C72.5504014,38.1484604 74.0356686,39.3190043 74.4109782,41.9223824 C76.5737331,38.3856757 78.245328,38.3463317 80.1222633,38.2723155 L77.1691719,61.8970466 C76.7165616,61.419017 76.3207003,60.6979523 75.9869283,59.617483 C75.5852886,64.3085619 72.2269765,63.9480182 70.3808467,60.3182236 C69.4705702,62.2094763 68.6818492,63.5210538 67.8163328,64.0721746 Z M64.8843389,63.3502035 C64.6982058,63.1797105 64.5056127,62.9868126 64.3058257,62.7708411 C62.8305894,60.6426056 61.6929028,58.7048832 60.886268,56.8781895 L60.886268,57.2220505 C53.2232753,57.2220505 53.0422887,45.9990415 60.343308,45.4689054 C61.1649935,43.228963 62.5199994,40.8784101 64.3941197,38.2434728 C65.5009029,36.846258 66.95109,37.5188759 67.8097993,40.5316117 L64.8843389,63.3502035 Z M80.0801046,62.796358 L82.7378634,41.5342879 C82.7650429,41.5869578 82.7919786,41.6396216 82.8186705,41.6922823 C83.0654361,41.2637957 83.3325865,40.8985563 83.618188,40.6095256 C85.0397167,39.1709295 88.1098975,38.7473841 89.5602091,38.3744862 C93.1824992,37.4430841 94.975415,36.9416154 103.951682,31.5603419 C103.970871,31.5446073 103.98657,31.5215286 104.005759,31.5058288 C108.323724,28.0730962 113.76091,26 119.705547,26 C120.485436,26 121.257082,26.0352976 122.018975,26.1043822 L114.874031,76.1189898 C110.773502,75.3118214 107.03704,73.5002707 103.897082,70.9733526 C98.8712303,66.8811469 90.8540461,64.3342906 83.618188,60.7248796 C83.2734213,60.3682658 82.9642186,59.9510037 82.6889584,59.483961 C82.1328006,60.5758146 81.4779144,61.6711531 80.7249816,62.7708411 C80.5050156,62.7805699 80.289993,62.7904634 80.0801046,62.796358 Z M117.847236,76.519755 L124.985499,26.5519197 C128.042567,27.2011312 130.895526,28.4026021 133.435013,30.0469695 L126.684456,75.6132216 C124.467787,76.2481572 122.126546,76.5882076 119.705896,76.5882076 C119.0804,76.5882076 118.460615,76.5651025 117.847236,76.519755 Z M129.888816,74.4548085 L136.165408,32.0878093 C141.573407,36.7268266 144.999651,43.6104228 144.999651,51.2941039 L145,51.2941039 C145,61.6408043 138.787257,70.5367259 129.888816,74.4548085 Z",
    "burst": "M68.1118295,36.6436091 L70.0908203,37.1401367 L77.6518555,27.9399414 L80.0402513,29.1856774 L75.4939944,65.5557326 L65.3769531,69.5927734 L64.2138791,67.0476225 L68.1118295,36.6436091 Z M65.1815328,35.9083994 L61.8519624,61.8790485 L60.7792969,59.5317383 L50.6767578,62.6801758 L52.7138672,54.2163086 L45,50.2573242 L53.4638672,45.7524414 L57.0615234,33.8710938 L65.1815328,35.9083994 Z M82.8785486,30.6660723 L88.4907227,33.5932617 L97.1030273,26 L106.668945,33.7460938 L117.067871,26.3056641 L124.536621,35.2602539 L125.303244,34.9873747 L120.897255,69.5574401 L114.771484,66.4399414 L106.099121,73.5102539 L96.2553711,66.1943359 L86.3144531,73.324707 L78.6159458,64.7668948 L82.8785486,30.6660723 Z M128.471231,33.8597307 L138.246094,30.3803711 L139.47874,33.5901842 L135.664295,63.342851 L132.88916,62.7124023 L125.643066,71.9726562 L123.737312,71.0027884 L128.471231,33.8597307 Z M141.746283,39.4948714 L141.955078,40.0385742 L151.456055,38.9282227 L150.497559,45.1645508 L157.697266,49.5722656 L149.677734,53.7255859 L145.260742,65.5229492 L138.603252,64.0105162 L141.746283,39.4948714 Z",
}
shapenames = list(shapes)

schemes = {
    "citrus":  "#3C989E,#5DB5A4,#F4CDA5,#F57A82,#ED5276".split(","),
    "fun":     "#E97778,#89C7B6,#FFD57E,#AD84C7,#7998C9".split(","),
    "pastels": "#DEDFE0,#FF8F93,#FFC4CD,#C9FFFC,#9BF2F0".split(","),
    "blues":   "#226C8A,#2F7A92,#4997A5,#4997A5,#6CBDBD".split(","),
    "raymond": "#D12229,#28335C,#00A499,#FFC72C,#63666A".split(","),
    "desert":  "#968973,#E3D8C4,#cccccc,#647B96,#C4D2E3".split(","),
    "sports":  "#326099,#AAB9CC,#624F49,#993C32,#2C6466".split(","),
    "garden":  "#F7A5CA,#FF7EB0,#B7DEA1,#83AE9B,#4A4F85".split(","),
    "lowkey":  "#454559,#B89380,#BFAE99,#848E85,#726270".split(","),
    "wonder":  "#E37B40,#46B29D,#DE5B49,#324D5C,#F0CA4D".split(","),
    "xmas":    "#FF6969,#B22525,#FFC56F,#14B241,#4FFF81".split(","),
}

PATH = '<path d="%s" stroke="%s" stroke-width="%s" fill="none" />\n'
LINE = '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" />\n'
NODE = '<use xlink:href="#%s" x="%s" y="%s" width="%s" height="%s" stroke="%s" stroke-width="%s" fill="%s" />\n'
CONN = '<use xlink:href="#conn" x="%s" y="%s" width="%s" height="%s" stroke="%s" fill="%s" />\n'

hex_expr = re.compile("[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3}")


def check_hex(string):
    if hex_expr.match(string):
        string = "#" + string
    return string


def generate(width=1920, height=1080, scale=1.0, rotate=0, slop=5,
             shape="cycle", wirestroke="#cccccc", nodestroke="none",
             nodefill="#cccccc", connstroke="#cccccc", connfill="#ffffff",
             wirestyle="bezier", background="#ffffff",
             strokewidth=2, wirewidth=None,
             saturation=1.0, lightness=0.5, scheme=None, seed=None):
    rnd = random.Random()
    if seed is not None:
        rnd.seed(seed)

    out = []

    background = check_hex(background)
    scale = float(scale)
    rotate = float(rotate)
    slop = int(slop * (1/scale))
    strokewidth = float(strokewidth)
    wirewidth = float(wirewidth) if wirewidth else strokewidth
    saturation = float(saturation)
    lightness = float(lightness)

    colors = []
    if scheme and isinstance(scheme, (str, unicode)):
        if scheme != "random":
            if scheme in schemes:
                colors = schemes[scheme]
            else:
                colors = scheme.split(",")

    def clr(string, index=0):
        if string == "background":
            return background
        elif string == "cycle":
            return colors[index % len(colors)]
        elif string == "random":
            if colors and scheme != "random":
                return rnd.choice(colors)
            hue = rnd.random()
            r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
            return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))
        else:
            return check_hex(string)

    # Write the opening boilerplate
    out.append("""<?xml version="1.0" encoding="UTF-8"?>
<svg width="%(w)spx" height="%(h)spx" viewBox="0 0 %(w)s %(h)s" version="1.1"
xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<title>Network editor wallpaper</title>
<desc>A wallpaper based on node shapes from the Houdini network editor.</desc>
<defs>
""" % {"w": width, "h": height})

    # Write shape definitions for the node shapes
    for name, path in shapes.items():
        out.append('<g id="%s" viewBox="0 0 200 100">' % name)
        out.append('  <path d="%s" class="outline" />' % path)
        out.append('</g>')

    # Write a shape definition for the connectors
    out.append("""
<g id="conn" viewBox="0 0 200 100" transform="translate(66.000000, 11.000000)"
stroke-width="%s">
    <circle cx="6.5" cy="6.5" r="5.5"></circle>
    <circle cx="33.5" cy="73.5" r="5.5"></circle>
    <circle cx="61.5" cy="6.5" r="5.5"></circle>
</g>    
""" % strokewidth)

    # Close the definitions element
    out.append('</defs>')

    # Write a rect to fill the background with color
    out.append(
        '<rect x="0" y="0" width="%s" height="%s" stroke="none" fill="%s"/>\n' %
        (width, height, background)
    )

    # Start a context to apply our rotation and scaling options
    out.append(
        '<g id="main" transform="rotate(%s) scale(%s,%s)">\n' %
        (rotate, scale, scale)
    )

    tilewidth = 200
    tileheight = 100 + 20
    cols = int(width // (tilewidth * scale)) + slop
    rows = int(height // (tileheight * scale)) + slop
    xoffset = 0 - (slop // 2) * tilewidth
    yoffset = 0 - (slop // 2) * tileheight

    wirew = 75
    wireh = 53
    cpoff = 35

    # Write the rows and columns of wires
    idx = -1
    for row in range(rows):
        rowoffset = -50 if row % 2 else 50
        for col in range(cols):
            idx += 1
            coloffset = -10 if col % 2 else 10
            x = col * tilewidth + xoffset + rowoffset
            y = row * tileheight + yoffset + coloffset
            outx = x + 100
            outy = y + 84
            if row % 2:
                leftoff = 20 if col % 2 else -20
                rightoff = 0
            else:
                leftoff = 0
                rightoff = 20 if col % 2 else -20

            lx = outx - wirew
            ly = outy + wireh + leftoff
            rx = outx + wirew
            ry = outy + wireh + rightoff

            leftd = (
                ("M%s,%s" % (outx, outy)) +
                ("C%s,%s %s,%s %s,%s" %
                 (outx, outy + cpoff, lx, ly - cpoff, lx, ly))
            )
            rightd = (
                ("M%s,%s" % (outx, outy)) +
                ("C%s,%s %s,%s %s,%s" %
                 (outx, outy + cpoff, rx, ry - cpoff, rx, ry))
            )

            if wirestyle == "bezier":
                out.append(PATH % (leftd, clr(wirestroke, idx), wirewidth))
                out.append(PATH % (rightd, clr(wirestroke, idx), wirewidth))
            elif wirestyle == "straight":
                out.append(LINE % (outx, outy, lx, ly, clr(wirestroke, idx),
                                   wirewidth))
                out.append(LINE % (outx, outy, rx, ry, clr(wirestroke, idx),
                                   wirewidth))

    # Write the rows and columns of nodes and connectors
    idx = -1
    for row in range(rows):
        rowoffset = -50 if row % 2 else 50
        for col in range(cols):
            idx += 1
            if shape == "cycle":
                shapename = shapenames[idx % len(shapenames)]
            elif shape == "random":
                shapename = rnd.choice(shapenames)
            else:
                shapename = shape

            coloffset = -10 if col % 2 else 10
            # coloffset = 0
            x = col * tilewidth + xoffset + rowoffset
            y = row * tileheight + yoffset + coloffset
            out.append(NODE % (shapename, x, y, tilewidth, tileheight,
                       clr(nodestroke, idx), strokewidth, clr(nodefill, idx)))

            out.append(CONN % (x, y, tilewidth, tileheight,
                               clr(connstroke, idx), clr(connfill, idx)))

    # Finish the file
    out.append('</g>')
    out.append('</svg>')
    return "".join(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates wallpaper images from Houdini node shapes",
        fromfile_prefix_chars="@",
    )
    parser.add_argument(
        "outfile", type=str, help=".png or .svg file to output."
    )
    parser.add_argument(
        "-W", "--width", type=int, default=1920,
        help="Width of the image to generate."
    )
    parser.add_argument(
        "-H", "--height", type=int, default=1080,
        help="Height of the image to generate."
    )
    parser.add_argument(
        "-s", "--scale", type=float, default=0.8, help="Scaling factor for graphics."
    )
    parser.add_argument(
        "-r", "--rotate", type=float, default=-7.0,
        help="Degrees (positive or negative) to rotate graphics."
    )
    parser.add_argument(
        "--slop", type=int, default=5,
        help=(
            "Number of 'extra' rows/columns to generate to compensate for "
            "rotation."
        )
    )
    parser.add_argument(
        "--background", type=str, default="ffffff", metavar="COLOR",
        help="Background hex color."
    )
    parser.add_argument(
        "--shape", type=str, default="cycle", metavar="SHAPE",
        help=(
            "A shape name, or "
            "'cycle' (cycle through all shapes), or "
            "'random' (randomly choose each shape)."
        )
    )
    parser.add_argument(
        "--scheme", type=str, default="raymond",
        help=(
            "Color scheme to use when specifying cycled and/or random colors -- "
            "either the name of a scheme (" + ", ".join(sorted(schemes)) +
            ") or a comma separated list of hex colors."
        )
    )
    parser.add_argument(
        "--nodestroke", type=str, default="none", metavar="COLOR",
        help=(
            "Color to use to draw node outlines -- "
            "A hex color string, or "
            "'cycle' (cycle through color scheme), or "
            "'random' (randomly choose from color scheme), or "
            "'none' (do not draw node outlines)."
        )
    )
    parser.add_argument(
        "--nodefill", type=str, default="cycle", metavar="COLOR",
        help=(
            "Color to use to draw node outlines -- "
            "A hex color string, or "
            "'cycle' (cycle through color scheme), or "
            "'random' (randomly choose from color scheme), or "
            "'background' (use background color)."
        )
    )
    parser.add_argument(
        "--wirestroke", type=str, default="cccccc", metavar="COLOR",
        help=(
            "Color to use to draw wires -- "
            "A hex color string, or "
            "'cycle' (cycle through color scheme), or "
            "'random' (randomly choose from color scheme), or "
            "'none' (do not draw wires)."
        )
    )
    parser.add_argument(
        "--wirestyle", type=str, default="bezier",
        choices=["bezier", "straight"],
        help="How to draw wires between nodes (bezier or straight)."
    )
    parser.add_argument(
        "--connstroke", type=str, default="cccccc", metavar="COLOR",
        help=(
            "Color to use to draw connector outlines -- "
            "A hex color string, or "
            "'cycle' (cycle through color scheme), or "
            "'random' (randomly choose from color scheme), or "
            "'none' (don't draw connector outlines)."
        )
    )
    parser.add_argument(
        "--connfill", type=str, default="background", metavar="COLOR",
        help=(
            "Color to use to fill connectors -- "
            "A hex color string, or "
            "'cycle' (cycle through color scheme), or "
            "'random' (randomly choose from color scheme), or "
            "'background' (use background color)."
        )
    )
    parser.add_argument(
        "--strokewidth", type=float, default=2.0, metavar="WIDTH",
        help="Stroke width to use when drawing node outlines."
    )
    parser.add_argument(
        "--wirewidth", type=float, default=None, metavar="WIDTH",
        help=(
            "Stroke width to use when drawing wires. If this is not given, "
            "it uses the same value as strokewidth."
        )
    )
    parser.add_argument(
        "--seed", type=float, default=None, metavar="FLOAT",
        help="A seed for the random number generator."
    )
    parser.add_argument(
        "--saturation", type=float, default=1.0, metavar="FLOAT",
        help="The saturation of random colors when a scheme is not specified."
    )
    parser.add_argument(
        "--lightness", type=float, default=0.5, metavar="FLOAT",
        help=(
            "The lightness (as in the HSL model) of random colors when a "
            "scheme is not specified."
        )
    )

    argdict = dict(vars(parser.parse_args()))
    filename = argdict.pop("outfile")
    svg = generate(**argdict)

    if filename.endswith(".svg"):
        print("Writing SVG to", filename)
        with open(filename, "w") as f:
            print(svg, file=f)
    else:
        try:
            from PySide2 import QtCore, QtGui, QtSvg
        except ImportError:
            try:
                from PyQt5 import QtCore, QtGui, QtSvg
            except ImportError:
                from hutil.Qt import QtCore, QtGui, QtSvg

        print("Rendering to image", filename)
        renderer = QtSvg.QSvgRenderer(QtCore.QByteArray(svg.encode("utf8")))
        if not renderer.isValid():
            raise Exception("Generated SVG is not valid")

        width = argdict["width"]
        height = argdict["height"]
        img = QtGui.QImage(width, height, QtGui.QImage.Format_ARGB32)
        # img.fill(QtGui.QColor("#ffffff"))
        painter = QtGui.QPainter()
        painter.begin(img)
        painter.setRenderHints(QtGui.QPainter.HighQualityAntialiasing)
        renderer.render(painter)
        painter.end()
        img.save(filename)

