cd
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:mystic-mirage/pycharm
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install python python3 python-tk python3-tk git pycharm-community mercurial -y
hg clone https://bitbucket.org/pygame/pygame
cd pygame
sudo apt-get install -y python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev \
  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
python3 setup.py build
sudo python3 setup.py install
cd 
git clone https://github.com/Arunscape/FlapPyBird.git
git config --global user.email "arunscape@gmail.com"
git config --global user.name "Arunscape
cd ~/FlapPyBird
pycharm-community
