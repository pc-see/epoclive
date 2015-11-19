Epoclive
========

Stream data from Epoc headset and perform BCI analysis.

Epoclive in action: [Hjernestyrt drone (showing Epoclive running in the background)](https://tv.nrk.no/serie/distriktsnyheter-midtnytt/DKTL98081015/10-08-2015#t=59s)

Content
* Using Epoclive
* Media coverage

Using Epoclive
--------------

```
$ epoc -h
usage: epoclive [--args]

epoc live data stream

optional arguments:
  -h, --help  show this help message and exit
  --fft       run FFT analysis
  --get-data  read data from sensors
  --hht       run HHT analysis
  --setup     setup epoc live
  --ssvep     steady-state visually evoked potential
  --stft      run STFT analysis
  --wavelet   show wavelet transform
  -a          all sensors
  -c          channel of sensor
  -d          total duration
  -i          path to get input
  -o          path to store output
```

To get real-time data from all sensors.

```
$ epoc --get-data -a
```

![$ epoc --get-data -a](https://cloud.githubusercontent.com/assets/12416402/7783299/cb67b966-013d-11e5-9a9a-8cc68246d951.png)

Media coverage
--------------

Epoclive has appeared in the media, see links below.

* [Think a thought and then take flight](http://gemini.no/en/2015/09/think-a-thought-and-then-take-flight/)
* [Tenk tanken - og fly av gårde] (http://www.abcnyheter.no/livet/2015/09/06/194870294/tenk-tanken-og-fly-av-garde)
* [Norske studenter styrer droner med hjernebølger](http://www.tek.no/artikler/her-styrer-han-dronen-med-hjernebolger/192625)
* [Får drone til å fly ved å blunke](http://www.nrk.no/trondelag/far-drone-til-a-fly-ved-a-blunke-1.12492845)

.. also in TV and Radio:

* [Hjernestyrt drone (showing Epoclive running in the background)](https://tv.nrk.no/serie/distriktsnyheter-midtnytt/DKTL98081015/10-08-2015#t=59s)
* [Tankestyrt drone på NTNU](https://radio.nrk.no/serie/her-og-naa-hovedsending/DMNH01015615/10-08-2015#t=1h20m2s)

