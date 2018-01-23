# Function Dennis converts a date into a formal date format
# Eg: Converts 24/08/1996 to 24th August 1996

def Dennis(adate):
    l0 = []
    l0 = adate.split('/')
    l = []
    l = [int(a) for i,a in enumerate(l0)]
    if l[0] % 10 == 1:
        new = str(l[0]) + "st "
    elif l[0] % 10 == 2:
        new = str(l[0]) + "nd "
    elif l[0] % 10 == 3:
        new = str(l[0]) + "rd "
    else:
        new = str(l[0]) + "th "
    d = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    new = new + d[l[1]]+" "
    new = new + str(l[2])
    return new

if __name__ == '__main__':
    x = raw_input("Enter a date : ")
    print Dennis(x)