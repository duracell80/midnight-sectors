# Midnight Sectors (Readable OctaDecimal Hybrid)
Time is messy and decimal time tricky. Midnight sectors is a decimal / hectosecond based unit of time measurement somewhere between Base 10 and Base 8 and somewhat relatable to the mundane sex·a·ges·i·mal system. It is a local and relative alternative to Swatch internet time (BMT) set around the calculation of 86,400 seconds per day thus a day will start at midnight @000 and end at midnight @864. Does this replace standard time? No, it's an overlay, the math underneath is about as Babylonian as David Grey at a traffic light. 

Throwback Thursday: https://www.youtube.com/watch?v=zI_SBAkdKzc

#### The Martian Time-Slip
See the end of this README.md transmission.

### Overall goal: Make decimal minutes and seconds eaiser to relate to ...
This proposal lays out a hybrid between the two opposing systems, keeping a 7 day week, spliting the day into 8 (chunks * ) and again into 4 (periods). It stops short of 10 hours, because that's just confusing!! (*) a 9th "hour" is needed for the remaining 64 sectors.

The @time is readable on an octal clock!
![Octahedron as net](https://raw.githubusercontent.com/duracell80/midnight-sectors/main/docs/images/octahedron_net.svg)

#### Application in real life
- A 3min 33s pop song = 2 sectors and 13 deconds (00:03:33 = 00:02:13)
- A 2 hour movie = 85 sectors and 71 deconds or 0.85 hedrons (02:00:00 = 00:85:71)
- A 45 minute bus ride takes 32 sectors and 14 deconds (00:45:00 = 00:32:14)

#### Terms For The Day
- Lumin (A whole of 864 sectors = 1 day of 24 hours, lumen = light, day is light)
- Segment (Octal division of the day into 8.64 parts of up to 100 sectors each)
- Period (A period denotes 4 periods of time within the lumin [NAME])

#### Lumin Periods:
- [N] = Night
- [A] = Afternoon
- [M] = Morning
- [E] = Evening

Ever noticed how it's not entirely clear how AM/PM denotes evening and morning? Before noon and after noon both relate to periods of time that don't relate to if it's day or night. 12pm is the brighest part of the day but 11pm is usually not daylight. It's not possible to look at a clock and know innately if it's night or day. Worse a dial interface doesn't rotate 360 degrees once, but TWICE and contains no AM/PM context! Are we in the first 360 rotation or second?

This is a problem, a generation is not able to read a dial clock face! How could they? 11 means 5 to something and 11 o'something at night and 11 o'something at day? How strange.
https://www.youtube.com/watch?v=PIe2auW9EMI

#### Terms for Hours, Minutes and Seconds
- Hedron  (A hedron (face with hands) is the second part of the word Octahedron, seems like a large measure)
- Sector  (A sector (minute) contains = 1 minute and 40 seconds or 100 decimalizable* seconds)
- Decond  (The way to think of an extended second, or hectosecond)
- Tick    (An odd  .decond)
- Tock    (An even .decond)
- SSM     (The number of whole single sectors of 100 deconds, since midnight)
- STM     (The number of whole single sectors of 100 sdeconds, til midnight)
- Range   (The progression of day from 0 to 100% clockwise in linear left to right motion)

Look at that! He:Se:De ... just like HH:MM:SS!

(*) decimalizable should be a word.

#### Terms for Periods:
Why only two (am/pm)? Let's double up and describe night and evening.

- Night     - nox (nx) *night crossing
- Afternoon - post meridiem (pm)
- Morning   - antemeridies (am)
- Evening   - noc (nc) *night coming

#### Hedrons with Latin Names:
There are 8 hedrons or hours in the day (technically the 9th to hold the final 64 sectors), named in latin for their boundary. A hedron defines 100 sectors (there are 100 minutes in an hour).

- Hedron 0 (@000 to @100) - venti (all computer scientists drink coffee at night, I assume)
- Hedron 1 (@100 to @200) - centumi
- Hedron 2 (@200 to @300) - ducenti
- Hedron 3 (@300 to @400) - trecenti
- Hedron 4 (@400 to @500) - quadrigenti
- Hedron 5 (@500 to @600) - quingenti
- Hedron 6 (@600 to @700) - sescenti
- Hedron 7 (@700 to @800) - septingenti
- Hedron 10 (@800 The remaining 64) - octingenti

Hedron 8 and 9 cannot exist in base 8, totally not confusing, October is the 10th month (instead of Decotober), see time is messy. 64 is divisible by 8 and equals 8 for fun Octal NYE celebrations!

#### Hedron Orientation Shorthand
Easily know how far through a Hedron you are with decimals. Question is it half past 5? Yes it is 5.50 .... makes sense. Half dollar. Quarter past the hours? Sure if it's 3.25, it's a quater-past three, easy, quarters are good in gaming arcades.

- H1 (.25 .50 .75)
- H2 ...
- H3 ...
- H4 ...
- H5 ...
- H6 ...
- H7 ... 
- H8 ... *

#### Triangles, 24 hours / 3 = 8
If all calculations are correct a hedron could be considered the passage of just a teeny bit more than 3 hours.

Let's tesselate!

#### Further Resources / Inspiration
- Decimal Minutes: https://hr.colostate.edu/minute-to-decimal-conversion-chart
- Decimal Hours  : https://www.youtube.com/watch?v=-58c2mDU1KY
- Time can be art: https://nanoleaf.me
- Time can be childsplay: https://www.youtube.com/watch?v=VRyxzHIq3wY
- The Decans: https://egyptmagictours.com/the-ancient-egyptians-chose-36-stars-or-a-group-of-stars-called-the-decans/

Decan Blue? Sure ok. Time is fun again with deconds (seconds 0 to 100)
https://www.youtube.com/watch?v=5SD4lI9GKUE

(*) Could there be 16 hours in a day? Sure I don't see why not. The asterix on the keyboard is Shift+8 anything is possible!

### Run the clock
In a terminal
```
$ chmod +x main.py
$ ./main.py
```

### Example
11:45pm = 855 total sectors with 9 sectors remaining today roughly 1% remains of the day
```
Local Time: 23:45:10  [ssm @855.10 stm @8.90 spc: 99% spr: 1%]
Range Bar : -------------------------------------------------[+]
            SS 1 2 3 4 5 6 7 8 9 10AM/PM  2 3 4 5 6 7 8 9 10  SE


Where
- stm = Sectors til midnight      (.decond is a decimal second [0-100])
- ssm = Sectors since midnight    (.decond   = 1min:40s,  1,000d = 10m)
- spc = Segment percent completed (.range    = from 0 to 100%)
- spr = Segment percent remaining (.percent  = 36.0ds     1,000s = 16m)


Sector Time       (Oct:Dec:Dec:Period)  : S8:55:10⋅Nꝑ Sector[8.75] Period[N]
REL Segment Time  (Duo:Percent:Period)  : 11:75:Nꝑ     Hour:23 (75% complete)
STD Segment Time  (Duo:Dec:Dec:Period)  : 23:55:10⋅Night
Angle of Decond          (Second hand)  : 35°
Angle of Sector            (Hour hand)  : 356°

Sector Beat              : @855.sectors (octingenti - nocturnis)
Locale Beat              : @991.beats   (CDT)
Global Beat              : @240.beats   (BMT)

```

#### Synchronization with Mars 
- The Martian Time-Slip
- The Decans (36 star system)
- The some 20 minutes communcation lag over distance (Recorded Video Messaging)

Settlements on Mars would likely be commerce focused. How would we communicate easily between the two bodies in relation to a synchronized universal time and could we use the delta of 40 minutes between a sol and a lux to aid communication? Communications systems could have limited capacity or endure times of lower processing power and distances in space itself that could further delay message processing.

The first live stream from MEX was around 16 minutes delayed:

![June 2023 first livestream](https://raw.githubusercontent.com/duracell80/midnight-sectors/main/docs/images/livestream.png)

Inspired by the Martian Time-Slip, midnight-sectors provides an approximation between time on Earth and Mars for the purpose of delivering messages back to Earth in synchronicity of human refrenced time. To humans a message sent at 10:10 on Mars would appear to be seen as a new message arriving on Earth at 10:10 if all processing and transmission was completed within or before 20 sexagesimal minutes. 

Human communication between Earth and Mars could benefit from a method of equating time between the two locations taking into account the lag in time of sending data. For example sending radio signals back to Earth could take up to 20 sexagesimal minutes. Placing universal time on Mars slightly ahead of universal time on Earth provides a way to send a message at say 10:25 (25% or quarter past 10) in the morning on Mars and have it delivered or played back at 10:25 (25% or quarter past 10) on Earth.

Thus giving the impression of instant communication in the most important direction, Mars back to Earth.

#### Emergency Broadcasts
All messages back to Earth may be sent, processed and deliverable before the time it was sent. Thus emergency messages from Mars to Earth should be delievered without waiting for the time on Earth to reach the send time from Mars. Non emergency messages processed and deliverable before the sent from Mars time, could in theory be held or lowered in priority to enable processing of Emergency or high priority messages.

#### Enhancing the Martian Time-Slip
Whereas PKD (Phillip K Dick) imagined the time at midnight to be frozen to celebrate Mars as a distinct civilization from Earth and a time to shed inhibitions, freezing time doesn't make too much logical sense in practical life. Therefore the first Martian 36 sectors after midnight (The Decans) can be approximated as a percentage. This time slip provides the perfect calculation to make Mars be consistently ahead of Earth by 36 sectors. Giving a mechanisim to send a message from Mars timestamped with a local Mars time that would then almost equate to a real time in Earth based reception systems.

Encoding The Decans into interstellar travel seems pretty poetic!

The extent of how far Mars is ahead of Earth shows around 65% past 11 or at 23:40 sexagesimal-time at night on Earth

```
Earth Time  : 11:65⋅Nꝑ
⋅Mars Time  : 12:00⋅Nꝑ

Producing the 20 minutes for comms lag
```

The Time Slip begins at Midnight on Earth Where Coordinated Mars Time switches to Mars Timeslip Time. The progression of the TS is marked in the hour section of the display:

```
⋅Mars Time  : %:52⋅Sꝑ

The period changes to "S" denoting the Time-Slip is in progress
The timezone MTC changes to MTS

@019.sectors (MTS)
```

At 36 sectors; Timeslip Time ends leaving Mars ahead of Earth by 36 sectors. Artistically this Martian Time-Slip can be illustrated by lighting one of 36 stars on the face of a clock or other interface. At this time the zodiac signs can also be celebrated.

(Permission to use this code in films, docuseries and science fiction works is granted)

#### Beat IT (Inspiration)
So I wouldn't have gone down a decimal rabbit hole if it wasn't for beats. As a kid of the 80's the Swatch was to us what these crazy computers on straps are to kids today, that and t-shirts that changed color when you got hot, wonder why that also never caught on? 

Swatch time or BMT aims to be a standardized absolute time format that would be exactly the same around the world and not relative to a local time (except Zurich is about as cool and epic as Greenwhich.). Neither is a beat anchored to the relation of two celestial bodies nor does it make any sense since there aren't 100,000 seconds in a day. Beats are instead like most timezones anchored to a physical location. An example of a beat would be @237 and the idea is that it would be universally @237 everywhere. However by dividing a day into 1000 .beats is a little difficult to innately relate to human time. Another drawback is that @237 to me close to midnight is not the same as @237 somewhere else where they may be eating breakfast. Whereas we eat breakfast roughly at the "same relative time" around the world, for example 7am, with beats we get a cultural disconnect. 

https://en.wikipedia.org/wiki/Swatch_Internet_Time
