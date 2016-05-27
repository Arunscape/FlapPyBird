cd
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo apt-get update && sudo apt-get upgrade
sudo apt install python python3 python-tk python3-tk git -y
sudo apt-get install mercurial
hg clone https://bitbucket.org/pygame/pygame
cd pygame
sudo apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev \
  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
python3 setup.py build
sudo python3 setup.py install
cd 
git clone https://github.com/Arunscape/FlapPyBird.git
git config --global user.email "arunscape@gmail.com"
git config --global user.name "Arunscape
