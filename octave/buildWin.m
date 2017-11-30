% COMPILATION ON WINDOWS.
%
% The compiler expects to have all source files in one directory. So copy and paste following files:
% - remote API source files (programming/remoteApi/*)
% - include files (programming/include/*)
%
% Then do something like:
%
% "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x64
% mkoctfile -DMAX_EXT_API_CONNECTIONS=255 -DNON_MATLAB_PARSING -DDO_NOT_USE_SHARED_MEMORY -lwinmm -lWs2_32 remApi.cc extApi.c extApiPlatform.c
%

