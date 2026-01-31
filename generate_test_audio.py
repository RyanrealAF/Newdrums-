import numpy as np
import scipy.io.wavfile as wav

def generate_test_audio(filename='test_audio.wav', duration=2.0, sr=22050):
    t = np.linspace(0, duration, int(sr * duration))
    # Generate 4 pulses at 0.5s, 1.0s, 1.5s, 2.0s
    y = np.zeros_like(t)
    for onset in [0.5, 1.0, 1.5]:
        idx = int(onset * sr)
        y[idx:idx+100] = 0.8  # Sharp pulse

    # Add some noise to simulate a real track
    y += 0.01 * np.random.randn(len(t))

    wav.write(filename, sr, (y * 32767).astype(np.int16))
    print(f"Generated {filename}")

if __name__ == "__main__":
    generate_test_audio()
