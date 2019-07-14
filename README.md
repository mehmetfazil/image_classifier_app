# How to Deploy Deep Learning Models

We've all been there. You train a fancy model, get strong results, then what? It is usually meaningless if you can't make it accessible by the people who need it. So you have to serve your model somehow. Fear no more, I got you covered. In this post I will guide you through from zero to hero and show how to deploy your model with a web application. For this project, we will use Keras model and deploy it with Flask using Docker. Do not hesitate if you are not familiar with them, I will give a basic overview of each step.

# Preparing

You can start with cloning my repository with

    git clone https://github.com/mehmetfazil/image-classifier-app.git

Then you can install packages in the requirements file if you don't have them already

    pip install -r requirements.txt

## Directory Structure

Here is the basic suggested Flask structure

```bash
├── static
│   ├── model.h5
│   ├── images
│   │   ├── uploaded_image
├── templates
│   ├── upload.html
│   ├── prediction.html
├── app.py
├── requirements.txt
├── Dockerfile
```
We will use the static folder to host our model and the uploaded image to be classified, as we don't want to store all the images uploaded we will basically overwrite each uploaded image to uploaded_image file. You may also uncomment some lines from `app.py` to store each image with their filenames if you would like to. Templates folder will store the html files for our application, `app.py` is where actual stuff happens. Requirements and Dockerfile will be used for Docker.

## Save the Keras Model

Keras models have built-in `save` method, so after training you can save your model easily with

    model.save('model.h5')

I have used pretrained ResNet50 model from Keras, which you can also find from official Keras documentation.

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
 
Good news is, I already implemented this step for you, you can simply use the `app.py` file. It enables users to uplaod an image and make predictions. Run it and check localhost:5000, you will see an upload button to make your predictions.

## Deploy it with Docker

If you have never used docker, you can think of it like a virtual machine that is dedicated to your application, but without the overhead of installing a brand new operating system. It has it's own benefits, but one thing that is absolutely great is you can isolate your logic for each project, which means your container has one and only job. So it is configured to use the packages and does not interfere with the system-wide installed packages, and you can deploy it on any machine where Docker is installed.

uild the Docker image with 

    docker build .
    
It will create an image something like 32afacdad806. If you can not find the image you can run docker images. Then you can run it with 

    docker run -p 5000:5000 --volume=/path/to/repo/image-classifier-app:/app 32afacdad806

## Summary

This tutorial actually happened to be shorter than I expected, so feel free to ask any questions. Pull requests are always welcomed!

## Further notes

This Flask app is not production ready to be deployed. You might consider WSGI server, which I will also add it to this documentation later.

Also, uploading files to server needs more consideration, especially you may want to secure filenames to prevent potentially harmful uploads to other directories than desired.

