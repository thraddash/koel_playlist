#!/usr/bin/env python3

import os
import subprocess
from simple_term_menu import TerminalMenu

def get_directories():
  curr_path=os.getcwd() ## current directory path
  list_directories=[]

  for item in os.listdir(curr_path):
    if os.path.isdir(os.path.join(curr_path, item)):
      list_directories.append(item)
  return(list_directories)

def menu():
  terminal_menu = TerminalMenu(
    get_directories(),
    title="List of Directories:",
    multi_select=True,
    show_multi_select_hint=True,
    show_multi_select_hint_text="Press <space> for multi-selection and <enter> to apply changes",
    menu_cursor_style=("fg_green", "bold"),
    menu_highlight_style=("fg_green", "bold"),
    multi_select_cursor="[x] ",
    #multi_select_cursor_brackets_style=("fg_yellow", "bold"),
    multi_select_cursor_style=("fg_green", "bold"),         
  )
  menu_entry_index = terminal_menu.show()
  selected_entries = terminal_menu.chosen_menu_entries
  curr_path=os.getcwd() ## current directory path

  for dir_name in selected_entries:
    for file in os.listdir(dir_name):
       if (file.endswith(".mp3") or file.endswith(".m4a")):
        #replace space with underscore, add underscore in front and back of dir_name
        name = file.rsplit(('.'), 1)
        dir_underscore = dir_name.replace(" ","_")
        dir_underscore = ''.join(('_',dir_underscore, '_'))

        #print(dir_underscore, name[0], name[1])
        #check if name.endswith dir_underscore
        if dir_underscore in name[0]:
          len_dir_name = len(dir_name)+3
          fix_name = name[0][:-len_dir_name] # remove foldername end of file
          #print(fix_name + "." + name[1])
          os.rename( curr_path + '/' + dir_name + '/' + file, curr_path + '/' + dir_name + '/' + fix_name + "." + name[1])
        else:
          print("[Skipped no changes needed] " + name[0])

if __name__ == "__main__":
  menu()
