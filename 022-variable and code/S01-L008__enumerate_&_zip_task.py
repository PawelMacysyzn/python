projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']


for pro, lead in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(pro, lead))
'''
The leader of "Brexit" is Theresa May
The leader of "Nord Stream" is Wladimir Putin
The leader of "US Mexico Border" is Donald Trump and Bill Clinton
'''

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

# for date, (pro, lead) in zip(dates, zip(projects, leaders)):
# or
for date, pro, lead in zip(dates, projects, leaders):
    print('The leader of "{}" started {} is {}'.format(pro, date, lead))
'''
The leader of "Brexit" started 2016-06-23 is Theresa May
The leader of "Nord Stream" started 2016-08-29 is Wladimir Putin
The leader of "US Mexico Border" started 1994-01-01 is Donald Trump and Bill Clinton
'''

for num, (date, (pro, lead)) in enumerate(zip(dates, zip(projects, leaders))):
    print('{}. - The leader of "{}" started {} is {}'.format(num + 1, pro, date, lead))
'''
1. - The leader of "Brexit" started 2016-06-23 is Theresa May
2. - The leader of "Nord Stream" started 2016-08-29 is Wladimir Putin
3. - The leader of "US Mexico Border" started 1994-01-01 is Donald Trump and Bill Clinton
'''