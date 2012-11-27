import glob, os, datetime, fileinput, sys


#############################################################################
###                      Helper Functions                                 ###
#############################################################################
# archive all files fitting a glob
# if preserve is set to "n" destroy the original. 
def arch_globed_files(glb, preserve):
    now = datetime.datetime.now()
    #create the archive destination if it does not yet exist.
    try:    
        os.makedirs("/etc/configuration_file_archive")
    #ignore exception thrown if directory exists
    except :        
        pass
        
    filelist=glob.glob(glb)
    for file in filelist:
        new_location = "/etc/configuration_file_archive/"+os.path.basename(file)+"_"+now.strftime("%Y-%m-%d-%I%M%S%p")        
        if preserve == "n":
            print "archiving -> ", file," to ->", new_location 
            os.system("mv "+file+" "+new_location)
        else:
            print "backing up -> ", file," to ->", new_location 
            os.system("cp "+file+" "+new_location)


#replace all lines containing the phrase searchExp with the complete new line specified in replaceExp.
#Delete the line if replaceExp is blank 
def replace_any_line_containing_word(file,search_exp,replace_exp):
    for line in fileinput.input(file, inplace=1):
        if search_exp in line:            
            if replace_exp:                #we don't even want a blank line if null 
                print replace_exp
        else :
             sys.stdout.write(line)

#wrapper function to delete line containing subtraction in it
def remove_from_file(file, search_exp):
    replace_any_line_containing_word(file,search_exp,"")

#make sure to remove any old occurrences of line and add it to end of file. 
def add_to_file(file, replace_exp):
    remove_from_file(file, replace_exp)
    file_handle = open(file, "a")
    try:
        file_handle.write(replace_exp+"\n")
    finally:
        file_handle.close()    

# add a parameter to a file making sure any old occurrences of the parameter are replaced. 
def add_unique_entry_to_file(file,search_exp,replace_exp):
    remove_from_file(file, search_exp)
    add_to_file(file,replace_exp)

# replace only the characters specified in serach_exp in all places in a file
def replace_all_occurances_of_a_phrase(file,search_exp,replace_exp):    
    for line in fileinput.input(file, inplace=1):
        line = line.replace(search_exp,replace_exp)        
        sys.stdout.write(line)    # using write instead of print, squelches carriage returns

#deploy specified config file from the proper profile to specified location
#first make sure if there is a file there it gets archived
def deploy_config_file(profile, file_name, new_location, repository_path):
    arch_globed_files(new_location+"/"+file_name, "y")
    os.system("curl -o "+new_location+"/"+file_name+" "+repository_path+profile+"/"+file_name)
    