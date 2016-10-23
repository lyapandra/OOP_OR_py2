def _01():
    import mymod
    print(dir(mymod))#[0])
    print mymod.var
    mymod.dothis()

def _02():
    from mymod import var, dothis
    print(dir(dothis))#[0])
    print var
    dothis()
_01()
_02()