import sys
import os

from personalLib import ClauseScript as cs
character_definers = {
    "create_country_leader":"Country Leader",
    "create_corps_commander":"General",
    "create_field_marshal":"Field Marshal",
    "create_navy_leader":"Admiral",
    "create_operative_leader":"Operative",
}
search_paths = [
    "./history/countries",
    "./common/decisions",
    "./common/national_focus",
    "./events"
]

if __name__ == "__main__":
    char_log = open("./found_chars.log", "w+", encoding="utf8")
    for search_path in search_paths:
        char_log.write("Search Path: "+search_path+"\n")
        data_files = [search_path+"\\"+file for file in os.listdir(search_path) if file[-4:] == ".txt"]
        for data_file_path in data_files:
            char_log.write("\tFile: "+data_file_path+"\n")
            data_file = open(data_file_path, "r", encoding="utf8")
            file_scope = cs.Scope("file = { " + data_file.read() + " }")
            char_scopes = [scope for scope in file_scope.getAllValues() if scope.statement in character_definers]
            for char_scope in char_scopes:
                for value in char_scope.values:
                    if value.statement == "name":
                        char_log.write(f"\t\t{character_definers[char_scope.statement]}: {value.value}"+"\n")
                        break
