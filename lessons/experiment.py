

def foo(a: list[int], b: list[int]) -> None:
    i: int = 0
    while i< len(a):
        a[i] = b[i] + 2
        b.append(a[i])
        i += 1
    b = a
    print(b)

def main() -> None:
    a: list[int] = [0,1,2]
    b: list[int] = [3, 4, 1]
    foo(a, b)
    print(a)
    print(b)


if __name__ == '__main__':
    main()

