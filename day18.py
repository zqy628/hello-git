#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
囚徒困境
https://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166421&idx=1&sn=f9db1120f591a6201ea60e59b41a50e2&chksm=be4b59ed893cd0fb0075e0dae51127837ac3ff5c257495084d11ed74d03b2523503252f284a0&scene=21#wechat_redirect
'''
nice = 'nice'
rat = 'rat'
tit_for_tat = 'tit_for_tat'
policy = {'nicenice': (1,1), 'nicerat': (5,0), 'ratnice': (0,5), 'ratrat': (2,2)}
def prisoner_delimma(N, strategy1, strategy2):
    p1_years, p2_years = 0, 0
    p1_sta, p2_sta = strategy1, strategy2
    for i in range(1, N+1):
        if strategy1 == 'tit_for_tat':
            p1_sta = 'nice' if i ==1 or p2_sta =='nice' else 'rat'
        if strategy2 == 'tit_for_tat':
            p2_sta = 'nice' if i == 1 or p1_sta =='nice' else 'rat'
        years1, years2 = policy[p1_sta + p2_sta]
        p1_years += years1
        p2_years += years2
    return p1_years, p2_years