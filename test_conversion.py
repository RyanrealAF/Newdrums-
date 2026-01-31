import os
import subprocess
import mido

def test_conversion():
    input_audio = 'test_audio.wav'
    output_midi = 'test_output.mid'

    # Ensure input audio exists
    if not os.path.exists(input_audio):
        print("Input audio not found, generating...")
        import generate_test_audio
        generate_test_audio.generate_test_audio(input_audio)

    # Run the script
    cmd = ['python', 'audio_to_midi.py', input_audio, '--output', output_midi, '--bpm', '120']
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("Conversion failed!")
        print(result.stderr)
        return False

    # Check if output exists
    if not os.path.exists(output_midi):
        print("Output MIDI not found!")
        return False

    # Verify MIDI content
    try:
        mid = mido.MidiFile(output_midi)
        num_notes = 0
        for track in mid.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    num_notes += 1
        print(f"MIDI file verified. Found {num_notes} notes.")
        if num_notes > 0:
            return True
        else:
            print("No notes found in MIDI file.")
            return False
    except Exception as e:
        print(f"Error reading MIDI: {e}")
        return False

if __name__ == "__main__":
    if test_conversion():
        print("Test PASSED")
    else:
        print("Test FAILED")
        exit(1)
