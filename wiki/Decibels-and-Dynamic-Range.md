# Decibels and Dynamic Range

Decibels are not a new signal representation by themselves. They are just a logarithmic way of expressing a ratio relative to some reference:

`dB = logarithmic relative strength`

And dynamic range tells you: how far apart the strongest and weakest useful levels are.

When computing spectrograms, we often convert power or magnitude to decibels using a top_db value (e.g., 80 dB), which means values more than 80 dB below the maximum are clipped.
