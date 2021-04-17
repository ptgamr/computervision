```
python3 color_range.py shl_1.jpg
```

```
Ubuntu 20.04

Change: sudo vi /etc/sysctl.conf

net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1

sudo sysctl -p

pip3 install opencv-python
pip3 install matplotlib
```
