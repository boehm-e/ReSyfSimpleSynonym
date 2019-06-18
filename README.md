# CREDIT
this module is based on [ReSyf](https://cental.uclouvain.be/resyf/) and all credit goes to :

@dorian Ricci - Student at Université Catholique de Louvain-la-Neuve (UCL)

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
