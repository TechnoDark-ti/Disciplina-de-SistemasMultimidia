import sounddevice as sd
import soundfile as sf
import librosa
import librosa.display
import matplotlib.pyplot as plt

def showAudio(escolha):
    print("Escolha uma opção:")
    print("1. Tocar áudio")
    print("2. Gravar áudio do microfone")
    print("3. Visualizar forma de onda")
    print("4. Sair")
    escolha = input("Digite sua opção: ")

    if escolha == '1':
        tocarAudio()
    elif escolha == '2':
        gravarAudioMicrofone()
    elif escolha == '3':
        visualizarFormaOnda()
    elif escolha == '4':
        break
    else:
        print("Opção inválida! Tente novamente.")


def tocarAudio():
    try:
        data, fs = sf.read('gravacao.wav')
        sd.play(data, samplerate=fs)
        sd.wait()
    except FileNotFoundError:
        print("Arquivo 'gravacao.wav' não encontrado!")

def gravarAudioMicrofone():
    try:
        duracao = 5
        fs = 44100
        print("Gravando...")
        gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
        sd.wait()
        print("Gravação concluída!")
        sf.write('gravacao.wav', gravacao, fs)
    except Exception as e:
        print(f"Erro ao gravar: {e}")

def visualizarFormaOnda():
    # Carregar o áudio
    y, sr = librosa.load('gravacao.wav')
    # Visualizar waveform
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Forma de Onda')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.show()