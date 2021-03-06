#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr


def voice_recognize():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Say something!")
        audio = r.listen(source)


    '''
    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    '''


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        try:
            result1 =r.recognize_google(audio,language='en-US')
        except:
            result1 = ''
        try:
            result2 = r.recognize_google(audio, language='zh-TW')
        except:
            result2 = ''
        if result1 != ''  and result2 == '':
            print("Google Speech Recognition thinks you said " + result1)
            return result1
        elif result2 != ''  and result1 == '':
            print("Google Speech Recognition thinks you said " + result2)
            return result2
        elif result1 != ''  and result2 != '':
            print("Google Speech Recognition thinks you said " + result1+','+result2)
            return result2
        else:
            return ''


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ''
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ''
