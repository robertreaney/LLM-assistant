def speech_to_text(input_file='output.wav'):
    try:
        from huggingsound import SpeechRecognitionModel

        model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english")

        transcriptions = model.transcribe([input_file])

        return transcriptions
    except:
        # this is so we dont crash on windows machines that dont have this library installed
        pass