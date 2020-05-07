# Directory Structure
```text
.
├── README.md
├── run.py
└── utils
    ├── data.py
    ├── __init__.py
    ├── model.py
    └── train.py

1 directory, 6 files
```
# Command Line Interface
```text
usage: run.py [-h] --inp INP --hidden HIDDEN --out OUT --bias BIAS

optional arguments:
  -h, --help       show this help message and exit
  --inp INP        FeedForward network Input Dimension
  --hidden HIDDEN  FeedForward network Hidden Dimension
  --out OUT        FeedForward network Output Dimension
  --bias BIAS      Add Bias Unit to the network
```

# Install PyBrain to Build FeedForward network
```text
$ git clone git://github.com/pybrain/pybrain.git
$ python setup.py install
````

# Data
## Logical XOR
```text
features: [0,0], [0,1], [1,0], [1,1]  
```
```text
Labels: 0, 1
```

# Build and Train the 1-Layer FeedForward network

## Parameters
```text
inp: FeedForward network Input Dimension
```
```text
hidden: FeedForward network Hidden Dimension
```
```text
out: FeedForward network Output Dimension
```
```text
bias: Add Bias Unit to the network
```

## CLI

```shell
 python run.py --inp 2 --hidden 3 --out 1 --bias yes
```
## Model with Bias
```text
FeedForwardNetwork-8
   Modules:
    [
        <BiasUnit 'bias'>, <LinearLayer 'in'>, 
        <SigmoidLayer 'hidden'>, 
        <LinearLayer 'out'>
    ]
   Connections:
    [
        <FullConnection 'FullConnection-4': 'in' -> 'hidden'>, 
        <FullConnection 'FullConnection-5': 'bias' -> 'hidden'>,
        <FullConnection 'FullConnection-6': 'bias' -> 'out'>, 
        <FullConnection 'FullConnection-7': 'hidden' -> 'out'>
    ]

````
## Model with no Bias
```text
FeedForwardNetwork-5
   Modules:
    [
        <LinearLayer 'in'>, 
        <SigmoidLayer 'hidden'>, 
        <LinearLayer 'out'>
    ]
   Connections:
    [   
        <FullConnection 'FullConnection-3': 'hidden' -> 'out'>, 
        <FullConnection 'FullConnection-4': 'in' -> 'hidden'>
    ]

```
## Training procedure
```text

it: 4000, error: 0.023168016122453627 
[0,0]: 0.7619703700071068
[0,1]: 0.21617108732047607 
[1,0]: 0.2150130945150721 
[1,1]: 0.8244412708615696 
----------------------------------------------------------------------------------------------------

it: 5000, error: 0.002396756318624832 
[0,0]: 0.9187350722850457
[0,1]: 0.06714937411408439 
[1,0]: 0.0704508533734266 
[1,1]: 0.9492915985559952 
----------------------------------------------------------------------------------------------------

it: 6000, error: 0.00014984932505376176 
[0,0]: 0.9790426860706662
[0,1]: 0.01668612934959457 
[1,0]: 0.01771765314691054 
[1,1]: 0.9883796744234414 
----------------------------------------------------------------------------------------------------

it: 7000, error: 8.173697094341001e-06 
[0,0]: 0.995037355849853
[0,1]: 0.00387120297802801 
[1,0]: 0.004136546365500426 
[1,1]: 0.9973892769719986 
----------------------------------------------------------------------------------------------------

it: 8000, error: 4.314430125613677e-07 
[0,0]: 0.9988534786579304
[0,1]: 0.000884702937198556 
[1,0]: 0.0009460132321691406 
[1,1]: 0.9994029423097202 
----------------------------------------------------------------------------------------------------

it: 9000, error: 2.254379838197172e-08 
[0,0]: 0.9997381116354624
[0,1]: 0.00020295017968186002 
[1,0]: 0.00021712038726795502 
[1,1]: 0.999864968620003 
----------------------------------------------------------------------------------------------------

it: 10000, error: 1.1768277228608924e-09 
[0,0]: 0.9999399660658328
[0,1]: 4.6211727826150906e-05 
[1,0]: 4.937901514168175e-05 
[1,1]: 0.9999689138150667 
----------------------------------------------------------------------------------------------------

it: 11000, error: 6.13881447535876e-11 
[0,0]: 0.9999863274390747
[0,1]: 1.058735458758786e-05 
[1,0]: 1.1332287837451105e-05 
[1,1]: 0.9999929428634463 
----------------------------------------------------------------------------------------------------

it: 12000, error: 3.2065192035329622e-12 
[0,0]: 0.9999968762582869
[0,1]: 2.4186493841060752e-06 
[1,0]: 2.589596654556381e-06 
[1,1]: 0.9999983897414053 

```

```text

Training ends 
[0,0]: 0.9999999954236384
[0,1]: 6.219498471793372e-09 
[1,0]: 6.2876548412305056e-09 
[1,1]: 0.9999999909627013 
````