def primo(num):
    is_primo = True
    qnt_div = 0

    for i in range(1, num):
        if (num % i) == 0:
            qnt_div += 1

    if qnt_div > 1:
        is_primo = False

    return is_primo