# BlockEngine installator
# run using	$ bash install.sh

GITURL="https://github.com/YuxiUx/BlockEngine.git"
PYDEPS="pygame numpy"
PROJNAME="BlockEngine"

gitClone() { 
  cprn INFO "Cloning repository";
  git clone $GITURL
  cd BlockEngine
}
installDepneds() {
  cprn INFO 'Install python dependeces...';
  pip3 install $PYDEPS || { 
      cprn W 'Sorry instalation failed. Attempt to install with sudo';
      sudo pip3 install $PYDEPS ;
  }
}
checkDeps() {
    cprn INFO 'Checking system dependences';
    cprn C Git;
    command -v git >/dev/null 2>&1 || { 
      cprn F "Git not found.  Aborting."; exit 1; }
    cprn E;
    cprn C python3;
    command -v python3 >/dev/null 2>&1 || { 
      command -v python >/dev/null 2>&1 || {
        cprn F "Python not found. You need to install python 3. Aborting."; exit 1; }
      pyv=$(python -c 'import sys; print(sys.version_info.major)')
      [[ pyv > 2 ]] || { cprn F 'You have python 2 but 3 is required. Aborting.'; exit 1; }
    }
    cprn E;
    cprn C pip3;
    command -v pip3 >/dev/null 2>&1 || {
      cprn F "pip3 not found.  You can install python dependences manualy"; exit 1;}
    cprn E;
}
checkName() {
    gitname="$(git remote -v | head -n1 | awk '{print $2}' | sed 's/.*\///' | sed 's/\.git//')";
    [[ $PROJNAME == $gitname ]] && {
        cprn INFO "Already cloned. continue to install dependences";
        cont;
      } || cprn W "You are in another git repository ($gitname)- you don't want to install this here";
}
isRepository() {
  if [ -d .git ]; then
    cprn INFO 'You are already in repository';
    checkName;
  else
    gitClone;
    cont;
  fi;
}

cprn() {
    case $1 in
      "F") printf "\e[41m[FAIL] $2 \e[0m\n";;
      "W") printf "\e[43m[WARING] $2 \e[0m\n";;
      "C") printf "\e[44m[CHECKING] $2... ";;
      "E") printf "OK\e[0m\n";;
      "N") printf "$2";;
      *)   printf "\e[0m[$1] $2 \r\n";;
    esac
}

cont() {
  installDepneds;
  echo "Instalation is done";
}

instl() {
  echo "Installing BlockEngine";
  checkDeps;
  isRepository;
}

instl;
