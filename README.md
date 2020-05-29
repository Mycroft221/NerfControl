This project is for enabling/disabling all nerf guns in the house using microcontrollers and WiFi!

It has 3 parts:
1. server running the API service that keeps track of the current status (enabled or disabled) and accepts requests to change the status
2. microcontroller on each nerf gun running the MicroPython Nerf program that reads the current status from the server every 100ms and physcially disconnects power to the toy or moves a servo to block the barrel
3. optional website to simplify interaction with the REST API service on the server

The API service is in the API folder. A prebuilt JAR can be found in API/target/rest-service-0.0.1-SNAPSHOT. This can be run on anything with java installed, including raspberry pis, laptop computers, and even cell phones.

The microcontroller code is designed for the WeMos D1 ESP8266 board. It should work on any MicroPython board with WiFi with some changes to the output pin assignments.

The website can be used locally by opening the HTML file in a browser such as Chrome or hosted using an apache web server.

I've enjoyed building this solution, and it has brough much peace during critical times when I don't want to get hit with Nerf darts. I hope you'll like it too!
