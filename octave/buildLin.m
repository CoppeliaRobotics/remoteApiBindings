% COMPILATION ON LINUX. HERE SOME USEFUL INFOS:
%
% Download and install Octave :
%
% $ sudo apt-add-repository ppa:octave/stable
% $ sudo apt-get update
% $ sudo apt-get install octave
% 
% and optionally, in order to compile the oct file yourself:
%
% $ sudo apt-get install octave-pkg-dev
%
% Read more here if needed:
% 1) it seems that mkoctfile can't work with relative directories.
% 2) (some say to put all files into the same directoy for compilation. Is that really necessary??)

% The compiler expects to have all source files in this directory. So copy and paste following files:
% - remote API source files (programming/remoteApi/*)
% - include files (programming/include/*)
%
% Then, in this directory, from the octave console, type "buildLin"

mkoctfile -DMAX_EXT_API_CONNECTIONS=255 -DNON_MATLAB_PARSING -DDO_NOT_USE_SHARED_MEMORY remApi.cc extApi.c extApiPlatform.c 
