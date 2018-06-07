sudo apt update
sudo apt install python-dev python-pip python-virtualenv gcc apache2 git
cd
git clone git@github.com:marromang/couchweb.git
virtualenv v-couch
source v-couch/bin/activate
pip install -r requirements.txt
