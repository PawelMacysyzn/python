from urllib import request
import requests




def rest_API(response):
    if (response.status_code != requests.codes.ok):
        print('Something went wrong')
    else:
        print(response.json())

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

rest_API(response)

'''
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
'''

print('------------------------------'*3)

response = requests.get('https://jsonplaceholder.typicode.com/posts/100')

rest_API(response)

'''
{'userId': 10, 'id': 100, 'title': 'at nam consequatur ea labore ea harum', 'body': 'cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut'}  
'''

print('------------------------------'*3)

response = requests.get('https://jsonplaceholder.typicode.com/posts/101')

rest_API(response)

'''
Something went wrong
'''

#------------------------------------------------------------------------------
print('####################'*3, '\n')
#------------------------------------------------------------------------------

requestBody = {
    'title' : 'Nasz tytul ',
    'body' : 'Tresc posta',
    'userID' : 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json= requestBody)

if (response.status_code != requests.codes.created):
    print('Something went wrong')
else:
    print(response.json())

'''
{'title': 'Nasz tytul ', 'body': 'Tresc posta', 'userID': 1, 'id': 101}
'''