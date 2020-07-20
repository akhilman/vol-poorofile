# Poor man's volume profile

This is an attempt to get something more or less similar to the volume profile for free.

![Screenshot](screenshot.png)


## Install

* Add [Poor man's volume profile][vpoorof] to you TradingView chart
* Add Poor man's volume profile (Big picture) to you TradingView chart (Not released yet)


## Build

```bash
# install jinja2
pip install -r requirements.txt
# generate code
./generate.py vol-poorofile.pine vol-poorofile.dist.pine
./generate.py vol-poorofile-big.pine vol-poorofile-big.dist.pine
```

[vpoorof]: https://www.tradingview.com/script/IWdpl712-Poor-man-s-volume-profile/
