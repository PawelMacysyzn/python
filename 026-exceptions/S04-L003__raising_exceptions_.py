def ProcessInvoice(netto, brutto) -> None:
    if netto >= brutto:
        raise ValueError('Netto should be lower or equal to brutto')
    else:
        print('Processing invoice: netto = {} brutto = {}'.format(netto, brutto))


def EndOfMonth():
    netto = 1230
    brutto = 1000

    try:
        ProcessInvoice(netto, brutto)

    except ValueError as e:
        print('The values on invoice are incorrect: {}'.format(e))
        raise ValueError('Error when procesing invoices') from e

    except Exception as e:
        print('Error processing invoice: {}'.format(e))


EndOfMonth()


'''
The values on invoice are incorrect: Netto should be lower or equal to brutto
Traceback (most recent call last):
  File "c:\Users\pmacyszyn_adm\Documents\python\python\026-exceptions\S04-L003__raising_exceptions_.py", line 13, in EndOfMonth
    ProcessInvoice(netto, brutto)
  File "c:\Users\pmacyszyn_adm\Documents\python\python\026-exceptions\S04-L003__raising_exceptions_.py", line 3, in ProcessInvoice
    raise ValueError('Netto should be lower or equal to brutto')
ValueError: Netto should be lower or equal to brutto

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:\Users\pmacyszyn_adm\Documents\python\python\026-exceptions\S04-L003__raising_exceptions_.py", line 23, in <module>
    EndOfMonth()
  File "c:\Users\pmacyszyn_adm\Documents\python\python\026-exceptions\S04-L003__raising_exceptions_.py", line 17, in EndOfMonth
    raise ValueError('Error when procesing invoices') from e
ValueError: Error when procesing invoices
'''