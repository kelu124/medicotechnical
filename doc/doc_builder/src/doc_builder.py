# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import fnmatch
import os
import os.path
import codecs
# import markdown
# import sys
# import string
import re

repo_dir = "../../../"
interfaces_col = "interfaces"
default_doc = "readme.md"

doc_build_dir = "../../build/"
cfg_matrix_name = doc_build_dir + "configurations.md"

#-------------------------------------------------------------------------------
def collection(name):
  rootPath = repo_dir + name
  pattern = default_doc
  ret=[]
  for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
      full_path = os.path.join(root, filename)
      ret += [full_path]
  return ret

#-------------------------------------------------------------------------------
def md_parse(text):
  lines = text.splitlines()
  dom = {}
  context = dom
  for i in range(0, len(lines)-1):
    re_obj = re.search(r"^# Interface", lines[i])
    if re_obj:
      context["interface"]={}
      context=context["interface"]

    re_obj = re.search(r"^## Name", lines[i])
    if re_obj:
      context["name"]= re.search(r"\[`(ITF-.+)`\]", lines[i+1]).group(1)

    re_obj = re.search(r"^## Title", lines[i])
    if re_obj:
      context["title"]= lines[i+1]

    re_obj = re.search(r"^## Amplitude", lines[i])
    if re_obj:
      context["amplitude"]= lines[i+1]
    
  return dom

#-------------------------------------------------------------------------------
def doc(name):
  input_file = codecs.open(name, mode="r", encoding="utf-8")
  text = input_file.read()
  dom = md_parse(text)
  return dom

#-------------------------------------------------------------------------------
def store(name, text):
  output_file = codecs.open(cfg_matrix_name, "w", encoding="utf-8",  errors="xmlcharrefreplace" )
  output_file.write(text)
  return name

#-------------------------------------------------------------------------------
if __name__ == "__main__":
  print("Documentation builder start :")

  md ="# Interfaces table\n\n"
  md+="| Name | Title | Amplitude |\n"
  md+="|------|-------|-----------|\n"
  
  doc_names = collection(interfaces_col)
  for doc_name in doc_names:
    print("<<< " + doc_name)
    dom = doc(doc_name)
    print(dom)
    n = dom["interface"]["name"]
    t = dom["interface"]["title"]
    a = dom["interface"]["amplitude"]
    md += '|[`{name}`](../../interfaces/{name} "{title}")|_{title}_|{amplitude}|\n'.format(
          name=n, title=t, amplitude=a)

  store(cfg_matrix_name, md)
  print(">>>\n" + md)
