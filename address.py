sample_path = "./sample/"
final_path = "./final/"

#  ======>   FILE OUTPUT SECTION

#@Notes : make file direction to open ( in final )
#@Param : final_path = "./final/(weapon_name)"
#         index      = weapon[i][5] (attachment_num) ex) "1_1_1_1_1"
#         folder     = element in file[i][0].keys()
#         name       = file[i][0][folder][j]
#@Return: string ./final/(weapon_name)/index/folder/name
def make_final_file_string( final_path , attach_index , folder , name ) :
    return final_path + "/" + attach_index + "/" + folder + "/" + name

#@Notes : make file direction to open ( in sample )
#@Param : sample_path = "./sample/(weapon_name)"
#         folder     = element in file[i][0].keys()
#         name       = file[i][0][folder][j]
#@Return: string ./sample/(weapon_name)/folder/name
def make_sample_file_string( sample_path , folder , name ) :
    return sample_path +  "/" + folder + "/" + name

#@Notes : make file direction to open ( in attachment )
#@Param : sample_path = "./sample/(weapon_name)"
#         folder     = element in file[i][0].keys()
#         name       = file[i][0][folder][j]
#@Return: string ./sample/(weapon_name)/attachment/attach_string/num.json
def make_attachment_file_string( sample_path , folder , attach_string , num ) :
    return sample_path +  "/" + "attachment" + "/" + attach_string + "/" + num + ".json"
#=========================================================================================
#=========================================================================================

#   MAKE INITIAL SETTING SECTION

#@Notes : address for checklist to input
#@Param : sample_path = "./sample/(weapon_name)"
#@Return: string ./sample/(weapon_name)/checklist.csv
def input_checklist_address( sample_path ) :
    return sample_path + "/" + "checklist.csv"


#@Notes : address for make primary folder
#@Param : final_path = "./final/(weapon_name)"
#       : attach_index = weapon[i][5]
#@Return: string ./sample/(weapon_name)/attach_index
def make_primary_mkdir_address( final_path , attach_index ) :
    return final_path + "/" + attach_index


#@Notes : address for make sub folder
#@Param : final_path = "./final/(weapon_name)"
#       : attach_index = weapon[i][5]
#         sub_dir_name = list(dict.keys())[i] of file_list
#@Return: string ./sample/(weapon_name)/attach_index/(sub_dir_name)
def make_sub_mkdir_address( final_path , attach_index , sub_dir_name) :
    return final_path + "/" + attach_index + "/" + sub_dir_name

#=========================================================================================
#=========================================================================================

#   MAKE PREDICATE SECTION

#@Notes : address for predicate to output
#@Param : sample_path = "./final/(weapon_name)"
#@Return: string ./sample/(weapon_name)/predicate.json
def make_predicate_string( final_path ) :
    return final_path + "/" + "predicate.json"