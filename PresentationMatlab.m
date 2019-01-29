clear
% When running the script the first time make sure the phone screen stays
% on and the phone also connects to the server being setup

% Use the command below to begin local hosting a server for the phone
% connector on canada;

% Set up mobile device
m = mobiledev;

% Enable Position Sensors
m.AccelerationSensorEnabled = 1;

% Start Logging
m.Logging = 1;

fileID = fopen('C:\xampp\htdocs\earlyWarning.json', 'w');

while true
    acceleration = accellog(m);
    if size(acceleration) > 1
        if abs(acceleration(end,1)) > 4
            pause(2);
            fprintf(fileID, '{"moved":"true"}');
            break;
        end
    end
end

m.Logging = 0;

m.AccelerationSensorEnabled = 0;

clear m;


%% Actual Implementation using position data insead and could also suppliment the usage of google API and data maps

% 
% clear
% % When running the script the first time make sure the phone screen stays
% % on and the phone also connects to the server being setup
% 
% % Use the command below to begin local hosting a server for the phone
% % connector on canada;
% 
% % Set up mobile device
% n = mobiledev;
% 
% % Enable Position Sensors
% n.PositionSensorEnabled = 1;
% 
% 
% % Start Logging
% n.Logging = 1;
% 
% pause(20);
% 
% % The position 
% [lat,lon,t,spd] = poslog(n);


% n.PositionSensorEnable = 0;







