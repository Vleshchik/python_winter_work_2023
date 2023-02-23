import re
n = int(input()) #45
text = input() #10 2 7 1 95 70 70 43 49 78 61 53 85 69 4 2 1 776 645 46 722 572 470 703 891 0 100
print(re.findall(fr'\b[0-{n//10}][0-{n%10}]\b|\b[0-9]\b', text))