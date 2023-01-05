# map()



store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00),]


to_euro = lambda data:(data[0],data[1]*0.95)
to_dollars = lambda data:(data[0],data[1]/0.95)

store_dollars = list(map(to_dollars,store))
store_euro = list(map(to_euro,store))

for i in store_dollars:
    print(i)