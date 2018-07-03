## How to install

### Make program executable

run `sudo chmod +x dlytv` so that this program can be executed.

### Add this folder to your PATH.

```
export PATH="blah/blah:$PATH"
```

### install reqs

The program uses Python3 and so use pip3 to install the requirements. 

```
pip3 install -r ./requirements.txt
```


## How to Use

dlytv : use this program with any number of urls.  Ie

```
dlytv https://www.youtube.com/watch?v=Hy8kmNEo1i8
```

This will download an mp4 into the cwd the command is called from.

To convert the mp4 to an mp3 use

```
ffmpeg -i <mp4 file name> -f mp3 -ab 192000 -vn <output name>
```

