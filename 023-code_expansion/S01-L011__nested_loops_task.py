ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
#  len(ports) == 15       

routes = [(start, stop) for start in ports for stop in ports]
print(len(routes))  # 225

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(len(routes))  # 210


routes = [(start, stop) for start in ports for stop in ports if start > stop]
print(len(routes))  # 105


# for route in routes:
#     print(route)