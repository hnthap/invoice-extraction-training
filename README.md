# Invoice Extraction for Vietnamese: some experiments

***Please carefully read this README.***

Train and evaluate models for Invoice Extraction.

⚠️ Before using the code, make sure you have these files downloaded:

| Download URL | Save to path |
| ------------ | ------------ |
| [Google Drive](https://drive.google.com/file/d/1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ/view) | weights/craft_mlt_25k.pth |
| [Google Drive](https://drive.google.com/file/d/1XSaFwBkOaFOdtk4Ane3DFyJGPRw6v5bO/view) | weights/craft_refiner_CTW1500.pth |
| [MC-OCR Competition 2021](https://aihub.ml/competitions/1) | data/mc_ocr_warmup_500images.zip |
| [MC-OCR Competition 2021](https://aihub.ml/competitions/1) | data/mcocr2021_public_train_test_data.zip |

Scripts:

- Prepare the 2021 MC-OCR corpus: [prepare_mcocr2021.py](./prepare_mcocr2021.py)
- (Text Recognition) PARSeq model: [parseq.py](./parseq.py)
- (Text Recognition) VietOCR model: [vietocr_api.py](./vietocr_api.py)
- Scene text inference (PARSeq + VietOCR): [scene_text.py](./scene_text.py)

Experiments:

- [[01] CRAFT + VietOCR/PARSeq inference](./exp_01_craft_vietocr_parseq.ipynb)
- [[02] PARSeq inference](./exp_02_parseq.ipynb)
- [[03] VietOCR inference](./exp_03_vietocr.ipynb)
- [[04] MC-OCR corpus example usage](./exp_04_mcocr_corpus.ipynb)

I use Python 3.10.11. Any other version of Python has not yet been tested.
