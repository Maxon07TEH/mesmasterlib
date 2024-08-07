from datetime import datetime

LOGfilepatch = ""
LOGcontent = ""
returning = True
def writelog(LOGfilepath, LOGcontent, returning):
    LOGfile = open(LOGfilepatch, 'a+')
    LOGfile.write(str(datetime.now()))
    LOGfile.write("\n")
    LOGfile.write(LOGcontent)
    LOGfile.close()
    if returning == 1 or True or "Yes" or "Y" or "YES" or "yes":
        return (str(datetime.now()))
        return "\n"
        return (LOGcontent)
    elif returning == 0 or False or "No" or "N" or "NO" or "no":
        return "log writed, not returned"
    else:
        return "\n"
