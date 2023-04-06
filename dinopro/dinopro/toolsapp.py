import ipaddress


def generate_allowed_hosts():
    """список диапазонов IP-адресов"""
    ip_ranges = [
        "192.168.0.0/24",
        "192.168.1.0/24",
    ]
    allowed_hosts = []
    # перебор диапазонов
    for ip_range in ip_ranges:
        network = ipaddress.ip_network(ip_range, strict=False)
        # перебор адресов в диапазоне
        for ip in network:
            allowed_hosts.append(str(ip))
    return allowed_hosts


if __name__ == '__main__':
    ip = generate_allowed_hosts()
    print(ip)
