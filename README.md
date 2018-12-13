poetryBot is a simple command line bot that will generate a poem using Markov chains.

This is based **heavily** on [markovBot](https://github.com/tmkuba/markovBot).

# Getting Started
## Dependencies

Install the [markovify](https://github.com/jsvine/markovify) package:

`pip install markovify`

_I recommend using pipenv to handle your installation of markovify. There is a good (easy) pipenv walkthourgh here: [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)_

## Fill corpus of example text

This project comes with a copy of Marx and Engles' _Communist Manifesto_ and the King James Version of Ecclesiastes.

Lots of good sources are available from [Project Gutenberg](https://www.gutenberg.org/).

Save your own in the `works` directory.

## Test Markov chain

You determine the source and length of the poem by passing arguments when running from the command line.

`python poem.py manifesto.txt 5` to see an example poem.

## Caveat Emptor

It doesn't write particularly good poems:

```
> python poem.py manifesto.txt 12
```
<pre>
Precisely so; that is required of him,
For the rest, it is a really revolutionary class,
By degrees they sink into the political arena:
The unceasing improvement of the working class!
Altogether collisions between two classes
The conditions of his own class.
But even in the hands of those nine-tenths
All that is bound to be, exploded by those means.
When, therefore, capital is wage-labour
Conservation of the proletarian movement
Differences of age and sex
The whole of bourgeois society.
</pre>

```
> python poem.py ecclesiastes.txt 12
```
<pre>
As thou knowest not what evil shall be many!
As thou knowest not what is man the better
There is a fool will swallow up himself--
I said of laughter, It is better than he-
Curse not the rich sit in low place
For who knoweth what is good and to the end!
As he came forth of them with their eyes,
This is an evil disease
And so I saw vanity under the sun.
There is no end of a thing
Wisdom is good in his life--
There is no better.
</pre>