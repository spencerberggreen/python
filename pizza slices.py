requests = {'joe': {'cheese': 4}, 'anna': {'supreme': 2},
            'steve': {'supreme': 6}, 'jamie': {'cheese': 3}}


def total(guest, item):
    pizza_request = 0
    for k, v in guest.items():
        pizza_request = pizza_request + v.get(item, 0)
    return pizza_request


print(str(total(requests, 'cheese')), 'cheese slices')
print(str(total(requests, 'supreme')), 'supreme slices')
