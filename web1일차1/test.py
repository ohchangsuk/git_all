data = [('a', 'a', '가', 12, datetime.datetime(2019, 12, 27, 14, 15, 13)), ('b', 'b', '나', 22, datetime.datetime(2019, 12, 27, 14, 15, 17)), ('c', 'c', '다', 33, datetime.datetime(2019, 12, 27, 14, 15, 19)), ('d', 'd', '오tetime.datetime(2019, 12, 27, 14, 15, 17)), ('c', 'c', '다', 33, datetime.datetime(2019, 12e.datetime(2019, 12, 27, 6, 51, 47)), ('f', '1', 'f', 123, datetime.datetime(2019, 12, 27, 7, 12, 47)), ('r', 'd', 'k', 12, d, 27, 14, 15, 19)), ('d', 'd', '오', 23, datetime.datetime(2019, 12, 27, 6, 49, 23)), ('ocs13', '1234', '오창석', 28, datetime.datetime(2019, 12, 27, 6, 51, 47)), ('f', '1', 'f', 123, datetime.datetime(2019, 12, 27, 7, 12, 47)), ('r', 'd', 'k', 12, datetime.datetime(2019,
12, 27, 7, 29, 14))]
 sum=0
    for i in data :
        a,b,c,d,e = i
        sum+=d
    print(sum)