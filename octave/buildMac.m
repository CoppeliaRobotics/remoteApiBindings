% COMPILATION ON MAC. HERE SOME USEFUL INFOS:
%
% Install via Fink or homebrew. Good luck with that!
%
% Read more here if needed:
%
% http://www.gnu.org/software/octave/download.html
% http://wiki.octave.org/Octave_for_MacOS_X 
% http://ntraft.com/getting-octave-to-work-on-mountain-lion/
% http://stackoverflow.com/questions/16445098/how-can-i-install-gnu-octave-on-mac-with-fink
% http://octave.1599824.n4.nabble.com/missing-mkoctfile-3-6-3-on-OS-X-td4647526.html
% http://www.weescribble.com/technology-menu/138-fixing-fontconfig-warning-for-octave-on-osx

% 1) it seems that mkoctfile can't work with relative directories.
% 2) (some say to put all files into the same directoy for compilation. Is that really necessary??)

% The compiler expects to have all source files in this directory. So copy and paste following files:
% - remote API source files (programming/remoteApi/*)
% - include files (programming/include/*)
%
% Then, in this directory, from the octave console, type "buildMac"

mkoctfile -DMAX_EXT_API_CONNECTIONS=255 -DNON_MATLAB_PARSING -DDO_NOT_USE_SHARED_MEMORY remApi.cc extApi.c extApiPlatform.c 
