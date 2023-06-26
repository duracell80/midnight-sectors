# midnight-sectors
Local and relative alternative to swatch internet time set around the notion of 86,400 seconds per day. 

### Run the clock
In a terminal
```
$ chmod +x main.py
$ ./main.py
```

### Example
11:30pm = 846 sectors with 18 sectors remaining today
```
Local Time: 23:30:00  [ssm @846.00 stm @18.00 (sph: 36)]


Where
- ssm = Sectors since the last midnight
- stm = Sectors remaining until the next midnight
- sph = Sectors per human hour
```

### Theory
- There are 86,400 seconds in a day.
- Divided by 100, there are @864 sectors in a day
- Each sector can hold 100 relatable human seconds!!
- Subtracting the current sector from 864 produces an innate notion of countdown towards the end of the day
- At local midnight the SSM (Sectors Since Midnight) start back at zero, this is highly intuitive
- At local midnight the STM (Sectors Til Midnight) flip back to 864, giving an intuitive context of sectors
- A sector that is at midnight @000 is then easily identifiable and relatable to human midnight 00:00

### Defining a day as a seg
There simply are enough sectors in a seg!! Since a human day consists of 24 hours to relate the two systems the total number of sectors can be divided by 24, giving 36 sectors per hour and 100 seconds per sector. A whole day can then be thought of as a segment of the week. Each segment representing @864 sectors. A week may still be 7 segs in duration and December can contain 31 segs as it would days.

### Beat IT
.Beat or Swatch Time aims to be a standardized absolute time format that would be exactly the same around the world and not relative to a local time. Neither is a beat anchored to the relation of two celestial bodies nor does it make any sense since there aren't 100,000 seconds in a day. Beats are instead like most timezones anchored to a physical location. An example of a beat would be @237 and the idea is that it would be universally @237 everywhere. However by dividing a day into 1000, .beats is a little difficult to innately relate to human seconds, nor does it track with human minutes and being absolute there is no refrence to local time. Another drawback is that @237 to me close to midnight is not the same as @237 somewhere else where they may be eating breakfast. Whereas we eat breakfast roughly at the "same relative time" around the world, for example 7am, with beats we get a cultural disconnect. 

https://en.wikipedia.org/wiki/Swatch_Internet_Time

### Advantages of sectors:
- The main advantage of this time format is its dual personality 
- As an example STM gives a countdown to midnight
- Relates to and changes alongside the current minute
- Contains 100 seconds per sector, making math easier
- Can be roughly related to an hour by halving (if 30 sectors have passed, likely an hour has elapsed)
