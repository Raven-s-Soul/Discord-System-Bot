# Discord-System-Bot

## PyNaCl needed for join channel, FFmpeg for play audio

### replit.nix:
#### { pkgs }: {
####   deps = 
    [pkgs.python310Full
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
    pkgs.ffmpeg.bin];
####   env = 
    {PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
    # Needed for pandas / numpy
    pkgs.stdenv.cc.cc.lib
    pkgs.zlib
    # Needed for pygame
    pkgs.glib
    # Needed for matplotlib
    pkgs.xorg.libX11
    # ffmpeg
    pkgs.libopus    ];
    PYTHONHOME = "${pkgs.python310Full}";
    PYTHONBIN = "${pkgs.python310Full}/bin/python3.10";
    LANG = "en_US.UTF-8";
    STDERREDBIN = "${pkgs.replitPackages.stderred}/bin/stderred";
    PRYBAR_PYTHON_BIN = "${pkgs.replitPackages.prybar-python310}/bin/prybar-python310";};}
