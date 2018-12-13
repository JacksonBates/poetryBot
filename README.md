poetryBot is a simple command line bot that will generate a poem using Markov chains.

This is based **heavily** on [markovBot](https://github.com/tmkuba/markovBot).

# Getting Started
## Dependencies

Install the [markovify](https://github.com/jsvine/markovify) package:

`pip install markovify`

_I recommend using pipenv to handle your installation of markovify. There is a good (easy) pipenv walkthourgh here: [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)_

## Fill corpus of example text

This project comes with a copy of Marx and Engles' _Communist Manifesto_ as its example corpus.

Lots of good sources are available from [Project Gutenberg](https://www.gutenberg.org/).

Save the text file as `corpus.txt`

## Test Markov chain

You determine the length of the poem by passing a number as an argument when running from the command line.

`python poem.py 5` to see an example poem.

## Caveat Emptor

It doesn't write particularly good poems:

```
> python poem.py 12
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