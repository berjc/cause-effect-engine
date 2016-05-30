# Cause-Effect-Engine
The Cause-Effect-Engine is a simple AI for explaining how a source cause leads to a sink effect.

## Installation
Run `git clone https://github.com/berjc/cause-effect-engine.git`

## Use the Cause-Effect-Engine
Run `cd cause-effect-engine; python engine.py -f <FILE>` where `FILE` denotes the cause-effect pairs to load.

## Format of Cause-Effect File
Each line is a cause-effect pair where the cause and effect are delimited by a space.

## Example Usage
```
>>> python engine.py -f ../toy_example
Source: homework
Sink:   sleep

  Source Cause 'homework'
    leads to Concept 'tired'
  Sink Effect 'sleep'

Source: hungry
Sink:   sleep

  Source Cause 'hungry'
    leads to Concept 'eat'
    leads to Concept 'nap'
  Sink Effect 'sleep'

Source: ^C
Goodbye!
```
