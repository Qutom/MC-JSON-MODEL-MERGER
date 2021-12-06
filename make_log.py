log = open('log.log' , 'w')



def write(string) :
    log.write(string + "\n")

def write_section(section_string) :
    write("===========================")
    write("  " + section_string.upper())
    write("===========================")

def write_list(l) :
    for i in l :
        write(str(i))
