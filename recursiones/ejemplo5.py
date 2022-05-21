def suma (x):
    if x == 0:
        return 0
    else:
        return x + suma(x-1)

def main():
    suma(3)

main() 