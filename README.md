### Installation

```bash
git clone https://github.com/Ninou01/Django-Blog.git
cd Django-Blog
```

if you are using a virtualenv then you need to create a new virtual environment and activate it 

```bash
virtualenv env 
 env\Scripts\activate.bat
```

then install install the requirement packages 

```bash
pip install -r requirements.txt 
```

### Run

```bash
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
```

### Create Admin User 

```bash
python manage.py createsuperuser
```

