def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    list1 = s.split(" ")
    list1 = [x for x in list1 if x.strip ()]
    print(list1)
    str = ""
    for i in list1[::-1]:
        str += i
        str += " "

    print(str)
        


reverseWords("  hello world  ")