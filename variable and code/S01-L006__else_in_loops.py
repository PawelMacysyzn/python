import os, urllib.request

data_dir = r'c:\temp' # the "temp" folder must exist on "drive C"

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]


for page in pages:

    try: 
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)


        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve(page["url"], path)  
        print('...done\n')

    # except Exception as inst:
    #     print(type(inst))
    #     break

    except:
        print(' FAILURE processing web page: {}'.format(page["url"]))
        print('>>>\tStopping the process!')
        break
else:
    print('All pages downloaded successfully!!!')
