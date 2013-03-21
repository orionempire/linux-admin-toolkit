import glob, os, datetime, fileinput, sys, socket, re, shutil

base_archive_directory = "never_set"
default_file_owner = "never_set"

###############################################################################
###                    Configuration File Edit Functions                        ###
###############################################################################
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

###############################################################################
###                            Utility Functions                                ###
###############################################################################

def deploy_files(file_list,source_dir,dest_dir,archive) :
    if (archive == "y" or archive == "Y") :
        arch_globed_files(destination,"n")
    
    #create the destination if it does not yet exist.
    try:    
        os.makedirs(dest_dir)
    #ignore exception thrown if directory exists
    except :        
        pass
    
    #first check for a glob passed as a string 
    #then if any other string is passed suppress it from breaking into letters by making it a single list item
    if( file_list == "*" ) :    
        file_list = os.listdir(base_archive_directory+source_dir)
    elif( type(file_list) == type( str())) :        
        file_list = [''.join(file_list)]
        
    for item in file_list :
        print "Deploying -> "+base_archive_directory+source_dir+item+" | To -> "+dest_dir+item        
        shutil.copyfile(base_archive_directory+source_dir+item,dest_dir+item)
        os.system("chown "+default_file_owner+" "+dest_dir+item)
        os.system("chmod g+rw "+dest_dir+item)
    pass    

#Return the systems ip address unless it is localhost then throw error
def get_system_ip_address():
    ip_address = socket.gethostbyname(socket.gethostname()) 
    
    if (re.search('^127.',ip_address)) :
        raise LocalHostFound("ERROR - Official ip address is localhost")
    else :
        return ip_address

def log_item(the_level, the_item) :
    print the_level+" - "+the_item