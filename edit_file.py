import CONSTANT

sample = ''
attach = ''

#@Note   : copy source file to dest until get end_str
#@Param  : source = source file
#        : dest = destination file
#        : end_str = string of denote end
#        : mode = 1 means don't write end_str to dest
#                 1 means write end_str to dest
#@Return : None
def copy_file(source , dest , end_str , mode) :
    temp = ''
    while( True ) :
        #get source string
        temp = source.readline()

        if "__comment" in temp :
            continue

        #exit condition
        if (temp == '' or temp == end_str ) and mode == 0:
            return
        elif temp == end_str and mode == 1 :
            dest.write(temp)
            return
        #write to dest
        dest.write(temp)

#@Note   : move cursor in attachment file
#@Param  : attachment file
#@Return : If file is blank text file return 1, else 0
def set_init_attach_file ( attach_file ) :
    print(attach_file)
    while(True) :
        temp = attach_file.readline()
        #check blank text
        #stop if "\t\"elements\": [\n"
        if  temp == CONSTANT.FILE_ELEMENT_STRING :
            print('found')
            return 0
        elif temp == 'BLANK\n' :
            print('found')
            return 1


def main() :

    f = open("./sample/fires/attachment/sight/0.json" ,'r')
    set_init_attach_file(f)
if __name__ == '__main__':
    main()



