import json,sys
a,b = json.load(open(sys.argv[1]))
m=[26,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,13,3,20,3,2,20,3,2,10,3,10,3,10,3,10,3,13,3,29,2,29,3,2,1,61,3,2,1,2,3,2,61,3,2,1,2,3,2,61,3,2,1,2,3,2,61,3,2,1,2,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,61,3,2,1,2,3,2,9,27,3,2,27,3,2,27,3,2,27,3,2,9,9,9,9,10,3,10,3,29,2,20,3,2,20,3,2,29,3,2,1,20,3,2,20,3,2,10,3,10,3,10,3,10,3,27,3,2,27,3,2,27,3,2,27,3,2,10,3,10,3,20,3,2,20,3,2,20,3,2,20,3,2,61,3,2,1,2,3,2,61,3,2,1,2,3,2,61,3,2,1,2,3,2,61,3,2,1,2,3,2,20,3,2,20,3,2,26,13,3,29,3,2,1,10,26,26,6,45,3,2,1,10,3,9,19,3,2,13,3,13,3,19,3,2,19,3,2,13,3,19,3,2,10,3,19,3,2,19,3,2,13,3,19,3,2,27,3,2,27,3,2,10,3,10,3,9,9,9,9,24,19,3,2,10,3,13,3,19,3,2,10,3,10,3,24,19,3,2,69,3,2,1,2,3,2,1,26,37,3,2,1,19,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,2,49,3,2,1,2,49,3,2,1,2,49,3,2,1,2,49,3,2,1,2,2,49,3,2,1,3,2,49,3,2,1,2,49,3,2,1,2,3,49,3,2,1,2,49,3,2,1,2,49,3,2,1,2,49,3,2,1,2,25,3,2,25,3,2,25,3,2,25,3,2,25,3,2,25,3,2,25,3,2,25,3,2,29,3,2,1,29,3,2,1,40,3,2,1,40,3,2,1,11,3,11,3,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,11,3,9,11,3,11,3,11,3,11,3,11,3,11,3,50,50,2,2,20,3,2,20,3,2,47,3,2,1,61,3,2,1,2,3,2,3,2,1,61,3,2,1,2,3,2,61,3,2,1,2,3,2,30,3,2,1,17,3,2,1,61,3,2,1,2,3,2,3,2,1,2,3,2,1,2,85,3,2,1,2,2,2,1,77,3,2,1,2,3,2,1,3,2,1,3,3,67,3,2,1,2,3,2,3,2,1,2,3,2,1,2,2,3,3,63,3,2,1,2,3,2,2,46,3,2,1,2,3,2,3,2,49,3,2,1,3,2,61,2,2,63,3,2,1,2,3,2,2,2,2,3,2,1,3,2,1,3,2,1,9,3,2,1,3,61,3,2,1,2,3,2,2,3,2,1,21,3,2,1,13,2,1,57,3,2,1,2,3,2,3,25,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,2,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,3,2,1,29,2,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,27,3,2,61,3,2,1,2,3,2,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,29,3,2,1,61,3,2,1,2,3,2,9,9,9,9,1,9,9,9,9,1,1,1,9,3,9,9,9,9,9,9,1,3,2,1,1,1,39,1,1,1,10,3,10,3,61,3,2,1,2,3,2,10,3,10,3,61,3,2,1,2,3,2,29,3,2,1,29,3,2,1,48,3,3,2,1,48,3,3,2,1,1,1,3,2,1,1,1,1,3,2,1,3,2,1,3,2,1,1,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,1,3,2,1,3,2,1,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,40,3,2,1,1,16,3,1,16,3,16,3,16,3,16,3,49,3,2,1,2,16,3,1,16,3,16,3,16,3,16,3,16,3,16,3,16,3,16,3,16,3,16,3,16,3,16,3,1,49,3,2,1,2,16,3,16,3,16,3,16,3,16,3,16,3,16,3,16,3]
n=[6,35,37,66,68,82,84,98,100,114,116,130,132,146,148,162,164,178,180,194,196,210,212,226,228,242,244,258,260,274,276,290,292,306,308,322,324,344,346,360,362,376,378,392,394,408,410,424,426,440,442,494,496,903,905,914,926,928,937,949,951,962,964,975,977,988,990,1004,1006,1130,1151,1162,1164,1173,1184,1230,1232,1241,1252,1273,1276,1285,1294,1296,1305,1316,1337,1340,1349,1358,1360,1369,1380,1401,1404,1413,1422,1424,1433,1444,1465,1468,1477,1691,1693,1702,1721,1723,1732,1751,1753,1762,1781,1783,1792,1815,1817,1826,1845,1847,1856,1875,1877,1886,1905,1907,1916,2291,2293,2302,2321,2323,2332,2351,2353,2362,2381,2383,2392,4179,4181,4190,4209,4211,4220,4239,4241,4250,4269,4271,4280,4299,4301,4310,4329,4331,4340,4359,4361,4370,4389,4391,4400,4419,4421,4430,4449,4451,4460,4479,4481,4490,4509,4511,4520,4539,4541,4550,4569,4571,4580,4599,4601,4610,4629,4631,4640,4667,4669,4678,4689,4710,4713,4722,5253,5332,5334,5343,5392,5394,5403,5452,5454,5463,5512,5514,5523,5676,5771,5808,5952,6055,6057,6068,6070,6115,6136,6276,6278,6287,6299,6301,6310,6396,6398,6407,6418,6716,6718,6727,6739,6741,6750,6762,6764,6775,6777,6788,6790,6801,6803,6831,6833,6842,6861,6863,6872,6891,6893,6902,6921,6923,6932,6954,6956,6967,6969,6980,6982,6991,7003,7005,7014,7273,7275,7284,7296,7298,7307,7766,7768,7777,7788,7809,7812,7821,7830,7832,7841,7852,7873,7876,7885,7894,7896,7905,7916,7937,7940,7949,7958,7960,7969,7980,8001,8004,8013,8028,8030,8039,8051,8053,8062,8383,8413,8415,8429,8431,8440,8451,8470,8505,8532,8549,8596,8598,8607,8618,8669,8671,9360,9698,9700,9709,9724,9726,9740,9742,9756,9758,9767,9778,9780,9789,9806,9808,9822,9824,9833,9844,9846,9858,9860,9869,9880,9882,9891,9902,9904,9918,9920,9929,9947,9949,9958,9977,9979,9988,10007,10009,10020,10022,10035,10046,10058,10069,10086,10117,10119,10128,10139,10141,10152,10154,10168,10170,10179,10224,10226,10237,10239,10251,10279,10281,10290,10634,10636,10645,10656,10677,10680,10689,10700,10722,10811,10813,10822,10833,10858,10860,10869,10932,10934,10943,10962,10964,10973,10992,10994,11003,11022,11024,11033,11077,11079,11088,11107,11109,11118,11137,11139,11148,11167,11169,11178,14415,14417,14426,14445,14447,14456,14475,14477,14486,14505,14507,14516,16328,16441,16443,16452,16463,16484,16493,16495,16504,16515,16536,16545,16547,16556,16567,16588,16597,16599,16608,16619,16640,16692,16701,16703,16712,16723,16745,16848,17117,17119,17128,17139,17160,17169,17171,17180,17191,17212,17265,17481,17483,17492,17503,17524,17533,17535,17544,17555,17576,17845,17847,17856,17867,17888,17897,17899,17908,17919,17940,17949,17951,17960,17977,17979,17988,18005,18007,18016,18033,18035,18044,18061,18063,18072,18089,18091,18100,18117,18119,18128,18145,18147,18156,18173,18175,18184,18195,18205,18207,18216,18227,18241,18243,18252,18263,18284,18286,18295,18306,18327,18329,18341,18343,18388,18390,18399,18410,18431,18433,18442,18453,18474,18476,18485,18496,18517,18519,18528,18539,18560,18562,18571,18582,18603,18605,18614,18625,18646,18648,18657,18668,18689,18691,18700,18711,18734,18736,18748,18760,18762,18774,18776,18788,18790,18802,18804,18816,18818,18830,18832,19217,19269,19393,19425,19649,19651,19660,19672,19674,19683,19712,19714,19723,19734,19969,19971,19980,19991,20012,20015,20024,20295,20306,20317,20413,20415,20424,20435,20456,20459,20468,20478,20480,20489,20500,20521,20524,20533,20566,20568,20577,20588,20609,20611,20616,20619,20642,20644,20653,20664,20685,20688,20697,20715,20726,20737,20758,20761,20770,20781,20802,20811,20813,20822,20833,20854,20872,20894,20897,21142,21144,21153,21164,21185,21188,21197,21208,21242,21253,21264,21286,21360,21374,21376,21385,21396,21417,21420,21429,21449,21460,21471,21492,21495,21504,21515,21559,21581,21593,21667,21677,21679,21688,21699,21716,21719,21728,21771,22033,22035,22044,22055,22231,22234,22243,22267,22520,22705,22707,22716,22723,22741,22748,22904,22925,22947,22991,22993,23002,23013,23034,23037,23046,23335,23379,23397,23550,23557,23564,23574,23583,23590,23598,23607,23614,23717,23751,23760,23771,23793,24025,24027,24036,24047,24068,24071,24080,24507,24726,24733,24744,24770,24772,24777,24788,24897,24900,24903,25205,25207,25216,25225,25244,25247,25256,25290,25520,25522,25531,25542,26012,26014,26023,26034,26044,26046,26055,26066,26082,26084,26093,26104,26114,26125,26136,26152,26154,26163,26174,26184,26186,26195,26206,26222,26224,26233,26244,26254,26275,26293,26295,26304,26315,26325,26327,26336,26347,26361,26363,26372,26383,26393,26395,26404,26415,26428,26430,26439,26450,26460,26462,26471,26482,26493,26495,26504,26515,26525,26527,26536,26547,26559,26570,26581,26591,26612,26627,26629,26638,26649,26659,26661,26670,26681,26694,26696,26705,26716,26726,26728,26737,26748,26759,26761,26770,26781,26791,26793,26802,26813,30264,30266,30275,30294,30296,30305,30324,30326,30335,30354,30356,30365,30384,30386,30395,30414,30416,30425,30444,30446,30455,30474,30476,30485,30504,30506,30515,30534,30536,30545,30564,30566,30575,30594,30596,30605,30624,30626,30635,30654,30656,30665,30684,30686,30695,30714,30716,30725,30752,30754,30763,30774,30795,30798,30807,31755,31757,31766,31777,31787,31789,31798,31809,31821,31823,31832,31843,31853,31855,31864,31875,31886,31888,31897,31908,31918,31920,31929,31940,31952,31954,31963,31974,31984,31986,31995,32006,32273,32275,32284,32295,32316,32319,32328,32399,32427,32455,32482,32585,32795,32823,32850,32876,32939,32947,33071,33093,33121,33148,33173,33359,33387,33414,33439,33496,33728,33730,33732,33756,34176,34297,34507,34570,34656,34683,34685,34696,34698,34714,34716,34725,34736,34757,34760,34769,34778,34780,34791,34793,34873,34875,34884,34895,34916,34919,34928,34991,34993,35002,35013,35023,35025,35034,35045,35172,35190,35194,35202,35213,35317,35335,35339,35347,35358,35403,35496,35640,35651,35662,35779,35804,35853,35900,35911,35922,36160,36171,36182,36420,36431,36442,36584,36633,36680,36691,36702,36940,36951,36962,37200,37211,37222,37460,37471,37482,37720,37731,37742,37980,37991,38002,38240,38251,38262,38500,38511,38522,38825,38836,38847,39074,39085,39096,39323,39334,39345,39572,39583,39594,39821,39832,39843,40070,40081,40092,40319,40330,40341,40568,40579,40590,40817,40828,40839,40910,41066,41077,41088,41315,41326,41337,41564,41575,41586,41872,41873,41893,41904,42108,42109,42129,42140,42340,42341,42361,42372,42576,42577,42597,42608,42812,42813,42833,42844,43048,43049,43069,43080,43284,43285,43305,43316,43520,43521,43541,43552,43756,43757,43777,43788,43992,43993,44013,44024,44228,44229,44249,44260,44464,44465,44485,44496,44766,44767,44787,44798,45002,45003,45023,45034,45234,45235,45255,45266,45470,45471,45491,45502,45706,45707,45727,45738,45942,45943,45963,45974,46178,46179,46199,46210,46414,46415,46435,46446,46650,46651,46671,46682,46886,46887,46907,46918,47122,47123,47143,47154,47358,47359,47379,47390,47469,47710,47712,47859,47990,47992,48270,48272,48550,48552,48830,48832,49120,49122,49131,49142,49163,49390,49392,49539,49670,49672,49950,49952,50230,50232,50510,50512,50790,50792,51070,51072,51350,51352,51706,51708,51986,51988,52266,52268,52546,52548,52822,52824,53020,53112,53114,53123,53134,53155,53382,53384,53662,53664,53942,53944,54222,54224,54502,54504,54782,54784,55062,55064,55342,55344]
o=[1,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,8,3,2,8,3,2,1,2,1,2,1,2,1,2,4,2,1,2,8,10,2,2,8,10,10,1,8,4,2,8,10,10,1,8,4,2,8,10,10,1,8,4,2,8,10,10,1,8,4,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,10,1,8,4,2,2,8,10,2,8,10,2,8,10,2,8,10,2,2,2,2,2,1,2,1,2,1,2,8,3,2,8,3,2,8,10,2,2,8,3,2,8,3,2,1,2,1,2,1,2,1,2,8,10,2,8,10,2,8,10,2,8,10,2,1,2,1,2,8,3,2,8,3,2,8,3,2,8,3,2,8,10,10,1,8,4,2,8,10,10,1,8,4,2,8,10,10,1,8,4,2,8,10,10,1,8,4,2,8,3,2,8,3,1,2,4,2,8,10,2,2,1,1,1,2,8,10,10,2,1,2,2,8,2,2,4,2,4,2,8,2,2,8,2,2,4,2,8,2,2,1,2,8,2,2,8,2,2,4,2,8,2,2,8,10,2,8,10,2,1,2,1,2,2,2,2,2,2,8,2,2,1,2,4,2,8,2,2,1,2,1,2,2,8,2,2,8,10,10,1,8,10,2,2,2,8,10,10,2,8,2,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,1,2,8,10,10,1,2,8,10,10,1,2,8,10,10,1,2,8,10,10,1,1,2,8,10,10,2,1,2,8,10,10,1,2,8,10,10,1,2,2,8,10,10,1,2,8,10,10,1,2,8,10,10,1,2,8,10,10,1,2,8,8,2,8,8,2,8,8,2,8,8,2,8,8,2,8,8,2,8,8,2,8,8,2,8,10,2,2,8,10,2,2,8,10,10,2,8,10,10,2,2,2,2,2,8,10,10,2,8,10,10,2,8,10,10,2,8,10,10,2,8,10,10,2,8,10,10,2,8,10,10,2,8,10,10,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,8,3,2,8,3,2,8,10,10,2,8,10,10,1,8,4,10,10,2,2,8,10,10,1,8,4,2,8,10,10,1,8,4,2,8,10,3,2,4,2,2,2,8,10,10,1,8,4,10,10,10,1,8,10,10,1,2,8,10,10,1,1,1,4,2,8,10,10,1,8,10,10,10,10,10,10,10,2,8,10,10,1,8,10,10,10,10,1,8,10,10,1,1,10,6,2,8,10,10,1,8,10,1,2,8,10,10,1,8,4,1,1,2,8,6,6,6,4,2,1,1,2,8,10,10,1,8,6,1,1,1,6,6,2,8,6,2,8,6,2,2,8,10,10,10,2,8,10,10,1,8,4,1,6,10,2,2,4,10,2,2,2,2,2,8,8,8,1,8,4,1,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,10,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,1,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,10,10,2,2,1,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,2,8,10,10,1,8,4,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,2,2,8,10,10,1,8,4,2,2,2,2,1,2,2,2,2,2,2,6,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,1,2,2,2,1,2,1,2,8,10,10,1,8,4,2,1,2,1,2,8,10,10,1,8,4,2,8,10,2,2,8,10,2,1,1,7,10,4,1,1,7,10,4,1,2,10,10,10,1,1,1,10,10,10,10,10,10,10,10,10,1,1,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,1,10,10,10,10,10,10,10,10,10,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,19,10,5,1,2,7,1,2,7,2,7,2,7,2,7,2,8,10,10,1,2,7,1,2,7,2,7,2,7,2,7,2,7,2,7,2,7,2,7,2,7,2,7,2,7,2,7,1,2,8,10,10,1,2,7,2,7,2,7,2,7,2,7,2,7,2,7,2,7]
b.sort()
for i,j,k in zip(m,n,o):
	for x in range(k):
		b.insert(j+x,b.pop(i+j+x))
json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)
