#!/bin/bash

PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
PATH=$PATH:/Applications/Sublime\ Text.app/Contents/SharedSupport/bin
export PATH=/usr/local/Caskroom/miniconda/base/bin:$PATH

if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi

trap 'killall -9 python && sleep 0.5 && reset' INT
export PS1="\[\[\033[39;2m\]\w\[\033[m\]\$ "
export CLICOLOR=1F
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'

printf '\e[8;1000;1000t'

alias q='QHOME=~/.q rlwrap -r ~/.q/m64/q'
alias todo='cd /Users/spencersharp/Documents/Organization/TODO'
alias ecc='ssh -i ~/Desktop/random/bb.pem ubuntu@ec2-3-16-214-130.us-east-2.compute.amazonaws.com'
alias ect='scp -i ~/Desktop/random/bb.pem ~/Desktop/random/testing-file.txt ubuntu@ec2-3-16-214-130.us-east-2.compute.amazonaws.com:~'
alias src='source $HOME/Desktop/bash'

#alias build='var=$PWD && cd $SPOOLS_BUILD_PATH && python $SPOOLS_BUILD_PATH/build.py && cd $var'
#alias run='var=$PWD && cd ~/.spools && python $SPOOLS_BUILD_PATH/spools/music rate -d -s 3DK6m7It6Pw857FcQftMds 10.0 && cd $var'
alias music='cd $SPOOLS_PATH/src/main/modules/music/src'
alias cli='cd $SPOOLS_PATH/src/lib/cli/main'
alias bmusic='cd $SPOOLS_PATH/build/spools/music/lib'
alias spools='cd $SPOOLS_PATH'
alias filesys='cd /Users/spencersharp/Documents/Coding/Active/spools/build/spools/lib/filesys'

#shopt -s extdebug
#trap 'curpwd=$PWD && val=$BASH_COMMAND && REGEX="^[0-9]{1,2}\.[0-9].*" && if [[ $val =~ $REGEX ]]; then cd ~/.spools && python $SPOOLS_BUILD_PATH/spools/music `cat $HOME/.spools/test/music/info.txt` $val && cd $curpwd && false; else true; fi' DEBUG