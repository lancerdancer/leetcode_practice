import re

file = 'email_data.txt'
parttern = '\S+@\S+\.\S+'
first_email_and_date = '.*\s(\S+@\S+\.\S+).*\s(\d{4}/\d{2}/\d{2})\s(\d{2}:\d{2}:\d{2}).*\s'
test = 'sadfjio;32na89pfhdj yongxu.yao@gamil.com asdfioejasd asdfiohja@mst.edu frh 2019/12/29 12:06:08 asfaweasf'


# print(re.findall(parttern, test))
# result = re.match(first_email_and_date, test)
# print(result.groups())

# with open(file, mode='r') as f:
#     result = []
#     for line in f:
#         result += re.findall(parttern, line)
#
# print(result)

ip_str = 'asdfjie k asuiehawasdf192.168.1.18888 255.255.255.0'
ip_pattern = '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
             '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
             '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.' \
             '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])'
all_ip = re.findall(ip_pattern, ip_str)
print(all_ip)
