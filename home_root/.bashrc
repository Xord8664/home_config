#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias lsblk="lsblk -o MODEL,NAME,SIZE,UUID,FSTYPE,MOUNTPOINT,LABEL"
alias ll="ls -lah --color"
alias cp='cp -iv'
alias mv='mv -iv'

#[[ -z "$TMUX" ]] && [[ `echo $XTERM_VERSION` = XTerm* ]] && exec tmux
export EDITOR=vim

function nonzero_return() {
  RETVAL=$?
  echo "$RETVAL"
}

export PS1="\[\e[32m\]\t\[\e[m\] [\`nonzero_return\` \[\e[32m\]\u\[\e[m\]@\h \w]\\$ "
