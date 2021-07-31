def remove1(x):
    return list(dict.fromkeys(x))

with open(input("Input File: "), "r") as f:
    proxies = f.read().splitlines()

out = input("Output File: ")

try:
    open(out, "x").close()
except:
    pass

with open(out, "w") as f:
    proxies = remove1(proxies)
    for x in proxies:
        f.write(f"{x}\n")
