import azure.cognitiveservices.speech as speechsdk
class AISpeech:
   
    def __init__(self, speech_key:str, service_region:str, voice_name:str):
        self.speech_key = speech_key
        self.service_region = service_region
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # 読み上げさせる音声ライブラリ名
        self.speech_config.speech_synthesis_voice_name = voice_name
    # Speechシンセサイザの作成
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config)   
    
    def text_to_speech(self,text:str):
    # 音声で読み上げ
        self.speech_synthesizer.speak_text_async(text)

    def speechSSML(self, ssml: str):
        self.speech_synthesizer.speak_ssml_async(ssml).get()
        
    def genSSML(self, voice_name: str, volume: int, text: str):
            txt = f"""
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="ja-JP">
        <voice name="{voice_name}" effect="eq_car">
        <prosody volume="+{volume:.2f}%">{text}</prosody>
        </voice>
        </speak>
        """
            return txt