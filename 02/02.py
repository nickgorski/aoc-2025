import sys


def IsInvalid(n):
    n = str(n)
    num_digits = len(n)

    # Must have an even number of digits.
    if num_digits % 2 != 0:
        return False

    # Return True if the first and second halves are equivalent.
    return n[:num_digits // 2] == n[num_digits // 2:]

def FindInvalidProductsInRange(a, b):
    invalid_products = []
    for i in range(a, b + 1):
        if IsInvalid(i):
            invalid_products.append(i)
    return invalid_products


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_file:
        line = input_file.readline().strip()
    product_ranges = line.split(',')

    invalid_id_sum = 0
    for r in product_ranges:
        a, b = [int(x) for x in r.split('-')]
        invalid_products = FindInvalidProductsInRange(a, b)
        print('Checking range', r, ':', invalid_products)
        invalid_id_sum += sum(invalid_products)

    print(invalid_id_sum)
