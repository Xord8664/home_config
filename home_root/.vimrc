set pastetoggle=<F3>
set tabstop=4
set expandtab
set showmatch
set wrap
set ai

if &diff
    syntax off
else
    syntax on
endif

try
    source ~/.config/json.vim
catch
endtry
