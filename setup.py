import os

os.system("pip install --upgrade google-cloud-texttospeech")
#os.system("""export GOOGLE_APPLICATION_CREDENTIALS="steam-treat-397115-d9246f5f8e7e.json""""")
#os.system("""set GOOGLE_APPLICATION_CREDENTIALS="steam-treat-397115-d9246f5f8e7e.json""""")
os.system("curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-444.0.0-linux-x86_64.tar.gz")
os.system("tar -xf google-cloud-cli-444.0.0-linux-x86_64.tar.gz")
os.system("./google-cloud-sdk/install.sh")
os.system("./google-cloud-sdk/bin/gcloud init")
os.system("./google-cloud-sdk/bin/gcloud auth application-default login")