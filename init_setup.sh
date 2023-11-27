echo [$(date)]: "START"                     ## echo is like print/log statements in .sh format files
echo [$(date)]: "creating env with python 3.8 version" 
conda create --prefix ./env python=3.8 -y  ## creating virtual environment

echo [$(date)]: "activating the environment" 
source activate ./env                      ## activate the environment  

echo [$(date)]: "installing the dev requirements" 
pip install -r requirements_dev.txt        ## Install the requirements
echo [$(date)]: "END" 