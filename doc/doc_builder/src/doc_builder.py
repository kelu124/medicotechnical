# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import fnmatch
import os
import os.path
import codecs
# import markdown
import sys
import string
import re
 
if __name__ == "__main__":
  rootPath = '../../../interfaces'
  pattern = '*.md'
  cfg_matrix_name = '../../build/configurations.md'

  print("Documentation builder start :")
  out="# Configuration matrix\n\n"
  out+="## Interfaces\n\n"
  out+="| Name | Title | Amplitude |\n"
  out+="|------|-------|-----------|\n"
  for root, dirs, files in os.walk(rootPath):
      for filename in fnmatch.filter(files, pattern):
          full_path = os.path.join(root, filename)
          print("\n" + full_path)
          input_file = codecs.open(full_path, mode="r", encoding="utf-8")
          text = input_file.read()
          lines = text.splitlines()
#            html = markdown.markdown(text)
          for i in range(0, len(lines)-1):
            re_obj = re.search(r"^## Name", lines[i])
            if re_obj: itf_name = re.search(r"\[`(ITF-.+)`\]", lines[i+1]).group(1)
              
            re_obj = re.search(r"^## Title", lines[i])
            if re_obj: itf_title = lines[i+1]

            re_obj = re.search(r"^## Amplitude", lines[i])
            if re_obj: itf_amplitude = lines[i+1]

          out += "|[`" + itf_name + "`](../../interfaces/" + itf_name + " \"" + itf_title + "\")|_" + itf_title + "_|" + itf_amplitude + "|\n"""

  output_file = codecs.open(cfg_matrix_name, "w", encoding="utf-8",  errors="xmlcharrefreplace" )
  output_file.write(out)
  
