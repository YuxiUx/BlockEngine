# BlockEngine installator
# run using	$ bash install.sh

GITURL="https://github.com/YuxiUx/BlockEngine.git"
PYDEPS="pygame numpy"
PROJNAME="BlockEngine"

gitClone() { 
  echo "Cloning repository";
  git clone $GITURL
  cd BlockEngine
}
installDepneds() {
  echo "Install python dependeces...";
  pip3 install pygame $PYDEPS || { 
      echo 'sorry instalation failed we need a sudo' ;
      sudo pip3 install $PYDEPS ;
  }
}
checkDeps() {
    echo "Checking system dependences";
    echo "[Checking] Git";
    command -v git >/dev/null 2>&1 || { 
      echo >&2 "Required git but it's not installed.  Aborting."; exit 1; }
    echo "OK";
    echo "[Checking] python3";
    command -v python3 >/dev/null 2>&1 || { 
      echo >&2 "Required python3 but it's probably not installed. Trying find another compatibile version"; 
      command -v python >/dev/null 2>&1 || {
        echo >&2 "Definetly you need to install python 3"; exit 1; }
      pyv=$(python -c 'import sys; print(sys.version_info.major)')
      if (( pyv > 2 )); then 
        echo 'Compatibile version of python found';
       else 
        echo 'You have python 2 but 3 is required'; exit 1;
      fi;
    }
    echo "OK";
    echo "[Checking] pip3";
    command -v pip3 >/dev/null 2>&1 || {
      echo >&2 "Required pip3 but it's not installed. You can install python dependences manualy"; exit 1;}
    echo "OK";
}
checkName() {
    gitname=$(git remote -v | head -n1 | awk '{print $2}' | sed 's/.*\///' | sed 's/\.git//');
    [[ $PROJNAME == $gitname ]] && {
        echo "Already cloned. continue to install dependences";
        cont;
      } || echo "You are in another git repository - you dont need install this here";
}
isRepository() {
  if [ -d .git ]; then
    echo 'You are already in repository';
    checkName;
  else
    gitClone;
    cont;
  fi;
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
