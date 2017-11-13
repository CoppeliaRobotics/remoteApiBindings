% COMPILATION ON WINDOWS. HERE SOME USEFUL INFOS:
%
% Download and install Octave for MSVC2010 from here:
%
% http://sourceforge.net/projects/octave/files/Octave%20Windows%20binaries/Octave%203.6.4%20for%20Windows%20Microsoft%20Visual%20Studio/
%
% To start Octave, use following code in a batch file:
%
% call "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\vcvarsall.bat"
% C:\Software\Octave-3.6.4\bin\octave.exe -i
%
% You might also have to make sure that folder Octave-3.6.4 is in Windows path variable
%
% Then, you might have to change the following line of file: Octave-3.6.4\include\math.h (line 74):
% from: #include <c:/Program Files/Microsoft Visual Studio 10.0/VC/include/math.h>
% to: #include <c:/Program Files (x86)/Microsoft Visual Studio 10.0/VC/include/math.h>
%
% Read more here if needed:
% 1) http://octave.1599824.n4.nabble.com/unable-to-find-mkoctfile-in-expected-location-td4655586.html
% 2) http://wiki.octave.org/Octave_for_Windows#Using_the_Visual_C.2B.2B_compiler_with_Octave
% 3) -i is needed when starting Octave, otherwise Octave crashes at each syntax error
% 4) it seems that mkoctfile can't work with relative directories.
% 5) (some say to put all files into the same directoy for compilation. Is that really necessary??)

% The compiler expects to have all source files in this directory. So copy and paste following files:
% - remote API source files (programming/remoteApi/*)
% - include files (programming/include/*)
%
% Then, in this directory, from the octave console, type "buildWin"

mkoctfile -DMAX_EXT_API_CONNECTIONS=255 -DNON_MATLAB_PARSING -DDO_NOT_USE_SHARED_MEMORY -lwinmm -lWs2_32 remApi.cc extApi.c extApiPlatform.c 
