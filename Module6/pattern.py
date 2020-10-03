#!/usr/bin/env python3
import re
import operator
import csv

def error_message():
    error = {}
    # per_user = {}
    # # FOR 1st Condition
    with open('syslog.log') as file:
        for line in file:
            err = re.search(r"ticky: ERROR ([\w ]*) ", line)
            # result = re.search(r"ERROR|INFO ([\w ]*) ", line)
            # user = re.search(r"\(([\w]*)\)$", line)

            #print(result.group(0))
            if err is None:
                continue
            error[err.group(0)] = error.get(err.group(0), 0) + 1

            # if result is None:
            #     continue
            #
            # if result.group(0) == 'INFO':
            #     if user is None:
            #         continue
            #
            #     count = 1
            #     if user not in per_user:
            #         # print(user[1])
            #         # print(user[1], result.group(0))
            #         per_user[user[1]] = [result.group(0), count]
            #     count=count+1
            #     per_user[user[1]] = [result.group(0), count]
    file.close()
    # print(per_user)

    error_lst = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    # print(error_lst)

    # user_lst = sorted(per_user.items(), key=operator.itemgetter(0))
    # # print(user_lst)

    # Writing error_lst into error_message.csv file
    with open('error_message.csv', 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(error_lst)
    file.close()

    # # Writing user_lst into user_statistics.csv file
    # with open('user_statistics.csv', 'w') as file:
    #         writer = csv.writer(file, lineterminator='\n')
    #         writer.writerows(user_lst)
    # file.close()


def user_message():
    per_user = {}

    with open('syslog.log') as file:
        for line in file:
            line = line.strip()
            result = re.search(r"INFO ([\w ]*) ", line)
            user = re.search(r"\(([\w]*)\)$", line)
            # print(result[1])
            if result is None:
                continue

            count = 1
            if user is None:
                continue

            elif user[1] not in per_user:
                # print(user[1])
                # print(user[1], result[1])
                per_user[user[1]] = [result[1], count]
            count=count+1
            per_user[user[1]] = [result[1], count]
    file.close()
    print(per_user)

    user_lst = sorted(per_user.items(), key=operator.itemgetter(0))
    # print(user_lst)

    # Writing user_lst into user_statistics.csv file
    with open('user_statistics.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(user_lst)
    file.close()


error_message()
user_message()
