import yaml
from yaml.loader import SafeLoader
from json2table import convert

#import the yml file
with open('new2.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)

json_object = data
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style" : "width:100%"}
html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
print(html)