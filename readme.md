# Janulus
![](https://github.com/bri-maybe/two-hackathon-2023/blob/main/JA.png)

Janulus is an AI-powered conversation app designed to help you become fluent in just about any language you want. Janulus provides tailored conversations (via text or audio) based on users' interests and abilities with real-time feedback. Paired with progress tracking across 5 proficiency ratings, this app will build your confidence while encouraging consistent learning.

Practice in conversation is one of the best ways to improve in a language. However, friends who speak that language won't always be available to practice with you, and beginners may feel nervous about making mistakes in front of someone else. This app aims to bridge that gap, by providing a stress-free environment where learners of all skill levels can engage in customisable conversations 24/7 while receiving instant tailored feedback.

<iframe width="560" height="315" src="https://www.youtube.com/embed/--PJx-rJRX4?si=77zM6oILDB8ZgH3o" title="Janulus Demo Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Who is it for?
People who want to practice conversations in a foreign language but cannot find another speaker of that language (or would like to practice in a stress-free environment)

## Key features
- Lets user chat with an AI in a language of choice
- Wide range of languages to choose from
- Text-to-speech
- Per-text Feedback and General Conversation Feedback

## How to use
Copy and paste your openai key to `key.py` with `KEY= <secret key>`.
Then ensure your have all dependancy install and run the app with `python -m app`
Once started, follow the link shown on the console and:

1. Create username and sign in
2. Select language, proficiency level, and hobbies
3. Initiate conversation in the language
4. End conversation after satisfied

## To use TTS:
1. have to pip install google text to speech
    `pip install --upgrade google-cloud-texttospeech`
2. have to get json api key
    from the google cloud site
3. have to download google cloud cli
    `curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-444.0.0-linux-x86_64.tar.gz`
    
4. extract gcloud and install, as well as initialise, and login with credentials etc from the dir where u extracted from
    `tar -xf google-cloud-cli-444.0.0-linux-x86_64.tar.gz`
    `./google-cloud-sdk/install.sh`
    `./google-cloud-sdk/gcloud init`
5. run google tts file in src/ or can import function with parameters (romanised text, language, gender)


### How it was implemented
A Python back-end interacts with ChatGPT via the OpenAI API to create the language facilitator functionality. Text-to-speech is achieved via the Google Cloud TTS API. User data is stored locally using JSON files (in the full release, a web server will be hosted which will store this data). The front-end is built using Flask, JavaScript, HTML and CSS which provides an interface to interact with the application.


