from huggingsound import SpeechRecognitionModel

def speech_to_text(input_file='output.wav'):
    model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english")
    transcriptions = model.transcribe([input_file])
    return transcriptions
