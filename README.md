
# TruckStop

A DeltaHacks Project (24 Hour McMaster Univerisity Hackaton)

A clean, scalable, and realistic solution towards reducing cargo theft

From the client who generously provided data we noted that all cargo trucks have GPS trackers on the cargo and the trailler, but require an early warning system when cargo is potentially being stolen.

We can assume that the drivers are to have phones on them at all times which can be tracked as well (fully charged with data).

## Solution

This solution utilizes the GPS trackers on the phone, trailler, and cargo utilizing their average relative speed to determine whether of not the cargo has potentillty been stolen.

For any time a driver is set out on a delivery we only have 4 cases:

* Phone is Moving || Cargo is Moving (speed are within a specific threshold) *OKAY*
* Phone is Moving || Cargo is Stationary (position of driver and cargo are within specific threshold) *OKAY*
* Phone is Stationary || Cargo is Stationary *OKAY*
* Phone is Stationary || Cargo is Moving (Speed of truck is much faster than phone) *SEND ALERT*

If any time the truck is stored in storage and is found to be moving then an alert is sent automatically

## Why This is Better?

The GPS data of the phone and trucks are always being tracked anyway so in no way is this solution invasive.

* The solution is better as it makes sure it does not affect the lives of any drivers as this solution is all controlled from the backend.
* This provides additional security against comprimised drivers
* Completely **Free**: All the data and trackers already exists so the solution is all sofware based
* Makes sure to contine tracking the truck and cargo in the event of a GPS jammer using the accelerometer and gyroscope
* Simple: The problem was noted to cost 4 Billion Dollars, so this solution targets the core issues present when cargo gets hijacked to better provide an early warning

## Demo

In this demo we have utilized matlab for telementary as the backend, then using apache to host an HTML server for the front end, and Javascipt will bridge between the front and back end.

Note: For this demo one would require to install Matlab Mobile on a phone that can be trakced by GPS and has an accelerometer.

Since we had to demo inside a small space we had to use the acceleration as the speed or position by gps would not be accurate. So for the demo we check if the accleration of the phone is much much greater than zero.

The idea is that the laptop where the code is being run on is the phone of the driver, and the phone with Matlab Mobile is the cargo which is accelerating away.

Additionally we have tracked the data point and plotted them using python's matlibplot library to visualize where all the data is located on a map.

![Plotted Coordinates](PlottedData.png)

One can go through the raw data in the data set zip or the formatted data in Data_From_Cargo.csv.

## Cheers