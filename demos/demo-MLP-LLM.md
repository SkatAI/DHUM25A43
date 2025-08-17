# Demo

Analyze MLP arguments in her intervention yesterday on TF1

- download youtube video
https://www.youtube.com/watch?v=ol-eh9u5NOY

- extract audio
- transcribe audio
- identify locutor: speaker diarization
- extract arguments

# online LLM

## Download audio

```
I use yt-dlp to download a video on youtube
what is the CLI to only download the audio
```

Using ... claude, mistral, qwen

- claude
yt-dlp --extract-audio --list-formats https://www.youtube.com/watch?v=ol-eh9u5NOY
yt-dlp --extract-audio --audio-format mp3 https://www.youtube.com/watch?v=ol-eh9u5NOY -o "ol-eh9u5NOY.%(ext)s"

## transcribe audio, speaker diarization

the file is 11M large, can't upload it to an web chatbot

need to use an API


```
I have a mp3 file of the audio track of an interview
the audio is of good quality
I want to transcribe the audio making sure to separate the 2 locutors
How do I do that using an LLM accesible with Groq
```

Let's try with groq

### Claude

generates code that uses whisper, base model, free, for the audio to text transcription

but pip install does not work
probably a version problem

let's check with another LLM

Qwen

how to pip install whisper from openai



