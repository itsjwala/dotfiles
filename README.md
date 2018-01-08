# dotfiles

## sublime setup
* copy all file of sublime folder into 
  <code>~/.config/sublime-text-3/Packages/User</code>
  
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
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"</code>
  ```
* now copy .zshrc file from repo to <code>~/.zshrc</code>

## virtual environment setup for python
> tutorial [link](https://www.sitepoint.com/virtual-environments-python-made-easy/) 
* install virtaulenv wrapper 

  ```shell
  pip install virtualenvwrapper
  ```
* keep all virtualenvs in same location
    ```shell
    mkdir ~/.virtualenvs 
    export WORKON_HOME=~/.virtualenvs
    ```
* edit .zshrc file , add line
  ```shell
  . /usr/local/bin/virtualenvwrapper.sh 
  ```
 * now reload zsh using
   ```shell
   source .zshrc 
   ```
## git setup
* install git
* edit <code>~/.gitconfig</code> file with .gitconfig from repo
 
 
