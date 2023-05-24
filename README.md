# Discord-System-Bot

PyNaCl needed for join channel
FFmpeg for play audio

replit.nix:
{ pkgs }: {
  deps = [
    pkgs.python310Full
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
    pkgs.ffmpeg.bin
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
      #ffmpeg
      pkgs.libopus
    ];
    PYTHONHOME = "${pkgs.python310Full}";
    PYTHONBIN = "${pkgs.python310Full}/bin/python3.10";
    LANG = "en_US.UTF-8";
    STDERREDBIN = "${pkgs.replitPackages.stderred}/bin/stderred";
    PRYBAR_PYTHON_BIN = "${pkgs.replitPackages.prybar-python310}/bin/prybar-python310";
  };
}

pip list
Package                  Version
------------------------ -----------
aiohttp                  3.8.4
aiosignal                1.3.1
argon2-cffi              21.3.0
argon2-cffi-bindings     21.2.0
async-timeout            4.0.2
attrs                    22.2.0
brotli                   1.0.9
cachecontrol             0.12.11
cachy                    0.3.0
certifi                  2023.5.7
cffi                     1.15.1
charset-normalizer       3.0.1
cleo                     0.8.1
click                    8.1.3
clikit                   0.6.2
crashtest                0.3.1
cryptography             38.0.4
debugpy                  1.6.5
discord                  2.2.2
discord-py               2.2.2
distlib                  0.3.6
ffmpeg                   1.4
filelock                 3.9.0
flask                    2.2.3
frozenlist               1.3.3
html5lib                 1.1
idna                     3.4
iso8601                  1.1.0
itsdangerous             2.1.2
jedi                     0.18.2
jeepney                  0.8.0
jinja2                   3.1.2
keyring                  21.8.0
lockfile                 0.12.2
markupsafe               2.1.2
msgpack                  1.0.4
multidict                6.0.4
mutagen                  1.46.0
numpy                    1.24.1
packaging                23.0
parso                    0.8.3
passlib                  1.7.4
pastel                   0.2.1
pexpect                  4.8.0
pip                      22.2.2
pkginfo                  1.9.6
platformdirs             2.6.2
pluggy                   1.0.0
poetry                   1.1.11
poetry-core              1.0.8
protobuf                 4.21.12
ptyprocess               0.7.0
pycparser                2.21
pycryptodomex            3.18.0
pyflakes                 2.5.0
pylev                    1.4.0
pynacl                   1.5.0
pyparsing                3.0.9
pyseto                   1.7.0
python-lsp-jsonrpc       1.0.0
pytoolconfig             1.2.4
replit                   3.2.5
replit-python-lsp-server 1.15.9
requests                 2.28.2
requests-toolbelt        0.9.1
rope                     1.7.0
secretstorage            3.3.3
setuptools               63.2.0
shellingham              1.5.0.post1
six                      1.16.0
toml                     0.10.2
tomli                    2.0.1
tomlkit                  0.11.6
typing-extensions        3.10.0.2
ujson                    5.7.0
urllib3                  1.26.14
virtualenv               20.17.1
webencodings             0.5.1
websockets               11.0.3
werkzeug                 2.2.3
whatthepatch             1.0.3
yapf                     0.32.0
yarl                     1.8.2
yt-dlp                   2023.3.4