# dotfiles

## sublime setup
* copy all file of sublime folder of the repo into 
  <code>~/.config/sublime-text-3/Packages/User</code>
## vscode setup
* copy all file of vscode folder of the repo into
`~/.config/Code/User`

## zsh setup
* install zsh 
```shell
sudo apt install zsh 
```
* set zsh as default shell
```shell
chsh -s $(which zsh) 
```
* check if zsh is default shell
```shell
echo $SHELL 
```
* install oh-my-zsh

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
  ```
* now copy .zshrc file from repo to <code>~/.zshrc</code>

## npm global package in user directory

###### 1. Create a directory for global packages

```sh
mkdir "${HOME}/.npm-packages"
```

###### 2. Tell `npm` where to store globally installed packages

```sh
npm config set prefix "${HOME}/.npm-packages"
```
rest of the setup is in [.zshrc](https://github.com/jigarWala/dotfiles/blob/master/.zshrc) so copy that too

## virtual environment setup for python
> Using [pipenv](https://github.com/pypa/pipenv) from now.

## git setup
* install git
* edit <code>~/.gitconfig</code> file with .gitconfig from repo
 
 ### Note 
  Added a python script which will grab all the sublime config files , .zshrc and .gitconfig files
 
