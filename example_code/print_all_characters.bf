Last modified November 21st 2025

Here is the organization
• c0: symbol
• c1: space
• c2: colon
• c3: ASCII 1s place
• c4: ASCII 10s place
• c5: ASCII 100s place
• c6: line break

>
> ++++ [<++++ ++++> -]              Insert space to c1
> +++++ ++ [ <+++++ +++> -]<++>     Insert colon to c2
> +++ +++ [ <++++ ++++> -]          Insert ASCII 0 to c3
> +++ +++ [ <++++ ++++> -]          Insert ASCII 0 to c4
> +++ +++ [ <++++ ++++> -]          Insert ASCII 0 to c5
  +++++ +++++ +++                   Insert line break to c6

<<<.<.<.<.+     Print symbol position and symbol

1 to 10
>>>> >>> +++ +++ +++ 
[
  <.<<<+.<.<.<.+ 
  >>>>>>>-
]                   
<.<<+.<----- ----.<.<.<.+   Reduce c3 to 0; add 1 to 10s place

11 to 90
>>>> >>>> ++++ ++++ 
[ 
  < +++ +++ +++ 
  [
    <.<<.<+.<.<.<.+ 
    >>>>>>>-
  ]                   
<.<<+.<----- ----.<.<.<.+ >>>> >>>> -
]

91 to 100
< +++ +++ +++ 
[
    <.<<.<+.<.<.<.+ 
    >>>>>>>-
]
<.<+.<----- ----.<----- ----.<.<.<.+

101 to 190
>>>> >>>> +++ +++ +++
[ 
  < +++ +++ +++ 
  [
    <.<.<.<+.<.<.<.+ 
    >>>>>>>-
  ]                   
<.<.<+.<----- ----.<.<.<.+ >>>> >>>> -
]

191 to 200
< +++ +++ +++ 
[
    <.<.<.<+.<.<.<.+ 
    >>>>>>>-
]
<.<+.<----- ----.<----- ----.<.<.<.+

201 to 250
>>>> >>>> +++++
[ 
  < +++ +++ +++ 
  [
    <.<.<.<+.<.<.<.+ 
    >>>>>>>-
  ]                   
<.<.<+.<----- ----.<.<.<.+ >>>> >>>> -
]

251 to 255
< +++++
[
  <.<.<.<+.<.<.<.+ 
  >>>>>>>-
]

I feel so stupid for doing it the other way
Could I reuse old functions?