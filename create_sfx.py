import wave, struct, math, os

# Folder for assets
ASSET_PATH = "assets"
os.makedirs(ASSET_PATH, exist_ok=True)

def make_wave(filename, freq=440.0, duration=0.2, volume=0.5):
    framerate = 44100
    amplitude = int(32767 * volume)
    nframes = int(framerate * duration)

    with wave.open(os.path.join(ASSET_PATH, filename), "w") as wav_file:
        wav_file.setnchannels(1)         # mono
        wav_file.setsampwidth(2)         # 16-bit
        wav_file.setframerate(framerate)

        for i in range(nframes):
            value = int(amplitude * math.sin(2 * math.pi * freq * i / framerate))
            wav_file.writeframes(struct.pack('<h', value))

    print(f"✅ Created {filename}")

# Generate sounds
make_wave("flap.wav", freq=440, duration=0.15)   # flap sound
make_wave("point.wav", freq=1000, duration=0.15) # point sound
make_wave("hit.wav", freq=200, duration=0.3)     # hit sound

