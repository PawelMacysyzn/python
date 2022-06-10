
# ------------------------------------------
mesage = "Enter int: "
# The walrus operator
print(x:=int(input(mesage)) + 6)
# ------------------------------------------



# ------------------------------------------
known_types = 'cake:muffin:meringue:biscuit:eclair:christmas:pretzel:other' # type<str>

# Nazwał bym to wyłuskiwaniem xd   *

print(*known_types)
'''
c a k e : m u f f i n : m e r i n g u e : b i s c u i t : e c l a i r : c h r i s t m a s : p r e t z e l : o t h e r
'''
print(known_types.split(':')) # type<list>
'''
['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
'''
print(*known_types.split(':')) # type<none>
'''
cake muffin meringue biscuit eclair christmas pretzel other

'''
# ------------------------------------------

# ------------------------------------------
import glob


f = glob.glob('c:/temp/*.txt')   # catalog/*.format_file

print(f)
# retururn list of .txt files 
# ------------------------------------------