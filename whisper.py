import whisper
# pip install openai-whisper

def transcribe_with_whisper(input_file, output_dir):
    # Load the Whisper model (large-v3 in this case)
    model = whisper.load_model("large-v3")
    
    # Perform transcription
    result = model.transcribe(
        input_file,
        language="en",
        word_timestamps=True,
    )
    
    # Extract the transcription text and word timestamps
    transcribed_text = result["text"]
    segments = result["segments"]
    
    # Save to an SRT file (as specified in the original parameters)
    srt_file = f"{output_dir}/output.srt"
    with open(srt_file, "w") as f:
        for idx, segment in enumerate(segments):
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"]
            
            # Convert start and end times to SRT time format (HH:MM:SS,MS)
            start_time_srt = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02},{int((start_time * 1000) % 1000):03}"
            end_time_srt = f"{int(end_time // 3600):02}:{int((end_time % 3600) // 60):02}:{int(end_time % 60):02},{int((end_time * 1000) % 1000):03}"
            
            # Write the segment to the SRT file
            f.write(f"{idx + 1}\n")
            f.write(f"{start_time_srt} --> {end_time_srt}\n")
            f.write(f"{text}\n\n")
    
    print(f"Transcription saved to: {srt_file}")

# Example usage
input_audio_file = "test.wav"
output_directory = "/Users/alexreute/Desktop/CC"
transcribe_with_whisper(input_audio_file, output_directory)
