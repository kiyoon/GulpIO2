# GulpIO2

Binary storage format for deep learning on videos.

# Fork Notice

This is a fork of Will Price's [gulpio2](https://github.com/willprice/GulpIO2).

# Fork Motivation
Many video datasets provide extracted jpeg format already, but the current GulpIO2 (v0.0.4) doesn't have a functionality to directly add the files without having to decode and re-encode them. It will slow down by 3 times when preparing the gulp directory, not to mention that there will be unwanted loss of data and compression artefacts.

# New Features

1. Now able to add jpeg files directly without decoding and re-encoding. Yield list of paths to the jpeg files instead of numpy arrays in the adapter.

2. Another change is the ability to specify jpeg encoding quality from the adapter. Define a function `jpeg_encode_quality(self)` and return an integer in range (0,100]. It is backward compatible because the `AbstractDatasetAdapter` class has a pre-defined value of 90.

# Benchmark

Here are the benchmark results using EPIC-Kitchens-100 dataset, generating optical flow training set gulp.

Re-encoding adapter can be found [here](https://github.com/epic-kitchens/C1-Action-Recognition-TSN-TRN-TSM/blob/2b7fa1894656e71dc5f8935213396b12c01b2eef/src/utils/gulp_adapter.py) and  
Modified adapter that bypasses re-encoding can be found [here](https://github.com/kiyoon/video_datasets_api/blob/d35e38e8a34aca0332553cd2d7e89c120c0c89a3/video_datasets_api/epic_kitchens_100/gulp_adapter.py).

Tested with the `AMD Ryzen 7 5800X 8-Core Processor` CPU and an NVME drive.

|GulpIO2 version|Re-encoding|Speed    |Final Size|
|---------------|-----------|---------|----------|
|0.0.4.1        |**No**     |**06:16**|**112GiB**|
|0.0.4.1        |Yes        |18:50    |78GiB     |
|0.0.4          |Yes        |18:52    |78GiB     |
