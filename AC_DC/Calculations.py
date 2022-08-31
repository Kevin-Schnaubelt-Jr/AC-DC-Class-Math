'''
This program calculates voltage, current, and resistance for a circuit.
'''


voltage = int(input('Enter Voltage.\n>: '))

resistance_series_str = input('Enter ohms of each resistor IN SERIES separated by a ","\n>: ')
resistance_series = resistance_series_str.split(',')
resistance_series = [int(i) for i in resistance_series]

resistance_parallel_str = input('Enter ohms of each resistor IN PARALLEL separated by a ","\n>: ')
resistance_parallel = resistance_parallel_str.split(',')
resistance_parallel = [int(i) for i in resistance_parallel]

# print(resistance_series, resistance_parallel)


resistance_parallel_total = 0
if 0 not in resistance_parallel:
    for ohms in resistance_parallel:
        resistance_parallel_total += 1/ohms
    resistance_parallel_total = 1/resistance_parallel_total

# print(resistance_parallel_total)

resistance_total = sum(resistance_series) + resistance_parallel_total
print(resistance_total)
