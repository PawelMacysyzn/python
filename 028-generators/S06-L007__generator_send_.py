def double_inputs():
    while True:
        x = yield
        yield x * 2



# ==========       yield      ========
# Generator |   ------------> | User |
# ==========                  ========



# ==========       yield       ========
# Generator |   ------------>  | User |
# ==========    <------------  ========
#                   send




gen = double_inputs()
print(next(gen))       # run up to the first yield
# None

print(gen.send(10))   # goes into 'x' variable
# 20

print(next(gen))       # run up to the next yield
# None

print(gen.send(6))     # goes into 'x' again
# 12

print(next(gen))      # run up to the next yield
# None

print(gen.send(94.3))  # goes into 'x' again
# 188.6