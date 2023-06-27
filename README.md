# midnight-sectors
Midnight sectors are a decimal / hectosecond based unit of time measurement somewhere between Base 10 and Base 8 and somewhat relatable to Base 12. It is a local and relative alternative to swatch internet time set around the Base 12 notion of 86,400 seconds per day. 

The @time is readable on an octal clock!
![image](data:image/jpeg;base64,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)

### Terms
- Segment (1 segment of 864 sectors = 1 day of 24 hours)
- Slice   (The octal time way of spliting the day into 8 parts)
- Sector  (The minute of 100 seconds)
- Tick    (The even second within a sector)
- Tock    (The odd second within a sector)
- Range   (The progression of a day from 0 to 100%)

Note: that the range allows the better scope of an afternoon and evening duration based on percentage of the day elapsed. To that goal a prefix to time can be added rather than AM/PM the following letters signify roughly four time periods in a segment (NAME)

[N] = Night
[A] = Afternoon
[M] = Morning
[E] = Evening 

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
- Each sector can hold 100 relatable human seconds (just like .beats)!!
- Subtracting the current sector from 864 produces an innate notion of a countdown that tracks actual minutes

- A day can be broken down into 8 periods and is readable on an Octal Clock
  
- At local midnight the SSM (Sectors Since Midnight) start back at zero, this is highly intuitive
- At local midnight the STM (Sectors Til Midnight) flip back to 864, giving an intuitive context of sectors
- A sector that is at midnight @000 is then easily identifiable and relatable to human midnight 00:00

### Defining a day as a seg
There simply are enough sectors in a seg!! Since a human day consists of 24 hours to relate the two systems the total number of sectors can be divided by 24, giving 36 sectors per hour and 100 seconds per sector. A whole day can then be thought of as a segment of the week. Each segment representing @864 sectors. A week may still be 7 segs in duration and December can contain 31 segs as it would days.

### Beat IT
.Beat or Swatch Time aims to be a standardized absolute time format that would be exactly the same around the world and not relative to a local time. Neither is a beat anchored to the relation of two celestial bodies nor does it make any sense since there aren't 100,000 seconds in a day. Beats are instead like most timezones anchored to a physical location. An example of a beat would be @237 and the idea is that it would be universally @237 everywhere. However by dividing a day into 1000, .beats is a little difficult to innately relate to human time, nor does it track with human minutes and being absolute there is no refrence to local time. Another drawback is that @237 to me close to midnight is not the same as @237 somewhere else where they may be eating breakfast. 

Whereas we eat breakfast roughly at the "same relative time" around the world, for example 7am, with beats we get a cultural disconnect. 

https://en.wikipedia.org/wiki/Swatch_Internet_Time

### Advantages of sectors:
- The main advantage of this time format is its dual personality 
- Easily know how much time remains in the day; STM gives a countdown to midnight
- Relates to and changes alongside the current minute
- Contains 100 seconds per sector, making math a bit easier
- Can be roughly related to an hour by halving (if 30 sectors have passed, likely almost an hour has elapsed)
- Who also doesn't want 40 more seconds per minute?
