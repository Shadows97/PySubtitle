import speech_recognition as sr
from googletrans import Translator

import os

from pydub import AudioSegment
from pydub.silence import split_on_silence
import pipes
from webvtt import WebVTT, Caption
from moviepy.editor import *


def getTime(milli):
    seconds = (milli / 1000) % 60
    minutes = (milli / (1000 * 60)) % 60
    hours = (milli / (1000 * 60 * 60)) % 24
    result = "00:00"
    if seconds < 10 and minutes < 10:
        result = "0%d:0%d" % (minutes, seconds)
    elif seconds >= 10 and minutes < 10:
        result = "0%d:%d" % (minutes, seconds)
    elif seconds < 10 and minutes >= 10:
        result = "%d:0%d" % (minutes, seconds)
    elif seconds >= 10 and minutes >= 10:
        result = "%d:%d" % (minutes, seconds)
    return result
    print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


def splitter(src, dest, subDest, fileName, audioFolder):
    # Input audio file to be sliced
    vttEn = WebVTT()
    # vttFr = WebVTT()
    # translator = Translator()
    audio = AudioSegment.from_wav(src)

    # Length of the audiofile in milliseconds
    n = len(audio)

    # Variable to count the number of sliced chunks
    counter = 1

    # Text file to write the recognized audio
    fh = open("recognized.txt", "w+")

    # Interval length at which to slice the audio file.
    # If length is 22 seconds, and interval is 5 seconds,
    interval = 8 * 1000

    # Length of audio to overlap.
    # If length is 22 seconds, and interval is 5 seconds,
    # With overlap as 1.5 seconds,
    overlap = 0  # 1.5 * 1000

    # Initialize start and end seconds to 0
    start = 0
    end = 0

    # Flag to keep track of end of file.
    # When audio reaches its end, flag is set to 1 and we break
    flag = 0

    # Iterate from 0 to end of the file,
    # with increment = interval
    for i in range(0, 2 * n, interval):

        # During first iteration,
        # start is 0, end is the interval
        if i == 0:
            start = 0
            end = interval

            # All other iterations,
        # start is the previous end - overlap
        # end becomes end + interval
        else:
            start = end - overlap
            end = start + interval

            # When end becomes greater than the file length,
        # end is set to the file length
        # flag is set to 1 to indicate break.
        if end >= n:
            end = n
            flag = 1

        # Storing audio file from the defined start to end
        chunk = audio[start:end]

        # Filename / Path to store the sliced audio
        filename = dest + 'chunk' + str(counter) + '.wav'

        # Store the sliced audio file to the defined path
        chunk.export(filename, format="wav")
        # Print information about the current chunk
        print("Processing chunk " + str(counter) + ". Start = "
              + str(start) + " end = " + str(end))

        # Increment counter for the next chunk
        counter = counter + 1

        # Slicing of the audio file is done.
        # Skip the below steps if there is some other usage
        # for the sliced audio files.

        # Specify the audio file to recognize

        AUDIO_FILE = filename

        # Initialize the recognizer
        r = sr.Recognizer()

        # Traverse the audio file and listen to the audio
        with sr.AudioFile(AUDIO_FILE) as source:
            audio_listened = r.listen(source)

            # Try to recognize the listened audio
        # And catch expections.
        try:
            rec = r.recognize_google(audio_listened)

            # If recognized, write into the file.
            captionEn = Caption('00:{0}.000'.format(getTime(start)),'00:{0}.000'.format(getTime(end)),rec)
            # recFr = translator.translate(rec, dest='fr')
            # captionFr = Caption(
            #     '00:{0}.000'.format(getTime(start)),
            #     '00:{0}.000'.format(getTime(end)),
            #     recFr.text)

            vttEn.captions.append(captionEn)
            # vttFr.captions.append(captionFr)
            fh.write(rec + ". \n ")

            # If google could not understand the audio
        except sr.UnknownValueError:
            print("Could not understand audio")

            # If the results cannot be requested from Google.
        # Probably an internet connection error.
        except sr.RequestError as e:
            print("Could not request results.")

            # Check for flag.
        # If flag is 1, end of the whole audio reached.
        # Close the file and break.
        if flag == 1:
            fh.close()
            vttEn.save(subDest + fileName + '.en.vtt')
            # vttFr.save(subDest + fileName + '.fr.vtt')
            deleteAllFile(dest)
            deleteAllFile(audioFolder)
            break


def silence_based_conversion(path):
    # open the audio file stored in
    # the local system as a wav file.
    song = AudioSegment.from_wav(path)

    # open a file where we will concatenate
    # and store the recognized text
    fh = open("recognized.txt", "w+")

    # split track where silence is 0.5 seconds
    # or more and get chunks
    chunks = split_on_silence(song,
                              # must be silent for at least 0.5 seconds
                              # or 500 ms. adjust this value based on user
                              # requirement. if the speaker stays silent for
                              # longer, increase this value. else, decrease it.
                              min_silence_len=100,

                              # consider it silent if quieter than -16 dBFS
                              # adjust this per requirement
                              silence_thresh=-16
                              )

    # create a directory to store the audio chunks.
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass

    # move into the directory to
    # store the audio files.
    os.chdir('audio_chunks')

    i = 0
    # process each chunk
    for chunk in chunks:

        # Create 0.5 seconds silence chunk
        chunk_silent = AudioSegment.silent(duration=10)

        # add 0.5 sec silence to beginning and
        # end of audio chunk. This is done so that
        # it doesn't seem abruptly sliced.
        audio_chunk = chunk_silent + chunk + chunk_silent

        # export audio chunk and save it in
        # the current directory.
        print("saving chunk{0}.wav".format(i))
        # specify the bitrate to be 192 k
        audio_chunk.export("./chunk{0}.wav".format(i), bitrate='192k', format="wav")

        # the name of the newly created chunk
        filename = 'chunk' + str(i) + '.wav'

        print("Processing chunk " + str(i))

        # get the name of the newly created chunk
        # in the AUDIO_FILE variable for later use.
        file = filename

        # create a speech recognition object
        r = sr.Recognizer()

        # recognize the chunk
        with sr.AudioFile(file) as source:
            # remove this if it is not working
            # correctly.
            r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)

        try:
            # try converting it to text
            rec = r.recognize_google(audio_listened, language="en-US")
            # write the output to the file.
            fh.write(rec + ". ")

            # catch any errors.
        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results. check your internet connection")

        i += 1

    os.chdir('..')


def video_to_audio(fileName, destination):
    try:
        file, file_extension = os.path.splitext(fileName)
        file = pipes.quote(fileName)
        print("file")
        print(file)
        video_to_wav = 'ffmpeg -i ' + file  + ' ' + destination + '.wav'
        final_audio = 'lame ' + destination + '.wav' + ' ' + file + '.mp3'
        os.system(video_to_wav)
        os.system(final_audio)
        file = pipes.quote(file)
        os.remove(file + '.mp3')
        print("sucessfully converted ", fileName, " into audio!")
    except OSError as err:
        print(err)
        exit(1)


def getFileList(source):
    return [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]


def deleteAllFile(src):
    files = getFileList(src)
    for file in files:
        os.remove(src + file)


def getFileWithoutSub(src):
    files = getFileList(src)
    result = []
    for vid in files:
        test = vid.split('.')[0] + '.en.vtt'
        if test not in files:
            os.rename(src + vid, src + vid.replace(' ', '_'))
            vid = vid.replace(' ', '_')
            result.append(vid)
    print(result)
    return result


sourceFolder = os.getcwd() + '/media/videos/'
destinationFolder = os.getcwd() + '/media/audio/'
splitFolder = os.getcwd() + '/media/splits/'
onlyfiles = getFileWithoutSub(sourceFolder)
print(sourceFolder)
print(onlyfiles)
for file in onlyfiles:
    destination, file_extension = os.path.splitext(destinationFolder + file)
    video_to_audio(sourceFolder + file, destination)
    # silence_based_conversion(destination + '.wav')
    splitter(destination + '.wav', splitFolder, sourceFolder, file.split('.')[0], destinationFolder)

