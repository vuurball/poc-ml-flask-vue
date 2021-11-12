### POC - trying out using ML movie recommendation script with Flask and VueJS

![img](https://github.com/vuurball/poc-ml-flask-vue/blob/master/screenshot.png)

#### Flask

**creation guide:**
```
> mkdir server
> cd server
> python -m venv env
> pip install Flask
> pip install flask_cors, ..., ...
```

**project init/server run:**
```
> cd server
> env\Scripts\activate
> python app.py
```
server is up on  http://127.0.0.1:5000/ 

#### Vue

**creation guide:**
```
> npm i -g @vue/cli@3.7.0
> vue create client
>> Presets: Manual
>> Features: Babel, Router, Linter
>> History? Yes
>> Linter? Airbnb
>> Lint on save
>> package.json
>> Preset? No
```

**project init/server run:**
```
> cd client
> npm run serve
```
client is up on  http://127.0.0.1:8080/ 
