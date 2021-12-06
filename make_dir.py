import os
import address
import shutil
import make_log

#@Notes : make weapon list with attachment index
#@Param : attachment count (sight , barrel , grip , stock ...)
#@Return: 2nd matrix
def make_weapon_list(sight_count , barrel_count , grip_count , stock_count , special_count) :

    result = []

    for sight in range(sight_count) :
        for barrel in range(barrel_count) :
            for grip in range(grip_count) :
                for stock in range(stock_count) :
                    for special in range(special_count) :
                        temp = [sight , barrel , grip , stock , special]
                        result.append(temp)

                        #record to log
                        make_log.write(str(temp))

    return result




#@Notes : make weapon name string
#@Param : weapon attachment index list
#@Return: name string
def make_name_stirng(i) :
    return str(i[0]) + "_" + str(i[1]) + "_" + str(i[2]) + "_" + str(i[3]) + "_" + str(i[4])




#@Notes : append weapon direction name in weapon list
#@Param : 2nd matrix
#@Return: 2nd matrix with string
def make_weapon_dir_name(weapon_list) :

    for i in weapon_list :
        temp = make_name_stirng(i)
        #print(temp)
        i.append(temp)
        #record to log
        make_log.write(temp)

    return weapon_list

#@Notes : make subdirection key list
#@Param : weapon list, file list
#@Return: list keys of sub direction names
def get_key_list( weapon_list , weapon , file_list) :
    return list(file_list[weapon_list.index(weapon)][0].keys());


#@Notes : delete all dir and files with check
#@Param : final_path = ./final/(weapon_name)
#@Return: None
def reset_dir(final_path) :
    if os.path.isdir(final_path) :
        shutil.rmtree(final_path)

#@Notes : make direction of copied sample in final
#@Param : weapon list
#@Return: None
def make_dir(weapon_list , final_path , file_list) :

    print(os.getcwd())

    #make weapon name dirction
    os.mkdir(final_path)
    #final_path = ./final/(weapon_name)
    #weapon[5] = ex) 1_1_1_1_1
    for weapon in weapon_list :

        os.mkdir(address.make_primary_mkdir_address( final_path , weapon[5] ))

        #make sub direction
        for sub_dir_name in get_key_list(weapon_list , weapon , file_list) :
            os.mkdir(address.make_sub_mkdir_address(final_path , weapon[5] , sub_dir_name ))


def main():

    make_weapon_dir_name( make_weapon_list(3,2,2,3,4) )

if __name__ == '__main__':
    main()