# NOW
Unlimited movies, TV shows, and more. Watch anywhere. Cancel anytime. Ready to watch? Enter your email to create or restart your membership. [NOW TV](https://nowtv.pythonanywhere.com/)


Create Virtual enviroumunt if there isn't
```bash
python3 -m venv nowtv
```
Activate The Virtual enviroumunt
```bash
source nowtv/bin/activate
```
Install the package requirements
```bash
pip3 install -r requirements.txt
```
Collect the static files by the Command Bellow
```bash
python3 manage.py collectstatic
```
Make Migrations for the DataBase
```bash
python3 manage.py makemigrations
```
Migrate The DataBase
```bash
python3 manage.py migrate
```
Create a admin user
```bash
python3 manage.py createsuperuser
```
Run The Website
```bash
python3 manage.py runserver
```
