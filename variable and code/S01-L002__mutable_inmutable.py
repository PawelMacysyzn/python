import inspect, re

def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)


days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()

workdays.pop() # remember  
workdays.pop() # this method also returns the deleted value of the list

'''or 
workdays.remove('sat')
workdays.remove('sun')
'''

print(varname(days),": ",days)
print(varname(workdays),": ",workdays)