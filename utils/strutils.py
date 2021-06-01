"""
字符串工具
"""
import re
from copy import deepcopy


def parse_name_equals_value_to_dict(s):
    """
    将NAME=VALUE格式字符串解析成dict{'name':NAME,'value':VALUE}
    """
    p = s.split('=')
    r = {'name': p[0].strip(), 'value': p[1].strip()}
    return r


def parse_name_equals_value_to_dict_map(s):
    """
    将NAME=VALUE格式字符串解析成dict{NAME:VALUE}
    :param s: str
    :return: dict
    """
    d = {}
    for e in s:
        p = e.split('=')
        d[p[0].strip()] = p[1].strip()
    return d


def parse_linux_conf_to_dict(file):
    """
    将linux conf文件解析成dict
    :param file: file path str
    :return: dict
    """
    try:
        linux_type_dict = dict()
        with open(file, 'r', encoding='utf-8') as f:
            linux_type_list = f.read().strip().split('\n')
    except IOError:
        pass
    else:
        if linux_type_list is not None:
            linux_type_list_to_purge = deepcopy(linux_type_list)
            # linux_type_list_to_purge = linux_type_list[:]  # another implement, sames to deepcopy
            for member in linux_type_list_to_purge:
                if re.search('^#+.*', member) is not None:
                    member_to_purge = member
                    linux_type_list.remove(member_to_purge)
            for member in linux_type_list:
                sub_member = member.split('=')
                linux_type_dict[sub_member[0]] = sub_member[1].strip('"')
            return linux_type_dict

