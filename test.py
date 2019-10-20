import string as _string

def letterCheck(str):
    allowed = _string.letters + _string.digits + "_" + "-"
    for ch in str:
        if not ch in allowed:
            return 0
    else:
        return 1

if not letterCheck("python_fu_create_spritesheetvisible"):
    print "procedure name contains illegal characters"
else:
    print "ok"