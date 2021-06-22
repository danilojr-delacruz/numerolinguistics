a = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
     'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
     'seventeen', 'eighteen', 'nineteen']
    
b = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
     'ninety']


from analysis import length


def english_number(n):
    """Return the english word for the number n."""
    num = ''
    if n==0:
        return 'zero'
    elif n < 0:
        return 'negative ' + english_number(-n)
    else:
        if n >= 1000:
            num += english_number(n//1000) + ' thousand'
            # if 0 < n % 1000 < 100:
            #     num += ' and'
            n = n % 1000
        if n >= 100:
            num += ' ' + a[(n // 100)] + ' hundred'

            # if n % 100 != 0:
            #     num += ' and'
        
        if n%100 < 20:
            num += ' ' + a[n%100]
        else:
            num += ' ' + b[(n%100)//10] + ' ' + a[n%10]
        
        return num.strip()

# Average letters per digit

total_letters = 0
total_digits = 0
for i in range(1, 1000000):
    total_letters += length(english_number(i))
    total_digits += len(str(i))

print(total_letters / total_digits)

# Number of letters in multiples of powers of 10.

num_list = [(10**i) * j for i in range(0, 6) for j in range(1, 10)]

for num in num_list:
    print(f"{num}: {length(english_number(num))}")