7 October

1 AM: Just got back from Studentparty lets get To work

3:20 AM: Made schematic for LED matrix and column multolexer still have to figure out how to adress the rows and how give the leds values that create nice patterns

8 October

In this session, I actually figured out how I wanted this matrix to work, which is using an EEPROM.

that stores arbitrary images that you can switch to using dip switches
I had to get creative to make it work since a row of the 16x16 matrix doesn't fit cleanly into the 8 bits that get stored per address on the EEPROM, so I had to split the display in half using 2 buffer ICs and display only one half each clock cycle

I needed 2 binary counter ICs, one to make the crystal clock, as it seems like a clean way to accomplish that because it leaves signals for future control, like if I wanted to make the images switch automatically, I could use the unused 1 Hz and bigger signals to address the eeprom!

9 October

Designed the PCB and added a voltage regulator to turn 5V into 3.3V and made sure the traces could handle the current of the LEDs.
The only thing left is to write some code to program the EEPROM/example image dump of an EEPROM, and maybe if I figure it out, simulate the PCB to find errors that I've missed

9 October After Sleeping: Disaster

Realized I hadn't checked the current of the LEDs I used (they were too high) -> had to replace all LEDs and transistors because their current rating was wrong, meaning all the work I did yesterday was useless, and I have to do it all over again. This time I'm going to meticulously check each component for such things my LEDs might need resistors now.

added 15 ohm resistors per row because (3.3V - 3V) / 0.02 = 15 Ohm

Designed almost 50% of the PCB and made 15h reel