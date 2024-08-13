import re
import sys

def ip2num(ip):
    if re.match(r"((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}", ip):
        return sum([int(octet) * (256 ** (3 - index)) for index, octet in enumerate(ip.split("."))])
    return None

def num2ip(num):
    if isinstance(num, int):
        return f"{num // 16777216 % 256}.{num % 16777216 // 65536}.{num % 65536 // 256}.{num % 256}"
    return None

def range2cidr(rng):
    cidr = list()
    try:
        first, last = [ip2num(i) + 0 for i in rng.split("-")]
    except:
        return None
    subnet = [2 ** (32 - i) for i in range(33)]
    while first <= last:
        mask = 32
        while mask >= 0:
            if (first % subnet[mask]) or (last - first + 1 < subnet[mask]):
                break
            mask -= 1
        mask += 1
        cidr.append(f"{num2ip(first)}/{mask}")
        first += subnet[mask]
    return cidr

if __name__ == "__main__":
    for line in sys.stdin:
        cidr = range2cidr(line.strip())
        if cidr:
            print("\n".join(cidr))
