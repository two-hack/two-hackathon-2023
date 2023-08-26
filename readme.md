hack
order of prompts:
sec
cri
per
con
fin


for tts:
1. have to pip install google text to speech
    pip install --upgrade google-cloud-texttospeech
2. have to get json api key
    from the google cloud site
3. have to download google cloud cli
    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-444.0.0-linux-x86_64.tar.gz
    
4. extract gcloud and install, as well as initialise, and login with credentials etc from the dir where u extracted from
    tar -xf google-cloud-cli-444.0.0-linux-x86_64.tar.gz
    ./google-cloud-sdk/install.sh
    ./google-cloud-sdk/gcloud init
5. run google tts file in src/ or can import function with parameters (romanised text, language, gender)