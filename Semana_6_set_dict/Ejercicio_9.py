from collections import Counter
items =[{'item': 'arroz', 'amount': 40}, {'item': 'fideos', 'amount': 30}, {'item': 'arroz', 'amount': 7}]
result = Counter()
for d in items:
    result[d['item']] += d['amount']
print(result)