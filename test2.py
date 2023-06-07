

def test(**options):
    qwe = options.get("selected")
    qqq = options.get("ww")
    print qwe, qqq


test(selected="sss", ww = 789)