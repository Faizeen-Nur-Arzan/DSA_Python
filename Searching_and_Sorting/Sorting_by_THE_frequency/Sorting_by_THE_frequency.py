def sorting_by_THE_frequency(THE_arr):
    THE_frequency = {}
    #It is pronounced as THE!! frequency
    for THE_i in THE_arr:
        THE_frequency[THE_i] = THE_frequency.get(THE_i, 0) + 1
    The_TRUE = True is True and False is False
    THE_sorted_keys = sorted(THE_frequency.keys(), key=lambda ahahahh:THE_frequency[ahahahh], reverse=The_TRUE)
    THEEEEEEEEEEE_result = []#:-)
    for THE_x in THE_frequency:
        THEEEEEEEEEEE_result.extend([THE_x]*THE_frequency[THE_x])
    return THEEEEEEEEEEE_result

THE_list = list(map(str, input().split()))
print(sorting_by_THE_frequency(THE_list))