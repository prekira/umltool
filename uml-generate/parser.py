#STEPS:
#open file
#parse
#conv to string
#call api


#Command to call plantuml api and convert text to uml diagram  as .png
#python3 -m plantuml umldiagram.txt

import json

#load dto data from json
file_ver = '2'
dto_json_path = 'DtoMap' + file_ver + '.json'
dto_data = {}

with open(dto_json_path) as json_file:  
    dto_data = json.load(json_file)
json_file.close()

#ignore built in classes
class_to_ignore = ['Dto', 'String', 'Boolean']
stereotypes = ['Audited', 'interface', 'enumeration']
enum_list = []

#get list of properties
def get_properties(dto_obj):
    class_properties_formatted = '\n{\n'
    connections = ''
    for i in dto_obj['properties']:
        class_properties_formatted += '    +'

        #type of field
        class_properties_formatted += get_class_name(i['type'])
        
        #name of field
        class_properties_formatted += ' ' + i['name'] + ': ' 
        
        #TODO: shorten
        #if field has optional annotation
        isRequired = True
        if 'notRequired' in i['annotations'] and i['annotations']['notRequired'] == 'true':
            class_properties_formatted += '(Optional)'
            isRequired = False
        class_properties_formatted += '\n'
        
        #if enums:
        if 'value' in i['dtoEnums']:
            enum_list.append(i['dtoEnums'])

        #if connection (external ref)
        #TODO: make case insensitive 
        cardinality = '1'
        '''
        if you have an external ref that is an array
                it is 0..* (meaning none or many)
        if it is just a ref id that is not an array it is 1
        unless it is @NotRequired, then it is 0..1
        '''
        #cardinality:
        if "swaggerReference" in i['annotations'] or "SwaggerReference" in i['annotations']:
            if 'isList' in i['annotations'] and i['annotations']['isList'] == 'true':
                cardinality = '0..*'
            else:
                if isRequired:
                    cardinality = '1'
                else:
                    cardinality = '0..1'

        #cardinality: in annotations: isList, notRequired = true
        if "swaggerReference" in i['annotations']:
            connections += '\n' + get_class_name(i['annotations']['swaggerReference']) + ' -o ' + dto_obj['className'] + ': ' +  i['name'] + '      ' + cardinality + '\n' 
        if "SwaggerReference" in i['annotations']:
            connections += '\n' + get_class_name(i['annotations']['SwaggerReference']) + ' -o ' + dto_obj['className'] + ': ' +  i['name'] + '      ' + cardinality + '\n'

        #embedded class
        if isDto(i['dtoClassName']):
            #inner class -> outerclass : inner class
            connections += '\n' + get_class_name(i['dtoClassName']) + ' -* ' + dto_obj['className'] + ' : + ' + get_class_name(i['dtoClassName']) + ' (inner class) '
        
    class_properties_formatted += '}' + connections
    return class_properties_formatted
    pass

#extract class name from string of package directory:
def get_class_name(name):
    return name[name.rfind('.') + 1 :]

#find if dto from type name
def isDto(name):
    return name[name.rfind('.')-len('dto'): name.rfind('.')].lower() == 'dto'
    
#find stereotype based on annotations
def get_stereotype(dto_obj):
    for stereotype in stereotypes:
        if stereotype in dto_obj['annotations'] and dto_obj['annotations'][stereotype]:
            return ' << ' + stereotype + ' >> '
    return ''
    pass

#define start of uml text 
uml_text = '@startuml\n'

#styling
uml_text += 'skinparam class {\n    BackgroundColor PaleGreen\n     ArrowColor SeaGreen\n   orderColor SpringGreen\n}\n'
uml_text += 'skinparam enum {\n    BackgroundColor PaleBlue\n     ArrowColor Cyan\n   orderColor Blue\n}\n'

#define connections info
uml_connections = ''



#split into pages if large:
#TODO: take out hardcode
#uml_text += '\' Split into ' + str(int(len(dto_data)/8)) + ' pages\npage 2x2\n'
#each class in json
color = 'Blue'
for i in dto_data:
    if i['className'] not in class_to_ignore:
        uml_text += 'class ' + (i['className']) 
        uml_text += get_stereotype(i)
        uml_text += get_properties(i)
        uml_text += '\n'
for i in enum_list:
    uml_text += 'enum ' + get_class_name(i['value']['name']) + ' {\n'
    for j in i['value']['values']:
        uml_text += '   ' + j['name'] + '\n'
    uml_text += '}\n'

#define end of uml text
uml_text += '@enduml'

#write uml text to txt file
file1 = open('umldiagram' + file_ver + '.txt','w')
file1.write(uml_text)
file1.close() 