7 October

1 AM: Just got back from a student party; let's get to work.

3:20 AM: Made a schematic for the LED matrix and column multiplexer; still have to figure out how to address the rows and how to give the LEDs values that create nice patterns

8 October

In this session, I actually figured out how I wanted this matrix to work, which is using an EEPROM that stores arbitrary images that you can switch to using dip switches
I had to get creative to make it work since a row of the 16x16 matrix doesn't fit cleanly into the 8 bits that get stored per address on the EEPROM, so I had to split the display in half using 2 buffer ICs and display only one half each clock cycle

I needed 2 binary counter ICs, one to make the crystal clock, as it seems like a clean way to accomplish that because it leaves signals for future control, like if I wanted to make the images switch automatically, I could use the unused 1 Hz and bigger signals to address the eeprom!

9 October

Designed the PCB and added a voltage regulator to turn 5V into 3.3V and made sure the traces could handle the current of the LEDs.
The only thing left is to write some code to program the EEPROM/example image dump of an EEPROM, and maybe if I figure it out, simulate the PCB to find errors that I've missed

9 October After Sleeping: Disaster

Realized I hadn't checked the current of the LEDs I used (they were too high) -> had to replace all LEDs and transistors because their current rating was wrong, meaning all the work I did yesterday was useless, and I have to do it all over again. This time I'm going to meticulously check each component for such things as my LEDs might need resistors now.

Added 15 ohm resistors per row because (3.3V - 3V) / 0.02 = 15 Ohm

Designed almost 50% of the PCB and made 15h reel

10 October 

Finished PCB wiring had to relocate the regulator region to make routing easier
Realized (using AI) that 74HC154 inverts the signal of the demultiplexers, so I need to use something else. 
Found some routing mistakes and swaps
Also, AI pointed out that my 15-ohm resistor placement is wrong and that the buffer IC can't directly drive the LEDs, so I'll also need to fix that
Fixed it now. I hope I'm done with the hard work. What's left is to write a program to return an image to be uploaded to the EEPROM using an Arduino or a programmer

Actually, AI found that I reversed the polarity of a capacitor and that I need to use pull-up resistors for my p-channel MOSFETs because controlling the output using the enable pin allows the gate to be floating, but I'm not sure there shouldn't be any more issues

Need 2 74HC595 to programm EEPROM with what i have

My outline for the programmer App:

Python scans folder for numbered BMP images gray scales them and then sets bit value based on brightness to on or off and Dumps a output.bin file to be programmed onto the EEPROM