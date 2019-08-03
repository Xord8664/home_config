#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#PS1='[\u@\h \W]\$ '
alias lsblk="lsblk -o MODEL,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,UUID"
alias ll="ls -lah --color"
#[[ -z "$TMUX" ]] && [[ `echo $XTERM_VERSION` = XTerm* ]] && exec tmux
