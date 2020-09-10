# Extended Experiments on LayoutLM

[Github Homepage of LayoutLM](https://github.com/microsoft/unilm/tree/master/layoutlm)

## FUNSD Dataset

### Experiments

| ID | Name                         | F1        | Timing | Code                                                     | Note                                                                 |
|:--:|:----------------------------:|:---------:|:------:|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| 01 | BERT from Scratch            | 23.65     | 14.21  | ```model.init_weights()```                               | 从零训练BERT模型                                                      |
| 02 | BERT Pretrained              | 62.45     | 58.42  | Origin BERT                                              | BERT预训练模型对效果提升显著                                          |
| 03 | BERT in LayoutLM             | 66.56     | 33.16  |                                                          | 在LayoutLM的预训练模型基础上只使用BERT特征进行训练                     |
| 04 | LayoutLM from Scratch        | 19.04     | 41.58  | ```model.init_weights()```                               | 从零训练含有BERT框架的LayoutLM的结果并不如纯粹的BERT模型               |
| 05 | LayoutLM Pretrained          | 79.20     | 80.00  | Origin LayoutLM                                          | LayoutLM预训练模型相比BERT带来了更大的提升                            |
| 06 | LayoutLM Concat Image        | 79.12     | 75.79  | ```torch.cat([layoutlm, bbox_images], 2)```              | 更make sense的concat似乎并没有很好的效果                              |
| 07 | 6 + Dropout                  | 78.96     | 89.00  |                                                          | Dropout在这里的效果平平                                               |
| 08 | LayoutLM Ensemble Image      | 79.15     | 55.26  | ```(classifier(layoutlm) + classifier(bbox_images))/2``` | 等权重的模型融合并不是一个好主意                                       |
| 09 | LayoutLM + Image             | **79.22** | 34.74  | ```layoutlm + bbox_images```                             | 增加了图像信息的LayoutLM可以在更短的时间达到更高的分数                  |
| 10 | 9 + Dropout                  | **79.45** | 42.63  |                                                          | Dropout对效果的提升起了一些作用                                       |
| 11 | Mixed Image Feature          | 78.93     | 34.74  | bbox_image += Origin Image                               | 将整张图像的特征添加到每个小图像当中降低了模型的表现                    |
| 12 | BERT + Layout + Image        | 67.50     | 94.74  |                                                          | 该特征计算与预训练模型的计算方式不同，显然地降低了效果                  |
| 13 | LayoutLM + Layout + Image    | **79.80** | 85.26  |                                                          | 在10号实验的基础之上再一次添加Layout信息，提升显著，5/19的F1都在0.79之上 |
| 14 | LayoutLM + Pos + Box + Image | 78.91     | 52.63  |                                                          | 在13号实验的基础之上拆分Layout信息为位置信息和宽高信息，结果反而下降     |
| 15 | 13 + BERT                    | 78.50     | 90.53  |                                                          | 在13号实验的基础之上再一次添加BERT特征，结果反而下降                    |

### Tensorboard

#### Eval_F1

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrEJuU6JtppyfvLR1e5Ql*enErLnwUTMp61vuJJuqDyI7YlunVmDbvp71rR522d*76O7qYnZ6xLHcBafEvrPCuUFs!/r)

#### Eval_Precision

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrELlyWa8XHVus03N4TdYy4UMw4J7FyxuLMbyhSmXRg*lkBG8AJVndffxsaxpuqnl54efeEB9OaDJXawFgn4f7SWQ!/r)

#### Eval_Recall

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrEAxIKMwH4V95AfIKt9hZaLquheMEUMl57ZecV.36S*baX72Dyr5XyrAJelMKHxHvKGV1wAEq9gu*T6XpjWmAv1o!/r)

#### Eval Loss

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrEK8lkoPxJtArWvItLsF0O*Nmcj9N3YNKp*NJnbHRpQy0zUCIY77X7h2ffOndoQmtH4YvhYi2okFu0X1sRF68yFw!/r)

#### Train_Loss

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrEPw8Oh04YAj9E6g7yw1zjZyhjUabdVUO2DBpdvXWcjq3HW0b.8RwZhjWDXAkEfcex46qeXEvmOixRjYNT7RbGJI!/r)

## SG-Customs Dataset

- [SG_Customs Dataset]()
- [SG_Customs Dataset_Invoice](https://bhpan.buaa.edu.cn:443/link/79BD538BDBE5AA4164ED03C0491DA737)
- [SG_Customs Dataset_Invoice [Splitted]](https://bhpan.buaa.edu.cn:443/link/A6D049B5ACF2CABA80E8F8B48AD39C4B)
- [SG_Customs Dataset_Invoice [Overall]](https://bhpan.buaa.edu.cn:443/link/A4CDAB285216DE3EC0E15CF76A7F9098)
- [cached_train_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/8A4996BAE9179BCE75E1FB665AE09949)
- [cached_test_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/4962F0E4280A89304FCC0E946C6C130B)
- [sen_level_cached_train_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/4962F0E4280A89304FCC0E946C6C130B)
- [sen_level_cached_test_layoutlm-base-uncased_512](https://bhpan.buaa.edu.cn:443/link/EBCFD7481BCD27C1937BEB2BFB73771D)

### Overview on Dataset

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

### Wrong Coordinate Clean

- Training Set : 440 IN 183581 ITEMS -> 183141 ITEMS  
- Testing Set : 108 IN 59673 ITEMS -> 59565 ITEMS  

### Original Feature Train in LayoutLM

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrELP5owIgRhIWHjWkha3EGe1wa97QtvsELW1diSeF.DuDVD7IWVIZRg7lW0ynwEayLtVFTJ.LjMw0zePnpplsS2E!/r)

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrEGc6ty4kFrczvEjnZuDw5KJgqmputEHr8zp6GwdUaipcq*QUD*VuLfO5NLeVVYT3EkhdBQOajZbtJQbHoh6rfSE!/r)

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrEIZlXwcoL8pnBqff6hDaKGSwYzJrsLM2wjoK6eJ7qaFulL.w8TzYctzcuAVSGe5arEdpgPfvf2CkAyIPcsGFSo4!/r)

![](http://r.photo.store.qq.com/psc?/V50VqFfH2A6OlZ2gWBDL0uxzNK4WmFgm/TmEUgtj9EK6.7V8ajmQrEA*gGtfVgk5CdVghOiV3dNKOx2R9ens3YHPr5ftAMrB1n2kyu4tJJzMAeO1tELjUo65wG*qjslCJM55ZOjfBWRc!/r)

