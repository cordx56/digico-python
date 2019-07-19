export $(cat .env | xargs); pipenv run ./discordClient.py ./wiki.model ./ansLearn.txt 
