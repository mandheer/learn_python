# groups = []
# with open("widgets.txt") as widget_file:
#     for line in widget_file:
#         if line.startswith('WIDGET'):
#             groups.append("")
#         groups[-1] += line
# print(groups[:4])


# import re
# groups = []
# with open("widgets.txt") as widget_file:
#     for line in widget_file:
#         if line.startswith('WIDGET'):
#             group = {}
#             groups.append(group)
#         else:
#             key, value = re.split(r'\s*=\s*', line, 2)
#             group[key] = value
# print(groups[2]['name'])
# print(groups[:2])

import re


def get_widget_groups(widget_file):
    keys = (
        re.split(r'\s*=\s*', line, 2)
        for line in widget_file
        if not line.startswith('WIDGET')
    )

    for k, v in keys:
        g = {k: v}
        for i in range(1, 4):
            k, v = next(keys)
            g[k] = v
        yield g

    # c = count(1)
    # for k, v in keys:
    #     if next(c) % 4 != 0:
    #         group[k] = v
    #     else:
    #         yield group

    # groups = []
    # for line in widget_file:
    #     if line.startswith('WIDGET'):
    #         group = {}
    #         groups.append(group)
    #     else:
    #         key, value = re.split(r'\s*=\s*', line, 2)
    #         group[key] = value
    #     if next(c) % 5 == 0:
    #         yield group


with open('widgets.txt', mode='rt') as widget_file:
    for group in get_widget_groups(widget_file):
        print(group['name'])
