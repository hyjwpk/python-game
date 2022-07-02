import speech_recognition as sr


def find(target):
    list = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    for index, value in enumerate(list):
        if value == target:
            return index
    return None


def convert(result):
    result = (str(str(result.split('"text" : ')[1]).split('"')[1])).split(' ')
    if len(result) == 1:
        return find(result[0])
    elif len(result) == 2:
        if result[0] == '十':
            return 10 + find(result[1])
        elif result[1] == '十':
            return find(result[0]) * 10
        elif result[1] == '百':
            return find(result[0]) * 100
    elif len(result) == 3:
        if result[1] == '十':
            return find(result[0]) * 10 + find(result[2])
    elif len(result) == 4:
        if result[1] == '百' and result[2] == '零':
            return find(result[0]) * 100 + find(result[3])
        if result[1] == '百' and result[3] == '十':
            return find(result[0]) * 100 + find(result[2])*10
    elif len(result) == 5:
        if result[1] == '百' and result[3] == '十':
            return find(result[0]) * 100 + find(result[2])*10 + find(result[4])
    return 'error'


def recognition():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Vosk
    try:
        result = convert(r.recognize_vosk(audio))
        print(result)
        return str(result)
    except sr.UnknownValueError:
        print("Vosk could not understand audio")
    except sr.RequestError as e:
        print("Vosk error; {0}".format(e))
