# print statements aren't necessary, but they help see what the script is doing when it runs
# print is helpful for 'wtf?' moments
print("Python: Combining NML files")

 # this module is a good way to handle working with files that might contain unicode (e.g. translations) 
import codecs

sections = [] # create an empty list, we'll put strings in here then join them later

# get the header file and append to a list
header = codecs.open("src/header.nml",'r','utf8')
sections.append(header.read())
header.close()

sprite_templates = codecs.open("src/sprite_templates.nml",'r','utf8')
sections.append(sprite_templates.read())
sprite_templates.close()

neoplan_an440 = codecs.open("src/neoplan_an440.nml",'r','utf8')
sections.append(neoplan_an440.read())
neoplan_an440.close()

flyer_e800 = codecs.open("src/flyer_e800.nml",'r','utf8')
sections.append(flyer_e800.read())
flyer_e800.close()

print("Python: Writing combined NML file")

# create a new file on disk, which will have a name and be writable
processed_nml_file = codecs.open('nmlc/2cc_trolleybuses.nml','w','utf8')

# write stuff into the file
processed_nml_file.write('\n'.join(sections)) # join the list of templated stuff with newlines, and write to a file
processed_nml_file.close() # we're done with this file now, finish with it
