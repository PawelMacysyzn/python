import time

source = "reportLine += 1"
reportLine = 0

loops = 1000000



start = time.time()
for i in range(loops):
    reportLine += 1
stop = time.time()
delta_time_none = stop - start
reportLine = 0


start = time.time()
for i in range(loops):
    exec(source)
stop = time.time()
delta_time_none_compiled = stop - start


start = time.time()
sourceCompiled = compile(source, 'internal variable source', 'exec')
for i in range(loops):
    exec(sourceCompiled)
stop = time.time()
delta_time_compiled = stop - start


print("delta_time_none:     ",delta_time_none)
print("delta_time_none_compiled:",delta_time_none_compiled)
print("delta_time_compiled:     ",delta_time_compiled)
print("Bost :",delta_time_none_compiled / delta_time_compiled)
'''
delta_time_none:      0.04199814796447754
delta_time_none_compiled: 4.731774091720581
delta_time_compiled:      0.15699195861816406
Bost : 30.140232234628048
'''