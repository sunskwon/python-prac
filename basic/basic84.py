str_input = input().split()

try:
    h = int(str_input[0])
    b = int(str_input[1])
    c = int(str_input[2])
    s = int(str_input[3])

    bit = h * b * c * s
    mb = bit / (1024**2)

    print(f"{mb:.1f}MB")
except Exception as e:
    print(e)
