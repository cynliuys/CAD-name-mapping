import json,sys
a,b = json.load(open(sys.argv[1]))
m=[10,18,28,38,48,58,68,78,88,10,19,10,18,10,19,10,18,10,19,10,18,10,19,2,10,18,28,38,48,58,68,78,88,10,19,10,18,10,19,10,18,10,19,10,18,10,19,2,10,18,28,38,48,58,68,78,88,10,19,10,18,10,19,10,18,10,19,10,18,10,19,2,8,18,28,38,48,58,66,9,8,9,8,9,8,8,18,28,38,48,58,66,9,8,9,8,9,8,8,18,28,38,48,58,66,9,8,9,8,9,8,4,14,24,34,44,48,9,9,9,4,14,24,34,44,48,9,9,9,8,18,28,38,48,58,66,9,8,9,8,9,8,8,18,28,38,48,58,66,9,8,9,8,9,8,8,18,28,38,48,58,66,9,8,9,8,9,8,4,14,24,34,44,48,9,9,9,4,14,24,34,44,48,9,9,9,10,20,26]
n=[921,934,935,936,937,938,939,940,941,942,943,953,954,956,965,975,976,978,987,997,998,1000,1009,1019,1170,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1202,1203,1205,1214,1224,1225,1227,1236,1246,1247,1249,1258,1268,1282,1295,1296,1297,1298,1299,1300,1301,1302,1303,1304,1314,1315,1317,1326,1336,1337,1339,1348,1358,1359,1361,1370,1380,2061,2062,2063,2064,2065,2066,2067,2070,2081,2092,2103,2114,2125,2161,2162,2163,2164,2165,2166,2167,2170,2181,2192,2203,2214,2225,2257,2258,2259,2260,2261,2262,2263,2266,2277,2288,2299,2310,2321,2403,2404,2405,2406,2407,2408,2413,2429,2445,2467,2468,2469,2470,2471,2472,2477,2493,2509,2538,2539,2540,2541,2542,2543,2544,2547,2558,2569,2580,2591,2602,2642,2643,2644,2645,2646,2647,2648,2651,2662,2673,2684,2695,2706,2738,2739,2740,2741,2742,2743,2744,2747,2758,2769,2780,2791,2802,2831,2832,2833,2834,2835,2836,2841,2857,2873,2895,2896,2897,2898,2899,2900,2905,2921,2937,2953,2954,2955]
o=[13,1,1,1,1,1,1,1,1,1,10,1,2,9,10,1,2,9,10,1,2,9,2,1,13,1,1,1,1,1,1,1,1,1,10,1,2,9,10,1,2,9,10,1,2,9,2,1,13,1,1,1,1,1,1,1,1,1,10,1,2,9,10,1,2,9,10,1,2,9,2,1,1,1,1,1,1,1,2,10,2,10,2,10,2,1,1,1,1,1,1,2,10,2,10,2,10,2,1,1,1,1,1,1,2,10,2,10,2,10,2,1,1,1,1,1,4,6,6,6,1,1,1,1,1,4,6,6,6,1,1,1,1,1,1,2,10,2,10,2,10,2,1,1,1,1,1,1,2,10,2,10,2,10,2,1,1,1,1,1,1,2,10,2,10,2,10,2,1,1,1,1,1,4,6,6,6,1,1,1,1,1,4,6,6,6,1,1,7]
b.sort()
for i,j,k in zip(m,n,o):
	for x in range(k):
		b.insert(j+x,b.pop(i+j+x))
json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)
