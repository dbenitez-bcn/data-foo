def isPrimo(num: int) -> bool:
    if num == 1:
        return True
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def run():
    print(isPrimo('qwerty'))

if __name__ == '__main__':
    run()