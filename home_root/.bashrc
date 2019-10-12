[[ $- != *i* ]] && return

export EDITOR=vim
PS1='\t \[\e[32m\]\u\[\e[m\]@\h \W\$ '
shopt -s histappend
alias ls='ls --color=auto'
alias lsblk="lsblk -o MODEL,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,UUID"
alias ll="ls -lah --color"
