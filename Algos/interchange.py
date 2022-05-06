def printMove(start: str, end: str):
    print("Move from", start, "to", end)

def interchange(num: int, start: str, spare: str, end: str):
    if num == 1:
        printMove(start, end)
    else:
        interchange(num - 1, start, end, spare)
        interchange(1, start, spare, end)
        interchange(num - 1, spare, start, end)


interchange(3, "start", "spare", "end")