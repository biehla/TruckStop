
clear
% When running the script the first time make sure the phone screen stays
% on and the phone also connects to the server being setup

% Use the command below to begin local hosting a server for the phone
% connector on canada;

% Set up mobile device
m = mobiledev;

% Enable Position Sensors
m.PositionSensorEnabled = 1;

% Start Logging
m.Logging = 1;

pause(20);

m.Logging =0;

% The position 
[lat,lon,t,spd] = poslog(m);

m.PositionSensorEnable = 0;







