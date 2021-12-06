#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     12-04-2020
# Copyright:   (c) User 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv

#@Note   : get last predicate number
#@Param  : predicate num file
#          name = weapon name string
#@Return : last predicate number + 1000
def get_last_predicate_num(file , name) :

    result = 0
    find = False
    number = 0

    line = csv.reader( file )

    for i in list(line) :

        if i[0] == name :
            result = int(i[1])
            find = True
            break;

        number = i[1]

    if find :
        pass
    else :
        write_predicate_num(file , name , number + 1)
        result = number

    return result

#@Note   : write last predicate number
#@Param  : file = predicate num file
#          name = weapon name string
#        : number = last predicate
#@Return : None
def write_predicate_num(file , name, number) :
    file.write(name + ',' + str(number) + '\n')
#address =  (weapon_name)/(attachment_index)/(folder_name)/(file)
def make_predicate(string , address) :
    return "\t\t{\"predicate\": {\"custom_model_data\":" + string + "}, \"model\": \"item/guns/" + address + "\"},\n"

def make_end_predicate(string , address) :
    return "\t\t{\"predicate\": {\"custom_model_data\":" + string + "}, \"model\": \"item/guns/" + address + "\"},\n"

def write_predicate(file, string , address ) :
    file.write( make_predicate(string, address) )


def write_end_predicate(file, string , address ) :
    file.write( make_end_predicate(string, address))

#@Note   : make CustomModelData number string
#@Param  : number = int value to change in string
#          digit = number digit to return
#@Return : CustomDataTag number string with 0 display
def itoa_with_zero(number ,digit) :
    result = ''

    for i in range(digit) :

        divisor = pow(10 , digit - i - 1)
        print(divisor)
        result += str( int(number / divisor) )

        number %= divisor

    return result



#@Note   : make CustomModelData number string
#@Param  : weapon = weapon_number
#          attachment = attachment number
#          pose = pose index
#          frame = frame index
#@Return : CustomDataTag number string with 0 display
def make_data_numstr( weapon , attachment , pose , frame) :

    result = ''

    if ( weapon >= 10 ) :
        result += itoa_with_zero(weapon , 2)
    else :
        result += itoa_with_zero(weapon , 1)

    result += itoa_with_zero(attachment , 2)
    result += itoa_with_zero(pose , 1)
    result += itoa_with_zero(frame , 2)

    return result


