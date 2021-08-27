import gzip
import re

user_re = re.compile(r'^(.*) \S+ farnsworth .* session opened for user (\w+)')

with gzip.open("sshd.log.gz", mode='rt') as log_file:
    # seen = set()
    # for line in log_file:
    #     match = user_re.search(line)
    #     if match:
    #         day = (match.group(1), match.group(2))
    #         if day not in seen:
    #             print(day[0],day[1])
    #         seen.add(day)

    # matches = [user_re.search(line) for line in log_file]
    # days = []
    # for match in matches:
    #     if match:
    #         day = (match.group(1), match.group(2))
    #         days.append(day)
    #         if day not in seen:
    #             print(day[0], day[1])
    #         seen.add(day)

    # find all matches in the file
    matches = (
        user_re.search(line)
        for line in log_file
    )

    # find all days when the user logged in
    days = (
        (match.group(1), match.group(2))
        for match in matches
        if match
    )

    # printout days uniquely
    seen = set()
    for day in days:
        if day not in seen:
            print(day[0], day[1])
        seen.add(day)
