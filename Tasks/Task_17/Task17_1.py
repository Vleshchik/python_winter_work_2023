import re
text = input() #10 2 7 1 95 70 70 43 49 78 61 53 85 69 4 2 1 776 645 46 722 572 470 703 891 0 100 39
print(re.findall(r'\b\d*[02468]\b', text))