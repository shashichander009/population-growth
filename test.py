india_data = {'india': 33, 'Pakistan': 332}

print(india_data.items())


lists = india_data.items()

print(lists)

print(*lists)


print(zip(*lists))


x, y = zip(*lists)

print(x)
print(y)
