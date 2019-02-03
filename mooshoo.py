
def cashback(monthly_costs): #начало функции
    percent = 3
    print('Function called')
    result = percent * monthly_costs / 100
    return result #возврат значения, результат
print('Our program')
# value = cashback(10_000) #вызов функции + передача параметра
# print(value)
print(cashback(10_000))
print(cashback(20_000))