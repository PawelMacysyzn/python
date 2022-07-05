import datetime 


netto = 100
brutto = 120
# netto must be less or equal to brutto
assert netto <= brutto, 'Netto cannot be greater than brutto'


orderDate = datetime.date(2022, 11, 13)
deliveryDate = datetime.date(2022, 10, 18)
# order date should be earlier than the delivery date 
assert orderDate <= deliveryDate, "Order date cannot be later than delivery date"