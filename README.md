# Midnight Sectors (Readable OctaDecimal Hybrid)
Time is messy and decimal time tricky. Midnight sectors is a decimal / hectosecond based unit of time measurement somewhere between Base 10 and Base 8 and somewhat relatable to Base 12. It is a local and relative alternative to Swatch internet time (BMT) set around the calculation of 86,400 seconds per day thus a day will start at midnight @000 and end at midnight @864. Does this replace standard time? No, it's an overlay, the math underneath is about as Babylonian as David Grey at a traffic light. 

Throwback Thursday: https://www.youtube.com/watch?v=zI_SBAkdKzc

### Overall goal: Make decimal minutes and seconds eaiser to relate to ...
This proposal lays out a hybrid between the two opposing systems, keeping a 7 day week, spliting the day into 8 (sectors) and again into 4 (periods). It stops short of 10 hours, because that's just confusing!!

The @time is readable on an octal clock!
![Octahedron as net](https://raw.githubusercontent.com/duracell80/midnight-sectors/main/docs/images/octahedron_net.svg)

#### Terms For The Day
- Lumin (A whole of 864 sectors = 1 day of 24 hours, lumen = light, day is light)
- Segment (Octal division of the day into 8 parts of up to 100 sectors each)
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
- Night     - nox (nx) *night crossing
- Afternoon - post meridiem (pm)
- Morning   - antemeridies (am)
- Evening   - nocturnis (nc) *night coming

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
- Hedron 8 (@800 The remaining 64) - octingenti

64 is divisible by 8 and equals 8 for fun Octal NYE celebrations!

#### Hedron Orientation Shorthand
Easily know how far through a Hedron you are with decimals is it half past 5? Yes it is 5.50 .... makes sense. Half dollar. Quarter past the hours? Sure if it's 3.25, it's a quater-past three, easy.

- H1 (.25 .50 .75)
- H2 ...
- H3 ...
- H4 ...
- H5 ...
- H6 ...
- H7 ... 
- H8 ... *

### Further Resources / Inspiration
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

#### Beat IT (Inspiration)
So I wouldn't have gone down a decimal rabbit hole if it wasn't for beats. As a kid of the 80's the Swatch was to us what these crazy computers on straps are to kids today, that and t-shirts that changed color when you got hot, wonder why that also never caught on? Swatch time or BMT aims to be a standardized absolute time format that would be exactly the same around the world and not relative to a local time (except Zurich is about as cool and epic as Greenwhich.). Neither is a beat anchored to the relation of two celestial bodies nor does it make any sense since there aren't 100,000 seconds in a day. Beats are instead like most timezones anchored to a physical location. An example of a beat would be @237 and the idea is that it would be universally @237 everywhere. However by dividing a day into 1000 .beats is a little difficult to innately relate to human time. Another drawback is that @237 to me close to midnight is not the same as @237 somewhere else where they may be eating breakfast. Whereas we eat breakfast roughly at the "same relative time" around the world, for example 7am, with beats we get a cultural disconnect. 

https://en.wikipedia.org/wiki/Swatch_Internet_Time
