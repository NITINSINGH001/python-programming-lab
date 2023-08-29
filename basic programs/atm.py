# Q. 11 ATM
# input section
amount = int(input('Enter the amount '))
amount = amount - 100


# logic section
twok = amount // 2000
amount = amount - twok * 2000

fiveh = amount // 500
amount = amount - fiveh * 500

oneh = amount // 100

# display section
print('Number of Two Thousand Notes', twok)
print('Number of Five Hundred Notes', fiveh)
print('Number of One Hundred Notes', oneh+1)
