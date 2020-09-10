# SG_Customs Dataset

- [SG_Customs Dataset](https://bhpan.buaa.edu.cn:443/link/FBDE129815220D30CD8797512ACC5C5B)
- [SG_Customs Dataset_Invoice](https://bhpan.buaa.edu.cn:443/link/79BD538BDBE5AA4164ED03C0491DA737)
- [SG_Customs Dataset_Invoice [Splitted]](https://bhpan.buaa.edu.cn:443/link/A6D049B5ACF2CABA80E8F8B48AD39C4B)
- [SG_Customs Dataset_Invoice [Overall]](https://bhpan.buaa.edu.cn:443/link/A4CDAB285216DE3EC0E15CF76A7F9098)
- [cached_train_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/8A4996BAE9179BCE75E1FB665AE09949)
- [cached_test_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/4962F0E4280A89304FCC0E946C6C130B)
- [sen_level_cached_train_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/4962F0E4280A89304FCC0E946C6C130B)
- [sen_level_cached_test_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/EBCFD7481BCD27C1937BEB2BFB73771D)

## Overview on Dataset

| SG-Custom    | ACTMAX | ADAMP | AKRIBIS | ALPHA | AMPHENOLE | CISCO | INFINEON | KOMAGUSAM | MICRON | NETAPP | RUCKSWIRE | SIIX | TI  | TOSHIBA | Total |
|:------------:|:------:|:-----:|:-------:|:-----:|:---------:|:-----:|:--------:|:---------:|:------:|:------:|:---------:|:----:|:---:|:-------:|:-----:|
| INVShipper   |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   14  |
| INVConsignee |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   14  |
| INVNo        |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   14  |
| INVPage      |        |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |           |   √  |  √  |         |   11  |
| INVDate      |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   14  |
| INVTermType  |    √   |   √   |    √    |       |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   14  |
| INVCurrency  |        |   √   |    √    |   √   |     √     |   √   |          |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   12  |
| INVQtyUom    |        |       |         |       |           |   √   |     √    |           |    √   |        |     √     |      |     |         |    4  |
| INVTotalGW   |        |   √   |         |       |     √     |   √   |     √    |     √     |    √   |        |     √     |   √  |     |         |    8  |
| INVTotalNW   |        |       |         |       |           |       |     √    |           |    √   |        |           |      |  √  |         |    3  |
| INVTotalQty  |        |   √   |         |   √   |     √     |   √   |     √    |     √     |    √   |        |     √     |   √  |  √  |    √    |   11  |
| INVTotal     |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   14  |
| INVWtUnit    |        |       |         |       |     √     |       |          |           |        |        |           |      |     |         |    1  |
| C.Desc       |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |      |  √  |    √    |   13  |
| C.PartNumber |    √   |   √   |    √    |   √   |     √     |   √   |     √    |           |    √   |    √   |     √     |   √  |  √  |         |   12  |
| C.ItemNo     |    √   |       |    √    |   √   |           |   √   |     √    |     √     |        |        |     √     |   √  |  √  |         |    9  |
| C.COO        |        |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |      |  √  |    √    |   12  |
| C.Unit       |        |   √   |    √    |   √   |     √     |       |          |           |        |        |     √     |   √  |  √  |         |    7  |
| C.HSCode     |        |       |    √    |       |     √     |       |     √    |           |    √   |    √   |     √     |      |  √  |         |    7  |
| C.GW         |        |       |         |       |     √     |       |          |           |        |        |           |      |     |         |    1  |
| C.Price      |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |         |   13  |
| C.Qty        |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |    √    |   14  |
| C.BoxNumber  |        |       |         |       |           |       |          |           |        |        |           |      |  √  |         |    1  |
| C.Total      |    √   |   √   |    √    |   √   |     √     |   √   |     √    |     √     |    √   |    √   |     √     |   √  |  √  |         |   13  |
| Data Num     |  150   |  148  |   120   |  421  |    150    |  150  |    133   |    442    |   77   |   160  |    297    | 150  | 150 |    48   |  2596 |
| Training Set |  112   |  111  |    90   |  315  |    112    |  112  |     99   |    331    |   57   |   120  |    222    | 112  | 112 |    36   |  1941 |
| Testing Set  |   38   |   37  |    30   |  106  |     38    |   38  |     34   |    111    |   20   |    40  |     75    |  38  |  38 |    12   |   655 |

## Wrong Coordinate Clean

- Training Set : 440 IN 183581 ITEMS -> 183141 ITEMS  
- Testing Set : 108 IN 59673 ITEMS -> 59565 ITEMS
