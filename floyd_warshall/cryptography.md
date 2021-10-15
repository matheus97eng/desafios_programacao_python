# Problem: Cryptography

The United Nations Against Leaks (UNAL) is trying to prove a method to encrypt e-mails to make them more secure to the world. However, this encryption method is not an easy process. First you have the original text to encode, then every character of the text is changed to any other character with a certain cost because the UNAL has to pay some money in order to change characters into other characters (this process can be repeated zero or various times). After this process is finished, we will have a new brand text which will be the message that will be send through the internet.

We already have the original text, the encrypted text, and which characters can be changed along with the corresponding cost. As the UNAL is paying for the encryption, they are hiring you to calculate the minimum cost of the e-mail encryption.

## Input
The first line of the input consists of a string s of size |s|, (1 ≤ |s| ≤ 105) - the original message.

The second line consists of a string t of size |t|, (|t| = |s|) - the encrypted message.

The third line consists of a number m (1 ≤ m ≤ 5 * 104), the number of possible changes between characters.

Finally m lines follow, each containing a, b, c, where a and b (a ≠ b) are ASCII characters and c is an integer (1 ≤ c ≤ 103), the cost of changing a into b.

It is guaranteed that s and t have the same length, don't have any whitespaces, and they are made using only printable characters ASCII (ASCII codes from 33 to 126).

## Output
Print one line with the minimum cost of encrypting s to t. If there is no way to encrypt s to t print  - 1.

## Examples
### Input
hello!

world!

8

a b 1

a d 3

e o 5

h w 10

l r 12

l e 5

o a 2

o d 8

### Output
32

### Input
Aa

ab

2

a b 10

a b 12

### Output
-1
