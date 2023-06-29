# Midnight Sectors (Readable Decimal Hybrid)
Time is messy and decimal time tricky. Midnight sectors is a decimal / hectosecond based unit of time measurement somewhere between Base 10 and Base 8 and somewhat relatable to Base 12. It is a local and relative alternative to swatch internet time set around the calculation of 86,400 seconds per day thus a day will start at midnight @000 and end at midnight @864.

### A 10 day week?
NO! Relax, there are no 10 day weeks or 1 day weekends here. This proposal lays out a hybrid between the two opposing systems, keeping a 7 day week.


The @time is readable on an octal clock!
![An Octal Wrist Watch](https://rlv.zcache.com/octal_clock_base_eight_wrist_watch-r96038d637caa4f628250eaf51195ed92_zd5ip_630.jpg?rlvnet=1&view_padding=%5B285%2C0%2C285%2C0%5D)

### Terms For The Day
- Segment (A segment of 864 sectors = 1 day of 24 hours)
- Slice   (Octal division of the day into 8 parts of up to 100 sectors each)
- Period  (2 slices of a segment, a period denotes 4 periods of time [NAME])

Ever noticed how it's not entirely clear how AM/PM denotes evening and morning? Add to this, AM denotes a period of time that is both night and day. It's not possible to look at a clock and know straight away if AM means morning when it's light or night when it's dark.

### Terms for Hours, Minutes and Seconds
- Sector  (A sector contains = 1 minute and 40 seconds or 100 seconds)
- Decond  (An integer second ranging to 100)
- Tick    (An odd  .decond)
- Tock    (An even .decond)
- SSM     (The number of whole single sectors of 100 seconds, since midnight)
- STM     (The number of whole single sectors of 100 seconds, til midnight)
- Range   (The progression of day from 0 to 100% clockwise in linear left to right motion)

#### Periods:
Two slices are combined to give 4 periods
- [N] = Night
- [A] = Afternoon
- [M] = Morning
- [E] = Evening

Latin:
- Night     - Nox
- Afternoon - post meridiem (pm)
- Morning   - antemeridies (am)
- Evening   - nocturnis

#### Slices with Latin Names:
There are 8 slices or hours in the day. A whole sector can span a period, so morning may run through the 3rd and 4th slice. A slice defines 100 sectors.

- Slice 1 (000 to 100) - centum
- Slice 2 (100 to 200) - ducenti
- Slice 3 (200 to 300) - trecenti
- Slice 4 (300 to 400) - quadrigenti
- Slice 5 (500 to 600) - quingenti
- Slice 6 (600 to 700) - sescenti
- Slice 7 (700 to 800) - septingenti
- Slice 8 (The remaining 64) - octingenti

64 is divisible by 8 and equals 8 for fun Octal NYE celebrations!

#### Sector Orientation Shorthand
Easily know how far through a sector you are with decimals.

- S1 (.25 .50 .75)
- S2 ...
- S3 ...
- S4 ...
- S5 ...
- S6 ...
- S7 ... 
- S8 ...

### Further Resources
- Decimal Minutes: https://hr.colostate.edu/minute-to-decimal-conversion-chart
- Decimal Hours  : https://www.youtube.com/watch?v=-58c2mDU1KY



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

### Theory
- Starting with Base 12
- There are 86,400 seconds in a standard day.
- Divided by 100, there are @864 sectors in a day (rather than 1000)
- Each sector can hold 100 relatable standard seconds (just like .beats)!!
- Subtracting the current sector from 864 produces an innate notion of a countdown that tracks actual minutes

- A day can be broken down into 8 sectors and is readable on an Octal Clock

- Those 8 sectors can yeild 4 periods, that we culturally know in English by NAME

- At local midnight the SSM (Sectors Since Midnight) start back at zero, this is highly intuitive
- At local midnight the STM (Sectors Til Midnight) flip back to 864, giving an intuitive context of sectors
- A sector that is at midnight @000 is then easily identifiable and relatable to human midnight 00:00

### Defining a day as a segment
There simply are enough sectors in a segment!! Since a human day consists of 24 hours to relate the two systems the total number of sectors can be divided by 24, giving 36 sectors per hour and 100 seconds per sector. A whole day can then be thought of as a segment of the week. Each segment representing @864 sectors. A week may still be 7 segs in duration and December can contain 31 segs as it would days.

### Beat IT
.Beat or Swatch Time aims to be a standardized absolute time format that would be exactly the same around the world and not relative to a local time. Neither is a beat anchored to the relation of two celestial bodies nor does it make any sense since there aren't 100,000 seconds in a day. Beats are instead like most timezones anchored to a physical location. An example of a beat would be @237 and the idea is that it would be universally @237 everywhere. However by dividing a day into 1000 .beats is a little difficult to innately relate to human time. Another drawback is that @237 to me close to midnight is not the same as @237 somewhere else where they may be eating breakfast. Whereas we eat breakfast roughly at the "same relative time" around the world, for example 7am, with beats we get a cultural disconnect. 

https://en.wikipedia.org/wiki/Swatch_Internet_Time
