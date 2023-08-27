"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
	https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

import os

#os.system('export GOOGLE_APPLICATION_CREDENTIALS="steam-treat-397115-d9246f5f8e7e.json"')
#os.system('set GOOGLE_APPLICATION_CREDENTIALS="steam-treat-397115-d9246f5f8e7e.json"')

language_voices = {
    "arabic" : ["ar-XA", "ar-XA-Wavenet-A", "ar-XA-Wavenet-C"],
    "bengali" : ["bn-IN", "bn-IN-Wavenet-A", "bn-IN-Wavenet-B"],
    "cantonese" : ["yue-HK", "yue-HK-Standard-A", "yue-HK-Standard-B"],
    "czech" : ["cs-CZ", "cs-CZ-Wavenet-A", "cs-CZ-Wavenet-A"], # no male voice for czech
    "danish" : ["da-DK", "da-DK-Neural2-D", "da-DK-Wavenet-C"],
    "dutch" : ["nl-BE", "nl-BE-Wavenet-A", "nl-BE-Wavenet-B"],
    "english" : ["en-AU", "en-AU-Neural2-C", "en-AU-Neural2-B"],
    "filipino" : ["fil-PH", "fil-ph-Neural2-A", "fil-ph-Neural2-D"],
    "french" : ["fr-FR", "fr-FR-Neural2-A", "fr-FR-Neural2-B"],
    "german" : ["de-DE", "de-DE-Neural2-C", "de-DE-Neural2-B"],
    "hindi" : ["hi-IN", "hi-IN-Neural2-D", "hi-IN-Neural2-C"],
    "indonesian" : ["id-ID", "id-ID-Wavenet-D", "id-ID-Wavenet-B"],
    "italian" : ["it-IT", "it-IT-Neural2-A", "it-IT-Neural2-C"],
    "japanese" : ["ja-JP", "ja-JP-Neural2-B", "ja-JP-Neural2-D"],
    "korean" : ["ko-KR", "ko-KR-Neural2-A", "ko-KR-Neural2-C"],
    "mandarin" : ["cmn-CN", "cmn-CN-Wavenet-A", "cmn-CN-Wavenet-B"],
    "portugese" : ["pt-BR", "pt-BR-Neural2-A", "pt-BR-Neural2-B"],
    "punjabi" : ["pa-IN", "pa-IN-Wavenet-A", "pa-IN-Wavenet-D"],
    "russian" : ["ru-RU", "ru-RU-Wavenet-C", "ru-RU-Wavenet-B"],
    "spanish" : ["es-US", "es-US-Neural2-A", "es-US-Neural2-C"],
    "swedish" : ["sv-SE", "sv-SE-Wavenet-A", "sv-SE-Wavenet-C"],
    "tamil" : ["ta-IN", "ta-IN-Wavenet-A", "ta-IN-Wavenet-D"],
    "thai" : ["th-TH", "th-TH-Neural2-C", "th-TH-Neural2-C"],   # no male voice for thai
    "turkish" : ["tr-TR", "tr-TR-Wavenet-D", "tr-TR-Wavenet-E"],
    "ukrainian" : ["uk-UA", "uk-UA-Wavenet-A", "uk-UA-Wavenet-A"], # no male voice for ukrainian
    "vietnamese" : ["vi-VN", "vi-VN-Neural2-A", "vi-VN-Neural2-D"]
}

def synthesise(input, language, gender, num: int = None):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    #synthesis_input = texttospeech.SynthesisInput(text=input("Text to synthesise: "))
    synthesis_input = texttospeech.SynthesisInput(text=input)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    if gender.lower() == 'male':
        ssml_gender = texttospeech.SsmlVoiceGender.MALE
        name = language_voices[language.lower()][2]
    else:
        ssml_gender = texttospeech.SsmlVoiceGender.FEMALE
        language_voices[language.lower()][1]
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_voices[language.lower()][0], name=name, ssml_gender=ssml_gender
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    if num is None:
        f = open("static/audio/output.mp3", "wb")
        print('Audio content written to file "output.mp3"')
    else:
        f = open(f"static/audio/output{num}.mp3", "wb")
        print(f'Audio content written to file "output{num}.mp3"')

    f.write(response.audio_content)
    f.close()

    if num is None:
        return "static/audio/output.mp3"
    return f"static/audio/output{num}.mp3"



def list_voices():
    """Lists the available voices."""

    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print(f"Name: {voice.name}")

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print(f"Supported language: {language_code}")

        ssml_gender = texttospeech.SsmlVoiceGender(voice.ssml_gender)

        # Display the SSML Voice Gender
        print(f"SSML Voice Gender: {ssml_gender.name}")

        # Display the natural sample rate hertz for this voice. Example: 24000
        print(f"Natural Sample Rate Hertz: {voice.natural_sample_rate_hertz}\n")