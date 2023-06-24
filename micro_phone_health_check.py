import sounddevice as sd

def check_microphone():
    print("Checking microphone...")

    # Get the default microphone device ID
    device_id = sd.default.device[0]

    # Set the desired sample rate and duration for recording
    sample_rate = 44100
    duration = 3  # Recording duration in seconds

    # Start recording from the microphone
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, device=device_id)
    sd.wait()  # Wait for recording to complete

    # Play back the recorded audio
    print("Playing back recorded audio...")
    sd.play(audio_data, samplerate=sample_rate)
    sd.wait()  # Wait for playback to complete

    print("Microphone check complete.")

# Call the function to check the microphone
check_microphone()