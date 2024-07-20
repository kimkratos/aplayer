import re
from collections import Counter

# 读取 access.log 文件
with open('access.log', 'r') as file:
    log_data = file.read()

# 查找所有 'Access from' 后面的 IP 地址
ips = re.findall(r'Access from ([\d\.]+)', log_data)

# 中国 IP 段列表 (这是一个简化的列表，实际情况可能需要更全面的列表)
china_ip_blocks = [
    re.compile(r'^1\.'), re.compile(r'^14\.'), re.compile(r'^27\.'), re.compile(r'^36\.'), re.compile(r'^39\.'),
    re.compile(r'^42\.'), re.compile(r'^49\.'), re.compile(r'^58\.'), re.compile(r'^59\.'), re.compile(r'^60\.'),
    re.compile(r'^61\.'), re.compile(r'^101\.'), re.compile(r'^103\.'), re.compile(r'^106\.'), re.compile(r'^110\.'),
    re.compile(r'^111\.'), re.compile(r'^112\.'), re.compile(r'^113\.'), re.compile(r'^114\.'), re.compile(r'^115\.'),
    re.compile(r'^116\.'), re.compile(r'^117\.'), re.compile(r'^118\.'), re.compile(r'^119\.'), re.compile(r'^120\.'),
    re.compile(r'^121\.'), re.compile(r'^122\.'), re.compile(r'^123\.'), re.compile(r'^124\.'), re.compile(r'^125\.'),
    re.compile(r'^126\.'), re.compile(r'^127\.'), re.compile(r'^139\.'), re.compile(r'^140\.'), re.compile(r'^144\.'),
    re.compile(r'^163\.'), re.compile(r'^171\.'), re.compile(r'^175\.'), re.compile(r'^180\.'), re.compile(r'^182\.'),
    re.compile(r'^183\.'), re.compile(r'^202\.'), re.compile(r'^203\.'), re.compile(r'^210\.'), re.compile(r'^211\.'),
    re.compile(r'^218\.'), re.compile(r'^219\.'), re.compile(r'^220\.'), re.compile(r'^221\.'), re.compile(r'^222\.'),
    re.compile(r'^223\.'), re.compile(r'^240\.'), re.compile(r'^211\.'), re.compile(r'^218\.'), re.compile(r'^219\.'),
    re.compile(r'^220\.'), re.compile(r'^221\.'), re.compile(r'^222\.'), re.compile(r'^223\.'), re.compile(r'^240\.'),
]

# 过滤出中国的 IP 地址
china_ips = [ip for ip in ips if any(block.match(ip) for block in china_ip_blocks)]

# 统计每个 IP 的出现次数
ip_counts = Counter(china_ips)

# 按出现次数降序排序
sorted_ip_counts = ip_counts.most_common()

# 输出结果
print("IP Address\tOccurrences")
for ip, count in sorted_ip_counts:
    print(f"{ip}\t{count}")
