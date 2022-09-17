# Zaimplementuj program, który przygotowuje środowisko do pracy. Uruchom 5 dowolnych procesów


import subprocess
import os
import time


def startCalc(path):
    try:
        x = subprocess.Popen(path)
        x.wait()
    except Exception as exc:
        print('Errrr..{} \n with: {}'.format(exc, path))


# startCalc('Notepad')
# startCalc('putty')


# code = r'C:\Users\pmacyszyn_adm\AppData\Local\Programs\Microsoft VS Code\Code.exe'
# startCalc(code)

# chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# startCalc(chrome)


def main():
    startCalc('calc.exe')
    time.sleep(5)

if __name__ == '__main__':
    main()
