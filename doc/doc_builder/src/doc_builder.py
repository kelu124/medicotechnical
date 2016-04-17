# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import fnmatch
import os
import os.path
import codecs
import markdown
import sys
import string
import re
 
#def print_fnmatches(pattern, dir, files):
#    for filename in files:
#        if fnmatch(filename, pattern):
#            full_path = os.path.join(dir, filename)
#            print(full_path)
#            if fnmatch(filename, "readme.md"):
#              input_file = codecs.open(full_path, mode="r", encoding="utf-8")
#              text = input_file.read()
##              text = open(full_path, encoding='utf-8').read()
##              text = open(full_path).read()
#              html = markdown.markdown(text)
#              print(html)
 
if __name__ == "__main__":
  rootPath = '../../../interfaces'
  pattern = '*.md'
  cfg_matrix_name = '../../build/configurations.md'

  print("Documentation builder start :")
  out="# Configuration matrix\n\n"
  out+="## Interfaces\n\n"
  out+="| Name | Title |\n"
  out+="|------|-------|\n"
  for root, dirs, files in os.walk(rootPath):
      for filename in fnmatch.filter(files, pattern):
          full_path = os.path.join(root, filename)
          print("\n" + full_path)
          input_file = codecs.open(full_path, mode="r", encoding="utf-8")
          text = input_file.read()
          lines = text.splitlines()
#          html = markdown.markdown(text)
          for i in range(0, len(lines)-1):
            re_obj = re.search(r"^# ?\[(ITF-.+)\]", lines[i])
            if re_obj:
              print(re_obj.group(1))
              out += "|`" + re_obj.group(1) + "`"
            re_obj = re.search(r"^## Title", lines[i])
            if re_obj:
              print(lines[i+1])
              out += "|_" + lines[i+1] + "_|\n"
  output_file = codecs.open(cfg_matrix_name, "w", encoding="utf-8",  errors="xmlcharrefreplace" )
  output_file.write(out)
  