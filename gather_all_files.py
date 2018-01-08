import os
from os import path

print("working on {} directory ".format(os.getcwd()))
print("continue [y/n] .. ")
opt = input()
if(opt[0:1].lower() == 'n'):
    quit()

print("running script ..")

print("copying sublime files ..")

try:
    os.system("rm -rf sublime")
    print("./sublime directory removed")
except FileNotFoundError as e:
    pass

print("creating sublime directory ..")
os.mkdir("sublime")


def surround_with_single_quotes(s):
    return '\'{}\''.format(s)


os.chdir("sublime")

sublime_path = path.join(os.getenv("HOME"), ".config/sublime-text-3/Packages/User")

for f in os.listdir(sublime_path):
    abs_path = path.join(sublime_path, f)
    if(not path.isdir(abs_path) and (abs_path.endswith(".sublime-settings") or abs_path.endswith(".sublime-build"))):
        source = surround_with_single_quotes(abs_path)
        destination = surround_with_single_quotes(f)
        os.system("cp %s %s" % (source, destination))

print("sublime files copying finished ")

os.chdir(path.pardir)

print("now copying .zshrc ..")

os.system("cp ~/.zshrc .zshrc")

print(".zshrc file copying complete")

print("now copying .gitconfig ..")

gitconfig_file = open("./.gitconfig", "w")

with open("/home/jigar/.gitconfig", "r") as source:

    for line in source:
        gitconfig_file.write("\temail = abc@pqr.xyz\n" if "email" in line else line)

gitconfig_file.close()
print(".gitconfig file copying complete")

print("Execution complete")
