# -*- coding: utf-8 -*-

import traceback
import logging
import datetime
from time import localtime
import os
import behave.test.test_axob as behave

if __name__== '__main__':
    myname = os.path.split(__file__)[1][:-3]
    mytime = str(datetime.datetime(*localtime()[:6])).replace(':',"").replace('-',"").replace(" ","_")

    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(f'log/{myname}_{mytime}.log')
    # fh = logging.FileHandler(f'log/{myname}.log', mode='w')
    fh.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setLevel(logging.WARNING)

    formatter_ts = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter_nts = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter_nts)
    sh.setFormatter(formatter_ts)

    logger.addHandler(fh)
    logger.addHandler(sh)

    ###测试20221010所有有委托的只股票，全天
    fh.setLevel(logging.WARN)
    sh.setLevel(logging.ERROR)
    logger.info('starting TEST_axob_bat')
    data_source = "data/20221010/sbe_20221010_all.log"
    all_inc=[200054, 200512, 200030, 200045, 200553, 200011, 200020, 200530, 200025, 300996, 200028, 200152, 301059, 200706, 200550, 200037, 200521, 200505, 200056, 300354, 300930, 301066, 300980, 200029, 200055, 300508, 200019, 200026, 300668, 2569, 200992, 200017, 200761, 300870, 2485, 2870, 200570, 301072, 200581, 200413, 300733, 300069, 300654, 201872, 300916, 200771, 2857, 972, 200541, 200058, 2972, 301099, 300530, 301004, 504, 300757, 2735, 300645, 2692, 300948, 200016, 2200, 300885, 2058, 200468, 300833, 300622, 301239, 200726, 300876, 301106, 2975, 200429, 301057, 300550, 300897, 300791, 300521, 2779, 300892, 300964, 301097, 300489, 300984, 300523, 300971, 300426, 300779, 300515, 301020, 301049, 300816, 300958, 300982, 300715, 300986, 2724, 301012, 301182, 300417, 300906, 300938, 300399, 301036, 300955, 300695, 2881, 301023, 301063, 300614, 300512, 301118, 300694, 3010, 300089, 300670, 300462, 300711, 2942, 200488, 300667, 301065, 301043, 2787, 301186, 200596, 300995, 300749, 2748, 2930, 300952, 301229, 2722, 301005, 300657, 2929, 300588, 300538, 300840, 2912, 2313, 300826, 300837, 300516, 300594, 2159, 695, 300557, 2088, 300658, 300445, 300536, 2066, 301051, 300852, 301031, 301000, 3003, 301133, 301068, 300796, 300275, 300631, 300743, 300931, 301076, 2052, 2072, 3026, 300391, 2420, 300548, 300895, 300277, 300626, 2879, 300475, 2802, 300873, 300946, 300580, 300570, 301083, 2301, 300824, 2211, 2577, 300886, 300211, 300893, 300790, 300960, 628, 300341, 300817, 301042, 301008, 300651, 2968, 32, 300478, 300492, 301167, 300518, 301257, 534, 301169, 300349, 300862, 2933, 300713, 300854, 2095, 809, 300561, 300806, 300051, 300243, 300414, 300985, 300096, 586, 2851, 971, 300384, 300280, 300652, 2718, 2961, 2346, 2836, 2778, 200869, 1288, 2729, 300407, 300400, 200539, 300932, 3025, 300752, 300756, 301138, 300560, 300969, 2910, 2331, 2671, 300843, 2790, 300380, 1211, 2571, 300488, 300901, 300798, 301080, 300621, 301349, 1205, 300600, 4, 300947, 300920, 301037, 410, 2998, 300976, 300720, 300473, 300356, 300894, 301193, 752, 2913, 2847, 300905, 1207, 300717, 300858, 301149, 2990, 300690, 2832, 301221, 301067, 301129, 300781, 2963, 2586, 300847, 300857, 300731, 2861, 2499, 2417, 300977, 659, 2923, 300564, 301168, 300787, 2971, 2771, 300381, 300818, 301009, 300935, 300258, 300192, 301092, 300880, 2740, 300907, 300811, 300844, 2977, 300675, 300579, 300812, 301019, 300265, 301237, 2259, 803, 300405, 300684, 300851, 300723, 301058, 300746, 300853, 300936, 1217, 301180, 3033, 2552, 2991, 300281, 300848, 300637, 300442, 300991, 300226, 300500, 301198, 301101, 300334, 2995, 2940, 301010, 300923, 1210, 301283, 2890, 301113, 301213, 3042, 2054, 300810, 300681, 2973, 2869, 300632, 300154, 300549, 300941, 300669, 300683, 301179, 300809, 300730, 2069, 300698, 2376, 300771, 300786, 300701, 300970, 300882, 300913, 301107, 590, 300220, 300642, 300539, 2590, 2872, 300939, 300392, 300987, 300624, 300547, 300161, 300434, 300998, 2887, 300789, 300849, 301085, 301130, 2848, 300697, 2919, 509, 300385, 300899, 300484, 301333, 300583, 300656, 301022, 2758, 301248, 300514, 300522, 300406, 300555, 300461, 301082, 301195, 3017, 301117, 300610, 300389, 301086, 2214, 301162, 300640, 301024, 691, 301312, 300909, 301222, 2086, 300151, 300155, 300486, 300767, 2988, 2931, 300314, 301188, 301081, 301148, 300491, 2859, 301131, 301070, 300700, 301102, 300143, 300855, 300802, 3008, 300025, 301116, 301026, 300949, 2674, 2213, 300150, 301055, 2395, 2981, 2637, 300918, 300221, 300578, 301178, 300943, 2322, 300953, 3007, 300838, 996, 300293, 300988, 906, 300606, 300845, 2698, 300103, 2777, 200725, 300933, 301016, 2741, 300030, 2983, 300788, 2786, 2979, 532, 2678, 301119, 301061, 301032, 26, 2831, 300989, 300374, 300174, 300235, 890, 300611, 301139, 300705, 2381, 301062, 300440, 300721, 301136, 2483, 2105, 300535, 301321, 300823, 2849, 2937, 2504, 300829, 301289, 2102, 2360, 2970, 2694, 300795, 300865, 2014, 301279, 300394, 300706, 2609, 301006, 300956, 300411, 300921, 2993, 300218, 2886, 300951, 300554, 300968, 300808, 300997, 806, 300993, 301125, 301108, 300305, 300410, 300753, 300959, 300961, 2595, 301201, 300283, 626, 2664, 301045, 300272, 2193, 300576, 2227, 301003, 300972, 300236, 301259, 5, 2808, 300922, 3015, 300517, 2021, 301288, 300162, 300490, 2775, 301166, 2521, 300649, 301151, 300313, 300928, 300994, 2209, 2401, 300815, 300290, 2986, 300647, 2801, 300825, 2669, 2755, 300585, 300722, 300963, 300609, 301093, 300747, 300597, 300619, 2687, 2357, 300912, 300800, 300898, 2760, 300902, 669, 300679, 2798, 300641, 300644, 2980, 301013, 300441, 300978, 2686, 2732, 2076, 2636, 300298, 2358, 301160, 300531, 2825, 301079, 301033, 779, 300835, 301126, 3038, 300927, 301256, 300333, 300278, 300375, 300469, 300738, 2811, 2324, 300169, 300234, 300577, 2721, 96, 300636, 300599, 2327, 300419, 301052, 200012, 300864, 300572, 1313, 300975, 2842, 301047, 300828, 300200, 635, 300225, 301181, 2247, 576, 301096, 301007, 153, 2892, 301028, 301029, 301046, 2522, 300680, 2730, 300617, 1228, 300286, 523, 300605, 301077, 301206, 301228, 2853, 2653, 2198, 300739, 300868, 300662, 2830, 301211, 300455, 300126, 300925, 1215, 3016, 301053, 300871, 300891, 2672, 300245, 300615, 301197, 300085, 300231, 300513, 300686, 300805, 300076, 301098, 2098, 300453, 300382, 301163, 300889, 300643, 2956, 679, 2388, 300227, 2608, 2116, 766, 2734, 300141, 300571, 301120, 2806, 300678, 2845, 300665, 300712, 3031, 2763, 2927, 301112, 2696, 1208, 720, 2544, 2900, 300219, 300537, 300153, 2099, 2356, 301263, 935, 300807, 2438, 910, 300329, 300860, 300732, 300856, 3028, 300940, 300504, 300321, 2574, 300608, 2833, 2122, 300543, 301218, 300427, 300429, 300562, 2144, 300590, 300575, 2005, 300559, 300607, 300648, 2899, 301041, 300366, 3009, 300378, 300691, 300291, 2766, 300107, 2893, 300183, 2824, 300965, 300553, 300628, 300910, 300368, 48, 2397, 2250, 301038, 300386, 300727, 300421, 300240, 301122, 300501, 2293, 300416, 3019, 300780, 300167, 2535, 300371, 915, 300360, 2199, 300942, 300470, 300173, 300620, 2633, 300444, 300911, 300209, 2996, 2184, 300338, 300591, 301156, 2423, 300834, 300330, 300966, 608, 2782, 300839, 300011, 300424, 2287, 300890, 548, 300877, 70, 403, 300370, 300452, 2816, 300342, 56, 300210, 300841, 2282, 2749, 300596, 300466, 1206, 301159, 300042, 300248, 300710, 301035, 2949, 300134, 300768, 708, 2813, 300831, 23, 300556, 301087, 2203, 300195, 300149, 11, 300270, 300300, 300004, 1319, 301027, 828, 705, 300097, 2153, 1212, 301298, 2838, 300540, 300175, 300288, 2494, 301025, 301002, 2392, 300703, 300702, 300120, 2855, 301220, 301278, 300306, 300005, 300673, 38, 300687, 300230, 300447, 300688, 300460, 300983, 300689, 300203, 301189, 2318, 737, 2134, 2706, 2338, 301192, 2984, 301185, 301338, 300350, 300836, 2502, 300396, 301078, 1309, 300719, 300266, 2957, 3036, 300766, 3001, 300279, 300638, 2978, 301001, 10, 300099, 300659, 301056, 301286, 300546, 301191, 29, 300250, 300344, 2096, 300395, 300602, 300881, 300264, 300532, 2308, 3032, 301318, 300190, 300506, 300332, 300685, 300866, 301100, 2843, 300915, 300520, 300425, 2796, 1219, 2484, 300246, 300318, 300801, 30, 300908, 300365, 300867, 300423, 300092, 300340, 301200, 301209, 2328, 300214, 913, 2362, 300256, 632, 2915, 300357, 301103, 300163, 300471, 985, 300499, 300625, 301110, 300582, 300736, 2889, 300301, 300566, 300322, 962, 2823, 2902, 300139, 1872, 300205, 301048, 301150, 2114, 300241, 2827, 2767, 300480, 2690, 300542, 300215, 300765, 2743, 2451, 2953, 300388, 300887, 2399, 300630, 300563, 2960, 2243, 2295, 553, 300331, 2315, 850, 300900, 2430, 2878, 2875, 300509, 710, 300846, 300034, 2841, 2187, 301121, 886, 2683, 301075, 300692, 2950, 2846, 300729, 300259, 688, 2576, 300745, 526, 300449, 2753, 2528, 301123, 300320, 300990, 301015, 698, 2453, 2253, 2029, 2365, 300262, 2025, 300238, 2655, 300255, 2679, 300799, 701, 300135, 692, 1226, 300581, 531, 300708, 3039, 300019, 300140, 301091, 2189, 2769, 300029, 300437, 2858, 300208, 607, 300950, 2172, 300310, 300878, 300016, 300041, 301266, 300446, 2556, 2559, 300584, 300493, 2659, 301190, 300257, 2416, 300526, 300050, 2441, 2513, 7, 301300, 300196, 300454, 300055, 300289, 3020, 2170, 301187, 2117, 301258, 300945, 300879, 300100, 300254, 300830, 2599, 2006, 2136, 2654, 301196, 925, 2719, 2757, 300774, 2345, 833, 300567, 300276, 300682, 2667, 2898, 300242, 1323, 2347, 300422, 300832, 2316, 1289, 605, 300616, 2034, 2398, 300510, 565, 2319, 2016, 2888, 301011, 301128, 2015, 301017, 2019, 2946, 2368, 757, 301135, 301073, 2479, 300552, 2123, 2976, 551, 2300, 2406, 2876, 301040, 2715, 300309, 300056, 2290, 301155, 300797, 2333, 300067, 2224, 2017, 300627, 300066, 300635, 533, 300304, 300086, 300319, 200625, 300487, 300213, 711, 2028, 2959, 819, 300467, 300351, 995, 2150, 301302, 2238, 2288, 633, 301090, 2229, 2501, 2516, 301021, 300598, 2410, 300770, 300095, 300121, 300415, 300040, 2320, 300937, 859, 2799, 37, 2053, 922, 2999, 300439, 300106, 300979, 2877, 300369, 2482, 300737, 300074, 300660, 655, 300725, 2097, 300716, 1229, 300519, 2434, 300819, 2448, 2605, 993, 300709, 300252, 300842, 2449, 300973, 2772, 300108, 1202, 1216, 300307, 301111, 2681, 2871, 2219, 300861, 2731, 300387, 802, 919, 2009, 300317, 300172, 2652, 58, 300402, 2264, 301306, 300269, 2616, 300294, 300302, 301234, 300755, 2040, 2262, 2727, 300187, 300112, 301088, 798, 300863, 2880, 3043, 2541, 928, 300063, 300603, 300229, 567, 300783, 301205, 900, 2780, 2868, 300102, 2768, 2829, 301127, 300792, 300168, 300592, 541, 300629, 2575, 300589, 2826, 839, 300726, 2695, 2921, 2232, 2440, 17, 813, 300032, 862, 639, 2752, 666, 606, 2190, 2785, 300545, 300048, 2321, 1696, 869, 2363, 300718, 2662, 2985, 300762, 2428, 301069, 300137, 631, 2296, 2676, 2462, 2644, 2206, 2632, 300018, 300165, 300193, 2012, 2235, 2344, 300232, 300078, 967, 2651, 300903, 300336, 2351, 300741, 700, 2675, 2055, 905, 818, 300198, 300176, 300180, 300222, 936, 2225, 301207, 300352, 672, 2281, 300528, 300661, 2303, 2928, 2862, 566, 572, 571, 300311, 2161, 409, 976, 823, 300328, 301208, 902, 990, 3006, 2082, 2645, 2515, 300031, 301030, 955, 301132, 2691, 2112, 2661, 2491, 300132, 300160, 300020, 2545, 300123, 2623, 300448, 2982, 2141, 300919, 300046, 300663, 301177, 2883, 2221, 2725, 300268, 2138, 2378, 2643, 16, 300957, 301217, 300926, 300435, 300541, 300534, 893, 300888, 2367, 2867, 3011, 300188, 300465, 880, 300412, 2457, 300612, 2026, 300271, 2452, 300533, 2781, 1270, 300353, 1914, 301233, 2093, 300239, 761, 300359, 300558, 682, 301226, 1234, 300428, 2810, 300233, 300494, 301137, 2087, 2582, 2611, 1296, 719, 300062, 753, 923, 2283, 300285, 2728, 300650, 300323, 2286, 300443, 300457, 300337, 2536, 1268, 300295, 300593, 301326, 3030, 2792, 2626, 150, 2354, 2263, 2573, 300119, 889, 2228, 2387, 300125, 2361, 1231, 524, 2111, 2557, 2649, 300735, 300377, 2275, 2997, 300247, 300664, 2646, 2163, 300981, 2201, 300131, 789, 300179, 300485, 300420, 2540, 2226, 2003, 300696, 300674, 2083, 2067, 300481, 2922, 2057, 300761, 536, 2815, 2323, 300212, 2708, 2254, 903, 2222, 2519, 2621, 300634, 301270, 300869, 3002, 2712, 597, 301276, 2309, 3021, 300511, 2106, 300013, 2010, 2627, 2965, 300587, 301236, 911, 300083, 2085, 2291, 301215, 300197, 2474, 2658, 301018, 2248, 785, 2178, 2130, 2955, 300138, 2140, 2606, 300358, 301050, 300072, 300036, 2215, 3013, 2421, 1896, 637, 1317, 300586, 2023, 2481, 782, 537, 2366, 2533, 300148, 2564, 610, 300436, 2534, 300077, 300113, 2391, 2386, 561, 2776, 2270, 1213, 300404, 426, 2873, 300883, 2788, 301039, 301158, 34, 2759, 2255, 557, 300045, 657, 2158, 826, 19, 2613, 616, 301161, 726, 2208, 300105, 1965, 300364, 601, 2149, 973, 300022, 300822, 2992, 599, 2177, 989, 2549, 300464, 415, 31, 2666, 885, 300082, 300114, 301071, 300345, 430, 1308, 2529, 2108, 987, 791, 2762, 2546, 2840, 851, 1203, 2160, 301231, 300127, 300769, 544, 2918, 981, 2492, 2425, 2967, 2284, 300130, 2427, 2638, 300655, 6, 300324, 3012, 45, 300740, 300479, 2906, 300098, 2047, 300177, 300084, 615, 300527, 2343, 966, 2751, 676, 1201, 2181, 300299, 159, 300053, 300061, 2596, 2341, 300671, 2369, 2819, 707, 2455, 2916, 2593, 301235, 420, 300775, 2700, 2194, 507, 2737, 301296, 2039, 2523, 300497, 300707, 2660, 2302, 300043, 2412, 820, 2446, 300047, 2375, 301308, 300244, 2467, 2688, 61, 301199, 301212, 300079, 2583, 790, 2180, 300477, 529, 301216, 300292, 609, 681, 596, 300623, 2370, 2488, 2558, 300772, 958, 156, 2373, 2538, 300472, 300793, 300618, 300284, 300145, 2004, 2103, 301309, 2048, 2043, 2587, 587, 2298, 300057, 2943, 158, 2167, 2566, 300398, 2429, 2063, 300303, 2154, 2642, 2935, 300507, 301183, 2705, 2274, 2820, 3037, 301328, 901, 300525, 300049, 417, 2527, 949, 2563, 300573, 300401, 99, 2137, 525, 65, 1336, 2174, 2350, 2109, 2863, 300896, 300237, 917, 2164, 2941, 300091, 301115, 969, 300821, 300672, 703, 2895, 2435, 518, 300308, 300147, 300569, 50, 301227, 570, 301330, 301219, 300776, 718, 20, 2132, 652, 3000, 300850, 2917, 777, 300181, 539, 300814, 419, 300505, 2413, 2355, 3035, 2268, 2803, 301175, 555, 559, 2119, 300503, 300476, 300260, 501, 2294, 751, 2133, 2635, 2818, 300054, 2041, 300117, 300917, 2186, 2217, 912, 300191, 2945, 950, 680, 300267, 811, 2562, 300613, 503, 300803, 300109, 300884, 301282, 300297, 2348, 543, 2588, 300409, 300021, 300006, 300002, 2581, 2911, 2746, 300355, 563, 2424, 300111, 300012, 997, 812, 717, 300456, 505, 2550, 690, 2951, 300071, 300742, 2396, 2311, 2578, 300129, 300967, 2068, 300007, 2042, 300159, 2885, 2409, 2402, 300962, 2337, 300052, 300296, 300327, 2454, 2380, 300929, 300001, 300397, 2404, 300820, 301109, 1266, 959, 2702, 2073, 21, 2278, 877, 300128, 800, 510, 2612, 2510, 2882, 2242, 300065, 300751, 300676, 685, 300194, 300115, 408, 90, 2332, 2307, 2390, 600, 498, 2512, 2891, 2306, 2498, 2075, 908, 300199, 712, 2168, 2791, 816, 2297, 2989, 2663, 2745, 2188, 2384, 2765, 300152, 300502, 838, 2701, 2233, 2125, 2089, 2266, 2496, 2625, 2952, 2258, 488, 796, 2032, 2237, 28, 300157, 2783, 603, 881, 2212, 300204, 793, 300758, 883, 300458, 528, 2677, 300224, 2091, 62, 3040, 2742, 2090, 300633, 2261, 2656, 301339, 2280, 755, 2597, 861, 2110, 423, 2756, 852, 300748, 2051, 2126, 2445, 2113, 300827, 2807, 300551, 2461, 988, 2265, 2151, 301060, 300075, 702, 1339, 2152, 300451, 2046, 2852, 612, 758, 2822, 582, 300249, 300070, 2038, 55, 300033, 300379, 300468, 300184, 301366, 2081, 300813, 2059, 2835, 767, 2962, 300316, 300408, 2539, 1209, 2036, 300773, 300080, 2020, 2682, 2905, 300035, 733, 301095, 550, 2383, 2135, 2310, 2107, 951, 300037, 2500, 300483, 2631, 1283, 301238, 404, 300495, 2400, 300136, 300189, 3029, 2723, 2947, 836, 2793, 738, 788, 815, 921, 300463, 2436, 300223, 2249, 2330, 1318, 2374, 678, 2216, 2495, 300010, 300287, 2439, 589, 581, 300263, 665, 300376, 2925, 636, 300474, 300273, 2336, 429, 300992, 520, 300403, 686, 2864, 59, 627, 930, 2837, 300017, 300693, 2591, 27, 300383, 663, 2478, 2939, 301089, 300666, 918, 300432, 35, 2517, 2444, 300087, 42, 300110, 517, 892, 2470, 2065, 2520, 888, 2162, 2628, 300009, 1218, 2657, 2800, 3018, 2080, 78, 2173, 2565, 2120, 2155, 25, 300859, 729, 2443, 713, 2920, 300228, 3022, 2252, 2932, 300081, 2442, 300529, 622, 2903, 401, 300604, 2493, 300373, 300027, 727, 2526, 2171, 300777, 999, 2277, 2239, 2908, 2733, 516, 2285, 2469, 300346, 300724, 300146, 2045, 8, 2524, 1316, 863, 2505, 558, 2699, 300601, 963, 2909, 848, 300347, 2860, 2139, 39, 2061, 2697, 300595, 2468, 2615, 2673, 2078, 1222, 2736, 300170, 301327, 2317, 2353, 739, 300094, 2276, 2472, 301268, 878, 2422, 300261, 783, 2377, 300039, 2314, 2326, 301, 2011, 300158, 2938, 301336, 151, 49, 2292, 2948, 2127, 927, 301369, 300206, 960, 2289, 2580, 822, 300315, 2897, 2267, 2839, 2850, 2312, 300008, 982, 300699, 2966, 300363, 2471, 2299, 300073, 400, 2465, 300413, 300418, 2592, 300101, 650, 2431, 2079, 2437, 2530, 155, 300326, 2418, 1230, 300024, 938, 2364, 731, 2926, 2408, 810, 715, 2958, 2572, 786, 300251, 2511, 514, 2342, 300185, 2179, 300343, 735, 2183, 887, 300875, 300677, 300482, 953, 2629, 2598, 2210, 2648, 952, 2169, 300171, 598, 619, 617, 2148, 14, 2033, 300778, 2601, 2579, 301176, 300166, 592, 860, 623, 300058, 2382, 2414, 2809, 2547, 300182, 2584, 2585, 2553, 300759, 545, 875, 421, 750, 2602, 2403, 2805, 300496, 2145, 1332, 2101, 829, 2713, 300339, 2389, 3004, 2865, 897, 2273, 300433, 2548, 300565, 584, 3041, 300282, 668, 2761, 2531, 2372, 1259, 89, 2251, 2115, 2218, 300438, 546, 2329, 300782, 2668, 2789, 300116, 301152, 998, 2192, 2060, 595, 300568, 300763, 2007, 60, 300639, 931, 2600, 2726, 300335, 2245, 722, 2305, 300459, 301171, 157, 300207, 2821, 554, 301153, 2205, 2256, 926, 2456, 402, 2064, 1258, 2419, 2508, 300785, 968, 2560, 2717, 300430, 2191, 2092, 2244, 2689, 2411, 2231, 2570, 2234, 2146, 2707, 68, 2304, 300390, 732, 2561, 2182, 2774, 837, 422, 2797, 978, 2056, 898, 1331, 2747, 961, 825, 830, 2394, 683, 2062, 795, 2670, 573, 300653, 2812, 801, 300144, 2335, 2624, 2044, 2037, 300122, 762, 2607, 2024, 2325, 2555, 1227, 300348, 506, 909, 66, 2518, 2532, 778, 2969, 977, 2334, 300450, 2001, 2507, 2703, 547, 2480, 300164, 300217, 416, 2121, 2049, 2487, 2739, 425, 759, 975, 2634, 46, 2459, 868, 2486, 980, 661, 670, 2506, 932, 2405, 300999, 300872, 301285, 300093, 2094, 530, 882, 2175, 2639, 2936, 300118, 2185, 2223, 300088, 2030, 538, 2896, 9, 2542, 2202, 2156, 2339, 513, 2204, 301319, 540, 300044, 856, 2230, 2426, 799, 2503, 2856, 1236, 2568, 2407, 2128, 697, 2013, 301331, 69, 300393, 2131, 2008, 1979, 2630, 2385, 728, 2685, 2118, 2240, 821, 2157, 552, 2458, 2620, 2195, 2773, 667, 300760, 2074, 301269, 2272, 2100, 638, 899, 2352, 2077, 591, 970, 831, 797, 2622, 2463, 568, 1330, 2665, 88, 413, 2884, 2166, 12, 2142, 2035, 2433, 2271, 2907, 2104, 2617, 920, 721, 2738, 300014, 300003, 2554, 519, 166, 807, 2124, 709, 2709, 2279, 2022, 338, 300026, 2610, 2866, 300253, 2497, 2489, 300015, 2340, 2432, 301313, 2589, 768, 2537, 300068, 2567, 2640, 1238, 895, 2236, 2349, 2475, 428, 300133, 2176, 776, 656, 63, 2269, 300142, 723, 2490, 2371, 933, 630, 1267, 736, 2002, 957, 929, 300274, 671, 2027, 300498, 2207, 2050, 2129, 937, 1255, 2379, 3816, 2828, 300124, 2551, 716, 3027, 564, 560, 521, 2460, 2031, 983, 2543, 792, 100, 593, 2750, 876, 2987, 2241, 411, 2650, 629, 2901, 2415, 333, 2647, 36, 2817, 3005, 2603, 858, 2693, 2466, 677, 2476, 300750, 2714, 2594, 2393, 2, 651, 2795, 3023, 2165, 625, 2514, 40, 965, 2246, 2197, 2614, 1269, 756, 1, 620, 725, 300059, 948, 2641, 2084, 407]

    try:
        behave.TEST_axob_bat(data_source, all_inc, n_max=0, openCall_only=False) #
    except Exception as e:
        logger.error(f'{traceback.format_exc()}')