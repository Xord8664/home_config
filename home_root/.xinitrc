[[ -f ~/.xprofile ]] && source ~/.xprofile
if [[ -f ~/.Xresourses ]]; then xrdb -merge ~/.Xresourses ; fi
