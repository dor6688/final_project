from audios import audioTrainTest as aT
import os

#aT.featureAndTrain(["C:\siseusers\glazersh\Downloads\pyAudioAnalysis\pyAudioAnalysis\data\happy","C:\siseusers\glazersh\Downloads\pyAudioAnalysis\pyAudioAnalysis\data\sad", "C:\siseusers\glazersh\Downloads\pyAudioAnalysis\pyAudioAnalysis\data\\angry", "C:\siseusers\glazersh\Downloads\pyAudioAnalysis\pyAudioAnalysis\data\\calm", "C:\siseusers\glazersh\Downloads\pyAudioAnalysis\pyAudioAnalysis\data\\fearful", "C:\siseusers\glazersh\Downloads\pyAudioAnalysis\pyAudioAnalysis\data\\neutral"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "rf", "rfSMtemp", False)

path1 = r"C:\Users\dorlev.BGU-USERS\PycharmProjects\final_project\audios\tmp1.wav"


def predict_emotion_by_audio(path):
    os.chdir(r"C:\Users\dorlev.BGU-USERS\PycharmProjects\final_project\audios")
    print(aT.fileClassification(path, "svmSMtemp","svm"))
    print(aT.fileClassification(path, "knnSMtemp","knn"))

# predict_emotion_by_audio(path1)