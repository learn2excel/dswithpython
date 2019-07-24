#install python-dotenv
from dotenv import find_dotenv
from dotenv import load_dotenv
import os
from requests import session
#find env path
envpath=find_dotenv()
print(envpath)
load_dotenv(envpath)
#get values from environment
kaggleusername=os.environ.get("KAGGLE_USERNAME")
kagglepassword=os.environ.get("KAGGLE_PASSWORD")
print(kaggleusername)
print(kagglepassword)


#payload =  {
#    'action': 'login',
#    'username': os.environ.get("KAGGLE_USERNAME"),
#    'password': os.environ.get("KAGGLE_PASSWORD")
#}
#url= "kaggle competitions download -c titanic"