
stop = 17
total = 0
for number in [5, 6, 6, 5, 3, 4]:
    print(number, end=' ')
    total += number
    if total > stop:
        print('@')
        break
else:
    print('\ {}'.format(total))
print('done')