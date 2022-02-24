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
      if (file.startswith(dir_name) and (file.endswith(".mp3") or file.endswith(".m4a"))):
        print("[Skipped foldername prefix exist!] " + file)
      elif (not file.startswith(dir_name) and (file.endswith(".mp3") or file.endswith(".m4a"))):
        print("[Adding prefix] ==> " + file)
        os.rename( curr_path + '/' + dir_name + '/' + file, curr_path + '/' + dir_name + '/' + dir_name + ' ' + file)
      elif (not file.startswith(dir_name) and (not file.endswith(".mp3") or not file.endswith(".m4a"))):
        #print("[Skipped] " + "Directory => " + dir_name + " ==> " + file)
        continue 

if __name__ == "__main__":
  menu()
