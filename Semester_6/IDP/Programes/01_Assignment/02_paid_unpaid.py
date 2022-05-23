def paid_or_unpaid(salary):
    if salary<3:
        return 'paid'
    elif salary<8:
        return 'unpaid'
    else:
        return 'paid'

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
                (76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), 
                (83000, 10),(48000, 1.9), (63000, 4.2)]
                
for _, tenures in salaries_and_tenures:
    print(tenures,paid_or_unpaid(tenures))