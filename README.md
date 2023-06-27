# midnight-sectors
Midnight sectors are a decimal / hectosecond based unit of time measurement somewhere between Base 10 and Base 8 and somewhat relatable to Base 12. It is a local and relative alternative to swatch internet time set around the Base 12 notion of 86,400 seconds per day. 

The @time is readable on an octal clock!
![An Octal Wrist Watch](https://rlv.zcache.com/octal_clock_base_eight_wrist_watch-r96038d637caa4f628250eaf51195ed92_zd5ip_630.jpg?rlvnet=1&view_padding=%5B285%2C0%2C285%2C0%5D)

### Terms
- Segment (1 segment of 864 sectors = 1 day of 24 hours)
- Slice   (The octal time way of spliting the day into 8 parts, also pie slices)
- Period  (Consisting of 2 slices, a period denotes 4 periods of time in the day)
- Sector  (The minute of 100 seconds)
- Tick    (The even second within a sector)
- Tock    (The odd second within a sector)
- Range   (The progression of day from 0 to 100% clockwise in linear left to right motion)

Note: that the range allows the better scope of an afternoon and evening duration based on percentage of the day elapsed. To that goal a prefix to time can be added rather than AM/PM the following letters signify roughly four time periods in a segment (NAME)

Periods: 
- [N] = Night
- [A] = Afternoon
- [M] = Morning
- [E] = Evening 

### Run the clock
In a terminal
```
$ chmod +x main.py
$ ./main.py
```

### Example
11:30pm = 846 sectors with 18 sectors remaining today roughly 2% remains of the day
```
Local Time: 23:29:59  [ssm @846.00 stm @18.00 spc: 98% spr: 2%]
Range Bar : -------------------------------------------------[+]-
            DS 1 2 3 4 5 6 7 8  11 AM/PM 2 3 4 5 6 7 8 9  10  DE



Where
- stm = Sectors til midnight      (.tick is a sector's second [0-100])
- ssm = Sectors since midnight    (.tick   = 1 minute 40 seconds)
- spc = Segment percent completed (.range  = from 0 to 100%)
- spr = Segment percent remaining
- sph = Sectors per standard hour (~36 .sectors in an hour)
- blt = Beats in Local time (.beat = 1min:25s, ~42 .beats in an hour)

NAME  = [N]ight [A]fternoon [M]orning [E]vening
DS/DE = [D]ay[S]tart [D]ay[E]nd



Segment Period     : N8:46:00
                         
Local Beat         : @982.beats (CDT)
Universal Beat     : @229.beats (BMT)

```

### Theory
- Starting with Base 12
- There are 86,400 seconds in a standard day.
- Divided by 100, there are @864 sectors in a day (rather than 1000)
- Each sector can hold 100 relatable standard seconds (just like .beats)!!
- Subtracting the current sector from 864 produces an innate notion of a countdown that tracks actual minutes

- A day can be broken down into 8 periods and is readable on an Octal Clock
  
- At local midnight the SSM (Sectors Since Midnight) start back at zero, this is highly intuitive
- At local midnight the STM (Sectors Til Midnight) flip back to 864, giving an intuitive context of sectors
- A sector that is at midnight @000 is then easily identifiable and relatable to human midnight 00:00

### Defining a day as a seg
There simply are enough sectors in a seg!! Since a human day consists of 24 hours to relate the two systems the total number of sectors can be divided by 24, giving 36 sectors per hour and 100 seconds per sector. A whole day can then be thought of as a segment of the week. Each segment representing @864 sectors. A week may still be 7 segs in duration and December can contain 31 segs as it would days.

### Beat IT
.Beat or Swatch Time aims to be a standardized absolute time format that would be exactly the same around the world and not relative to a local time. Neither is a beat anchored to the relation of two celestial bodies nor does it make any sense since there aren't 100,000 seconds in a day. Beats are instead like most timezones anchored to a physical location. An example of a beat would be @237 and the idea is that it would be universally @237 everywhere. However by dividing a day into 1000 .beats is a little difficult to innately relate to human time. Another drawback is that @237 to me close to midnight is not the same as @237 somewhere else where they may be eating breakfast. Whereas we eat breakfast roughly at the "same relative time" around the world, for example 7am, with beats we get a cultural disconnect. 

https://en.wikipedia.org/wiki/Swatch_Internet_Time

### Advantages of sectors:
- The main advantage of this time format is its dual personality
- Seen at midnight (or DayStart) when everything flips magically
- It's magic ... https://youtu.be/JYZv0_PMzOg 
- Easily know how much time remains in the day; STM gives a countdown to midnight
- Relates to and changes alongside the current minute
- Contains 100 seconds per sector, making math a bit easier
- Can be roughly related to an hour by halving (if 30 sectors have passed, likely almost an hour has elapsed)
- Who also doesn't want 40 more seconds per minute?
