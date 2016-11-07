### Download Baidu Maps tiles

Edit `download_tiles.py` to specify the area and the zoom level you want.

    zoom = 19
 
    lat_start, lon_start = 31.022547,121.429391
    lat_stop, lon_stop = 31.041453,121.45749
        
    satellite = True    # roads if false

You can easily find Baidu coordinates with [http://api.map.baidu.com/lbsapi/getpoint/](http://api.map.baidu.com/lbsapi/getpoint/).

Then, run `$ python download_tiles.py` and get individual tiles

### Merge Baidu Maps tiles

Edit `merge_tiles.py` to specify the area and the zoom level you want, it's just the same as before.

    zoom = 19
 
    lat_start, lon_start = 31.022547,121.429391
    lat_stop, lon_stop = 31.041453,121.45749

    satellite = True    # roads if false

Then, run `$ python merge_tiles.py` and get `map_s.jpg` for satellite or `map_r.png` for roads.


Note: merging the tiles requires [Python Image Library](http://www.pythonware.com/products/pil/).

