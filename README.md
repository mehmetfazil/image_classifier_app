# How to Deploy Deep Learning Models

We've all been there. You train a fancy model, get strong results, then what? It is usually meaningless if you can't make it accessible by the people who need it. So you have to serve your model somehow. Fear no more, I got you covered. In this post I will guide you through from zero to hero and show how to deploy your model with a web application. For this project, we will use Keras model and deploy it with Flask using Docker. Do not hesitate if you are not familiar with them, I will give a basic overview of each step.

Requirements
- Python, definetely
- A Keras model
- Docker

# Preparing



## Save the Keras Model

Keras models have built-in `save` method, so after training you can save your model easily with

    model.save('model.h5')


## Prepare Flask

Well, if you have never used Flask, it might seem a bit confusing at first, but I actually pretty like it as it enables to transfer ideas into reality real quick. It is basically a web application builder for your Python logic.

A minimal Flask app might look like this,

    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

It basically returns *'Hello World'* when you visit the web address from your browser. It might be something like localhost:5000 which is not important as of now. What we need to now is

 1. Load the Keras Model
 2. Get the test image to classify
 3. Make predictions
 4. Return results
 
 For this steps, you can simply use the following structure named `app.py`
