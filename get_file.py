import csv
import os
import glob
import CONSTANT
import make_dir
import address
import make_log


#Note   : get check list
#Param  : csv path(string)
#Return : list of check list
def get_check_list(path) :

    result = [ [] , [] , [] , [] , [] , {}]
    csv_file = open(path , 'r')
    csv_list = list(csv.reader(csv_file))

    # -1 means no special attachment model situation
    if csv_list[0][0] != "COMMON" :
        return [None]

    for line in csv_list :

        if line[0] == "COMMON" :
            result[CONSTANT.COMMON] = {"COMMON": line[1:]}
        elif line[0] == "SIGHT" :
            result[CONSTANT.SIGHT].append({int(line[1]):line[2:]})
        elif line[0] == "BARREL" :
            result[CONSTANT.BARREL].append({int(line[1]):line[2:]})
        elif line[0] == "GRIP" :
            result[CONSTANT.GRIP].append({int(line[1]):line[2:]})
        elif line[0] == "STOCK" :
            result[CONSTANT.STOCK].append({int(line[1]):line[2:]})
        elif line[0] == "SPECIAL" :
            result[CONSTANT.SPECIAL].append({int(line[1]):line[2:]})

    csv_file.close()

    for i in range(0,5) :
        for d in result[i] :
            while '' in d[list(d.keys())[0]] :
                d[list(d.keys())[0]].remove('')

    make_log.write_list(result)
    return result

#Note   : get direction list
#Param  : path(string)
#Return : list of direction
def get_dir(path) :

    dir_list = []
    result = []
    dir_list = os.listdir(path)

    for i in dir_list :
        print(i)
        if '.' in i :
            pass
        else :
            result.append(i)


    return result

#Note   : get file list
#Param  : path(string)
#Return : list of file
def get_file(path) :

    file_list = []
    result = []
    file_list = os.listdir(path)

    for i in file_list :
        #print(i)
        if '.' in i :
            result.append(i)



    return result

def make_file_list(check_list , weapon ,sample_path) :

    result = []


    for i in weapon :
        #this array is point out ex) 1_1_1_1_1
        result.append([{}])

        for index in range(CONSTANT.SIGHT ,CONSTANT.SPECIAL + 1) :
            #get dir_list in check list
            for check in check_list[index] :

                if i[index] in check :
                    for value in check[i[index]] :
                        result[-1][0][value] = []

        #append common check_list
        for value in check_list[CONSTANT.COMMON]["COMMON"] :
            result[-1][0][value] = []


        #get file_list in sub_dir
        for value in result :
            for d in value[0].keys() :
                value[0][d] = get_file( sample_path  + "\\" + d)


    return result



def main():

    #print("dir_list_py: {}".format(get_dir(sample_path + "fires")))
    #print("file_list_py: {}".format(get_file(sample_path + "fires")))
    weapon = make_dir.make_weapon_list(2,2,2,2,2)
    weapon = make_dir.make_weapon_dir_name(weapon)
    check_list = get_check_list("test.csv")
    print(check_list)
    index = 0



if __name__ == '__main__':
    main()
