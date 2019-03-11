<h1>Django-RESTful-API-MONGODB</h1>

ENV setup:
install python 3.7.2 32-bit

clone the git repository.

    run cmd-$ pip install -r requirements.txt
    used dependency:
        Django==2.1.7                 #django latest version
        django-ckeditor==5.6.1        #web text editor
        pillow==5.4.1                 #Python Imaging Library
        python-decouple==3.1          #Strictly separate settings from code
        djangorestframework==3.9.2    #toolkit for building Web APIs
        djongo==1.2.31                #mongodb engine
        dnspython==1.16.0             #high and low level access to DNS

RUN Project:
cmd: -$python manage.py makemigrations
        -$python manage.py migrate -$python manage.py createsuperuser
        -$python manage.py runserver

    open in browser/bash:  http://localhost:8000/

Use mongodb cloud:
make change on,
../rootApp/settings.py [line no. 80-90]

EXAMPLE:
GET http://localhost:8000/product

        {"count":2,"next":null,"previous":null,"results":[{"url":"http://localhost:8000/product/1/?format=json","id":1,"name":"coca-cola","details":"coke 250ml","subcategory":"http://localhost:8000/subcategory/3/?format=json","price":25,"stock":10000,"sells":10},{"url":"http://localhost:8000/product/2/?format=json","id":2,"name":"7up","details":"soda 250ml","subcategory":"http://localhost:8000/subcategory/3/?format=json","price":20,"stock":100000,"sells":100}]}


    GET http://localhost:8000/users

        {"count":1,"next":null,"previous":null,"results":[{"url":"http://localhost:8000/users/1/?format=json","username":"admin","email":"admin@admin.com","groups":[]}]}
