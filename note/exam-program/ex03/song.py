from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

infiles = ['song1.wav', 'song2.wav', 'song3.wav']
outfile = "song.wav"

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.html)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name=outfile, seconds=2):
    """Write the output of a sampler function as a wav file.
    (See https://docs.python.org/3/library/wave.html)
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def tri(frequency, amplitude=0.3):
    """A continuous triangle wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

def both(f, g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start or seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

def mario_at(octave):
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq), tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    z += 1/2
    return song

song = mario_at(1)
play(song, name='song1.wav')
song = mario_at(1/2)
play(song, name='song2.wav')
song = both(mario_at(1), mario_at(1/2))
play(song, name='song3.wav')

def append_songs(infile, append_file, start = 0, end = -1, outfilename = "song.wav"):
    w = open(infile, "rb")
    data = [w.getparams(), w.readframes(w.getnframes())]
    w.close()
    w = open(append_file, "rb")
    tmp = w.readframes(w.getnframes())
    parms = w.getparams();
    start_frame = int(start * parms.framerate)
    if end == -1:
        end_frame = parms.nframes
    else:
        end_frame = int(end * parms.framerate)
    tmp = tmp[start_frame:end_frame]
    data2 = [parms, tmp]
    w.close()
    output = open(outfilename, "wb")
    output.setparams(data[0])
    output.writeframes(data[1])
    output.writeframes(data2[1])
    output.close()

# data = []
# for infile in infiles:
#     w = open(infile, "rb")
#     data.append([w.getparams(), w.readframes(w.getnframes())])
#     w.close()

# output = open(outfile, "wb")
# output.setparams(data[0][0])
# output.writeframes(data[0][1])
# output.writeframes(data[1][1])
# output.writeframes(data[2][1])
# output.close()

append_songs("song1.wav", "song2.wav", 0, 2, "song.wav")
append_songs("song.wav", "song3.wav", 0, 2, "song.wav")
append_songs("song.wav", "song1.wav", 0, 2, "song.wav")
