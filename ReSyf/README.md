# installation

```bash
git clone https://github.com/boehm-e/ReSyfSimpleSynonym
cd ReSyfSimpleSynonym
./download.sh
```

# useage

```python
from ReSyfSimpleSynonym import Synonymes

sy = Synonymes()

sy.find_simpler("acquérir")
#> trouver
sy.find_simpler("tricoter")
#> faire du tricot
sy.find_simpler("acquérir")
#> trouver
```
