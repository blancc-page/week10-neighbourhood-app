# Neighbourhood App

> A webapp that brings the neighbourhood together.

## :hammer: Built With

- HTML, CSS
- Python, Django, PostgreSQL

### :computer: Setup
To get a local copy up and running follow these simple example steps.

##### Cloning the repository:  
 ```bash 
git clone https://github.com/blancc-page/week10-neighbourhood-app.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd week10-neighbourhood-app 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations neighbourhoodApp
 ``` 
 Now Migrate  
 ```bash 
python manage.py migrate 
```
##### Run the application  
 ```bash 
python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Behaviour Driven Development

> A user should be able to:

- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## :trollface: Authors

👤 **Moses Muta**

- GitHub: [@githubhandle](https://github.com/blancc-page)
- LinkedIn: [LinkedIn](<linkedIn link>)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## :muscle: Show your support

    Please give a⭐️if you love this project.
    

## 📝 License

This project is [MIT](./MIT.md) licensed.