# keyboardwalk

- `walk` / `walk_rec`: given a keyboard and a string, is the string a walk of the keyboard?
- `gen_rand_walk`: given a keyboard, generate a keyboard walk / key boardwalk string


keyboard | walk | keyboardwalk? |
-------- | ---- | ------------- |
`lol`    | `ok` | no
`qwertyuiop`<br>`asdfghjkl`<br>`zxcvbnm` | `wsdxcv` | yes
`qwertyuiop`<br>`asdfghjkl`<br>`zxcvbnm` | `qwertgbnji` | yes
`qwertyuiop`<br>`asdfghjkl`<br>`zxcvbnm` | `qwertybnm` | no
