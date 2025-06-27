from string import digits, ascii_letters
for i in digits+ascii_letters:
    for j in digits+ascii_letters:
        for k in digits+ascii_letters:
            for l in digits+ascii_letters:
                print(i,j,k,l, sep='', end='\t')