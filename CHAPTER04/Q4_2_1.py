def number_to_day(num=0):
    """

    戻り値
    昨日(numが-1の場合)
    今日(numが0の場合)
    明日(numが1の場合)
    今日より1日を超えて離れた日(numが上記以外の場合)
    """
    if num == 0:
        day = "今日"
    elif num == 1:
        day = "明日"
    elif num == -1:
        day = "昨日"
    else:
        day = "今日より1日を超えて離れた日"
    return day
