
# Phishing URL Detection Workshop

Welcome fellow MIST members!\
\
In this repository you shall find the code dump for the workshop organised under MIST for Artificial Intelligence and Machine Learning in Cybersecurity for club members. To put our model to test we also have an API set up for users to test out using custom frontend. 


## Run API Locally

Fork and clone the project

```bash
  git clone https://github.com/RampageousRJ/Movie-Recommender-System.git
```


Install all the  dependencies using the command

```bash
  pip install -r requirements.txt
```

After setting up all the dependancies, run the python script 'app.py' in the root directory which would run on the port 5000 by default (can be changed)

```bash
  python app.py
```


## API Reference

#### Send a POST request to the local URL only after the API is up and running

```
  POST http://127.0.0.1:5000
````

Type of input for the API 

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `url`      | `string` | Enter url to be checked|

The API processes the URL and returns the output in JSON format having the following fields:


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `prediction`      | `string` | 'Good URL' or 'Bad URL' based on the prediction, can be changed on the 'app.py' code as preferred.|

## Feedback

If you have any feedback or queries, please reach out to [Rishabh](https://github.com/RampageousRJ)

