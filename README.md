# LayoutLM
**Multimodal (text + layout/format + image) pre-training for document AI**

## Extended Experiments

### FUNSD Dataset

| ID | Name                         | F1        | Timing | Code                                                     | Note                                                                 |
|:--:|:----------------------------:|:---------:|:------:|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| 1  | BERT from Scratch            | 23.65     | 14.21  |                                                          |                                                                      |
| 2  | BERT Pretrained              | 62.45     | 58.42  |                                                          |                                                                      |
| 2  | BERT in LayoutLM             | 66.56     | 33.16  |                                                          | 在LayoutLM的预训练模型基础上只使用BERT特征进行训练                     |
| 3  | LayoutLM from Scratch        | 19.04     | 41.58  |                                                          |                                                                      |
| 4  | LayoutLM Pretrained          | 79.20     | 80.00  | Origin LayoutLM                                          | LayoutLM相比BERT带来了实质性的提升                                    |
| 5  | LayoutLM concat Image        | 79.12     | 75.79  | ```torch.cat([layoutlm, bbox_images], 2)```              | 更make sense的concat似乎并没有很好的效果                              |
| 6  | 5 + Dropout                  | 78.96     | 89.00  |                                                          | Dropout在这里的效果平平                                               |
| 7  | LayoutLM Ensemble Image      | 79.15     | 55.26  | ```(classifier(layoutlm) + classifier(bbox_images))/2``` | 等权重的模型融合并不是一个好主意                                       |
| 8  | LayoutLM + Image             | **79.22** | 34.74  | ```layoutlm + bbox_images```                             | 增加了图像信息的LayoutLM可以在更短的时间达到更高的分数                  |
| 9  | 8 + Dropout                  | **79.45** | 42.63  |                                                          | Dropout对效果的提升起了一些作用                                       |
| 10 | Mixed Image Feature          | 78.93     | 34.74  | bbox_image += Origin Image                               | 将整张图像的特征添加到每个小图像当中降低了模型的表现                    |
| 11 | BERT + Layout + Image        | 67.50     | 94.74  |                                                          | 该特征计算与预训练模型的计算方式不同，显然地降低了效果                  |
| 12 | LayoutLM + Layout + Image    | **79.80** | 85.26  |                                                          | 在9号实验的基础之上再一次添加Layout信息，提升显著，5/19的F1都在0.79之上 |
| 13 | LayoutLM + Pos + Box + Image | 78.91     | 52.63  |                                                          | 在12号实验的基础之上拆分Layout信息为位置信息和宽高信息，结果反而下降     |

### SROIE Dataset

| ID | Name                         | F1        | Timing | Note                                                                 |
|:--:|:----------------------------:|:---------:|:------:|:--------------------------------------------------------------------:|
| 0  | BERT                         | | |                                                                               |
| 1  | LayoutLM                     | 96.92     | 66.27  |                                                                      |
| 2  | LayoutLM + Layout + Image    | 96.74     | 24.92  |                                                                      |

## Introduction

LayoutLM is a simple but effective pre-training method of text and layout for document image understanding and information extraction tasks, such as form understanding and receipt understanding. LayoutLM archives the SOTA results on multiple datasets. For more details, please refer to our paper: 

[LayoutLM: Pre-training of Text and Layout for Document Image Understanding](https://arxiv.org/abs/1912.13318)
Yiheng Xu, Minghao Li, Lei Cui, Shaohan Huang, Furu Wei, Ming Zhou, [KDD 2020](https://www.kdd.org/kdd2020/accepted-papers)

## Release Notes
**\*\*\*\*\* New Aug 7th, 2020: Our new document understanding datasets, [TableBank](https://doc-analysis.github.io/tablebank-page/) (LREC 2020) and [DocBank](https://doc-analysis.github.io/docbank-page/) (Preprint 2020), are now publicly available.\*\*\*\*\***

**\*\*\*\*\* New May 16th, 2020: Our LayoutLM paper has been accepted to KDD 2020 as a full paper in the research track\*\*\*\*\***

**\*\*\*\*\* New Feb 18th, 2020: Initial release of pre-trained models and fine-tuning code for LayoutLM v1 \*\*\*\*\***

## Pre-trained Model

We pre-train LayoutLM on IIT-CDIP Test Collection 1.0\* dataset with two settings. 

* LayoutLM-Base, Uncased (11M documents, 2 epochs): 12-layer, 768-hidden, 12-heads, 113M parameters || [OneDrive](https://1drv.ms/u/s!ApPZx_TWwibInS3JD3sZlPpQVZ2b?e=bbTfmM) | [Google Drive](https://drive.google.com/open?id=1Htp3vq8y2VRoTAwpHbwKM0lzZ2ByB8xM)
* LayoutLM-Large, Uncased (11M documents, 2 epochs): 24-layer, 1024-hidden, 16-heads, 343M parameters || [OneDrive](https://1drv.ms/u/s!ApPZx_TWwibInSy2nj7YabBsTWNa?e=p4LQo1) | [Google Drive](https://drive.google.com/open?id=1tatUuWVuNUxsP02smZCbB5NspyGo7g2g)

\*As some downstream datasets are the subsets of IIT-CDIP, we have carefully excluded the overlap portion from the pre-training data.

## Fine-tuning Example

We evaluate LayoutLM on several document image understanding datasets, and it outperforms several SOTA pre-trained models and approaches.

Setup environment as follows:

~~~bash
conda create -n layoutlm python=3.6
conda activate layoutlm
conda install pytorch==1.4.0 cudatoolkit=10.1 -c pytorch
git clone https://github.com/NVIDIA/apex && cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
pip install .
## For development mode
# pip install -e ".[dev]"
~~~

### Sequence Labeling Task


We give a fine-tuning example for sequence labeling tasks. You can run this example on [FUNSD](https://guillaumejaume.github.io/FUNSD/), a dataset for document understanding tasks.

First, we need to preprocess the JSON file into txt. You can run the preprocessing scripts `funsd_preprocess.py` in the `scripts` directory. For more options, please refer to the arguments.

~~~bash
cd examples/seq_labeling
./preprocess.sh
~~~

After preprocessing, run LayoutLM as follows:

~~~bash
python run_seq_labeling.py  --data_dir data \
                            --model_type layoutlm \
                            --model_name_or_path path/to/pretrained/model/directory \
                            --do_lower_case \
                            --max_seq_length 512 \
                            --do_train \
                            --num_train_epochs 100.0 \
                            --logging_steps 10 \
                            --save_steps -1 \
                            --output_dir path/to/output/directory \
                            --labels data/labels.txt \
                            --per_gpu_train_batch_size 16 \
                            --per_gpu_eval_batch_size 16 \
                            --fp16
~~~

Note: The `DataParallel` will be enabled automatically to utilize all GPUs. If you want to train with `DistributedDataParallel`, please run the script like:

~~~bash
# Suppose you have 4 GPUs. 

python -m torch.distributed.launch --nproc_per_node=4 run_seq_labeling.py  --data_dir data \
                            --model_type layoutlm \
                            --model_name_or_path path/to/pretrained/model/directory \
                            --do_lower_case \
                            --max_seq_length 512 \
                            --do_train \
                            --num_train_epochs 100.0 \
                            --logging_steps 10 \
                            --save_steps -1 \
                            --output_dir path/to/output/directory \
                            --labels data/labels.txt \
                            --per_gpu_train_batch_size 16 \
                            --per_gpu_eval_batch_size 16 \
                            --fp16
~~~



Then you can do evaluation or inference by replacing `--do_train` with `--do_eval` or `--do_predict`

Also, you can run Bert and RoBERTa baseline by modifying the `--model_type` argument. For more options, please refer to the arguments of `run.py`.

### Document Image Classification Task

We also fine-tune LayoutLM on the document image classification task. You can download the [RVL-CDIP](https://www.cs.cmu.edu/~aharley/rvl-cdip/) dataset from [here](https://www.cs.cmu.edu/~aharley/rvl-cdip/). Because this dataset only provides the document image, you should use the OCR tool to get the texts and bounding boxes. For example, you can easily use Tesseract, an open-source OCR engine, to generate corresponding OCR data in hOCR format. For more details, please refer to the [Tesseract wiki](https://github.com/tesseract-ocr/tesseract/wiki). Your processed data should look like [this sample data](https://1drv.ms/u/s!ApPZx_TWwibInTlBa5q3tQ7QUdH_?e=UZLVFw). 

With the processed OCR data, you can run LayoutLM as follows:

~~~bash
python run_classification.py  --data_dir  data \
                              --model_type layoutlm \
                              --model_name_or_path path/to/pretrained/model/directory \
                              --output_dir path/to/output/directory \
                              --do_lower_case \
                              --max_seq_length 512 \
                              --do_train \
                              --do_eval \
                              --num_train_epochs 40.0 \
                              --logging_steps 5000 \
                              --save_steps 5000 \
                              --per_gpu_train_batch_size 16 \
                              --per_gpu_eval_batch_size 16 \
                              --evaluate_during_training \
                              --fp16 
~~~

Similarly, you can do evaluation by changing `--do_train` to `--do_eval` and `--do_test`

Like the sequence labeling task, you can run Bert and RoBERTa baseline by modifying the `--model_type` argument.

### Results

#### SROIE


| Model                                                        | Hmean      |
| ------------------------------------------------------------ | ---------- |
| BERT-Large                                                   | 90.99%     |
| RoBERTa-Large                                                | 92.80%     |
| [Ranking 1st in SROIE](https://rrc.cvc.uab.es/?ch=13&com=evaluation&task=3) | 94.02%     |
| [**LayoutLM**](https://rrc.cvc.uab.es/?ch=13&com=evaluation&view=method_info&task=3&m=71448) | **96.04%** |

#### RVL-CDIP

| Model                                                        | Accuracy   |
| ------------------------------------------------------------ | ---------- |
| BERT-Large                                                   | 89.92%     |
| RoBERTa-Large                                                | 90.11%     |
| [VGG-16 (Afzal et al., 2017)](https://arxiv.org/abs/1704.03557) | 90.97%     |
| [Stacked CNN Ensemble (Das et al., 2018)](https://arxiv.org/abs/1801.09321) | 92.21%     |
| [LadderNet (Sarkhel & Nandi, 2019)](https://www.ijcai.org/Proceedings/2019/0466.pdf) | 92.77%     |
| [Multimodal Ensemble (Dauphinee et al., 2019)](https://arxiv.org/abs/1912.04376) | 93.07%     |
| **LayoutLM**                                                 | **94.42%** |

#### FUNSD

| Model         | Precision  | Recall     | F1         |
| ------------- | ---------- | ---------- | ---------- |
| BERT-Large    | 0.6113     | 0.7085     | 0.6563     |
| RoBERTa-Large | 0.6780     | 0.7391     | 0.7072     |
| **LayoutLM**  | **0.7677** | **0.8195** | **0.7927** |

## Citation

If you find LayoutLM useful in your research, please cite the following paper:

``` latex
@misc{xu2019layoutlm,
    title={LayoutLM: Pre-training of Text and Layout for Document Image Understanding},
    author={Yiheng Xu and Minghao Li and Lei Cui and Shaohan Huang and Furu Wei and Ming Zhou},
    year={2019},
    eprint={1912.13318},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## License

This project is licensed under the license found in the LICENSE file in the root directory of this source tree.
Portions of the source code are based on the [transformers](https://github.com/huggingface/transformers) project.
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct)

### Contact Information

For help or issues using LayoutLM, please submit a GitHub issue.

For other communications related to LayoutLM, please contact Lei Cui (`lecu@microsoft.com`), Furu Wei (`fuwei@microsoft.com`).

