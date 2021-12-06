from tkinter import *
import CONSTANT
import get_file
import make_dir
import address
import make_log
import edit_file
import predicate

#attachment count ( 'SIGHT' , 'BARREL' , 'GRIP' , 'STOCK' , 'SPECIAL' )
ATTACHMENT = []
#weapon list
weapon_list = []

#specfic attachment model
check_list = [[] , [] , [] , [] , [] , {}]
# file list
#ex ) [ [{"0_normal" : [file1 , file2...]} , {} , ... , {} ,{"file" : [file1 , file2 ..]}] <= this array is point out like fires/1_1_0_1_2 folder , [] ... ]
file_list = []
#weapon_name
name = ''

#@Notes : get weapon info
#@Param : None
#@Return: None
def input_info( entry_name ,entry_sight , entry_barrel , entry_grip , entry_stock , entry_special , window) :
    global name
    name = str(entry_name.get())
    ATTACHMENT.append(int(entry_sight.get()))
    ATTACHMENT.append(int(entry_barrel.get()))
    ATTACHMENT.append(int(entry_grip.get()))
    ATTACHMENT.append(int(entry_stock.get()))
    ATTACHMENT.append(int(entry_special.get()))
    window.destroy()


def main():
#==================================================================================
#=====================  INPUT GUI CODE ============================================
#==================================================================================

    window = Tk()
    input_frame = Frame()

    entry_name = Entry(input_frame)
    entry_sight = Entry(input_frame)
    entry_barrel = Entry(input_frame)
    entry_grip = Entry(input_frame)
    entry_stock = Entry(input_frame)
    entry_special = Entry(input_frame)


    label_name = Label(input_frame , text = "무기 이름", width = 20)
    label_sight = Label(input_frame , text = "sight 개수", width = 20)
    label_barrel = Label(input_frame , text = "barrel 개수", width = 20)
    label_grip = Label(input_frame , text = "grip 개수", width = 20)
    label_stock = Label(input_frame , text = "stock 개수", width = 20)
    label_special = Label(input_frame , text = "special 개수", width = 20)

    button = Button(input_frame , text = "확인" , command=lambda:input_info(entry_name ,entry_sight , entry_barrel , entry_grip , entry_stock , entry_special , window))

    label_name.grid(row = 0 , column = 0) , entry_name.grid(row = 0 , column = 1)
    label_sight.grid(row = 1 , column = 0) , entry_sight.grid(row = 1 , column = 1)
    label_barrel.grid(row = 2 , column = 0) , entry_barrel.grid(row = 2 , column = 1)
    label_grip.grid(row = 3 , column = 0) , entry_grip.grid(row = 3 , column = 1)
    label_stock.grid(row = 4 , column = 0) , entry_stock.grid(row = 4 , column = 1)
    label_special.grid(row = 5 , column = 0) , entry_special.grid(row = 5 , column = 1)
    button.grid(row = 6)

    input_frame.pack()
    window.mainloop()

#==================================================================================
#=====================  Get File List Code ========================================
#==================================================================================

    make_log.write_section("initialing")

    address.sample_path += name
    address.final_path += name

    #make weapon list
    make_log.write_section("weapon_list")
    weapon_list = make_dir.make_weapon_list(ATTACHMENT[CONSTANT.SIGHT], ATTACHMENT[CONSTANT.BARREL], ATTACHMENT[CONSTANT.GRIP], ATTACHMENT[CONSTANT.STOCK], ATTACHMENT[CONSTANT.SPECIAL])

    #make direction list
    make_log.write_section("weapon_list_with_name")
    weapon_list = make_dir.make_weapon_dir_name(weapon_list)

    #get check list
    make_log.write_section("check_list")
    check_list = get_file.get_check_list( address.input_checklist_address( address.sample_path ))
    #make file list
    make_log.write_section("file_list")
    file_list = get_file.make_file_list(check_list , weapon_list , address.sample_path)

    #reset direction
    make_dir.reset_dir(address.final_path)
    #make direciton
    make_dir.make_dir(weapon_list , address.final_path , file_list)

#==================================================================================
#=====================  Edit File Code ============================================
#==================================================================================

    #open global predicate file
    predicate_num_file = open( 'predicate_num.csv' , 'a' , newline='' )
    predicate_file = open( address.make_predicate_string(address.final_path) , 'w' )
    predicate_num_read = open( 'predicate_num.csv' , 'r')
    #get last predicate number
    predicate_num = predicate.get_last_predicate_num(predicate_num_read , name)
    predicate_num_read.close()

    attachment_num = 0
    #start open file loop
    for weapon in weapon_list :
        pose_num = 0
        for folder_name in make_dir.get_key_list(weapon_list , weapon , file_list) :

            frame_num = 0
            for file_name in file_list[weapon_list.index(weapon)][0][folder_name] :

                #open sample file
                make_log.write( "Sample : "  + address.make_sample_file_string(address.sample_path , folder_name , file_name ) )
                sample_file = open( address.make_sample_file_string(address.sample_path , folder_name , file_name ), 'r' )
                #open local predicate file

                #open final file
                make_log.write( "Final : "  + address.make_final_file_string(address.final_path , weapon[5] , folder_name , file_name ) )
                final_file = open( address.make_final_file_string(address.final_path , weapon[5] , folder_name , file_name ), 'w' )

                #write first text
                edit_file.copy_file(sample_file , final_file , CONSTANT.FILE_ELEMENT_STRING , 1)

                #open attachment file
                for attach_index in range(CONSTANT.SIGHT , CONSTANT.SPECIAL + 1) :

                    make_log.write( "Attachment (" + CONSTANT.DIR_STRING[attach_index] + ") :"  + address.make_attachment_file_string(address.sample_path , folder_name , CONSTANT.DIR_STRING[attach_index] , str(weapon[attach_index]) ) )
                    attach_file = open( address.make_attachment_file_string(address.sample_path , folder_name , CONSTANT.DIR_STRING[attach_index] , str(weapon[attach_index]) ) , 'r' )

                    #concentrate file
                    is_blank = edit_file.set_init_attach_file(attach_file)

                    edit_file.copy_file(attach_file , final_file , CONSTANT.FILE_END_STRING , 0)

                    #if attach_file is not blank text file write , to final_file
                    if is_blank == 0 :
                        final_file.write('\t\t,\n')

                    #attach_file.close()
                    attach_file.close()

                #write rest of text in sample_file
                edit_file.copy_file(sample_file , final_file , "" , 0)
                #close sample file
                sample_file.close()

                #write predicate
                #file_address = (weapon_name)/(attchment_index)/(folder_name)/
                predicate_line = name + '/' + weapon[5] + '/' + folder_name + '/' + file_name.replace('.json' , '')
                predicate_str = predicate.make_data_numstr(predicate_num , attachment_num , pose_num , frame_num )
                frame_num += 1

                if weapon == weapon_list[-1] and folder_name == make_dir.get_key_list(weapon_list , weapon , file_list)[-1] and file_name == file_list[weapon_list.index(weapon)][0][folder_name][-1] :
                    predicate.write_predicate(predicate_file , predicate_str , predicate_line)
                else :
                    predicate.write_end_predicate(predicate_file , predicate_str , predicate_line)

                #close final file
                final_file.close()

                make_log.write("\n")

            pose_num += 1

        attachment_num += 1

    #write predicate number
    #predicate.write_predicate_num(predicate_num_file , name , predicate_num)
    make_log.log.close()
    predicate_file.close()
    print("DONE")

if __name__ == '__main__':
    main()
