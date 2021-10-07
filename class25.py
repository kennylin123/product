product = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name, price = line.strip().split(',')
        product.append([name, price])
print(product)

