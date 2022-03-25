# v0.0.4.1

Feature: now able to add jpeg files directly without decoding and re-encoding
which results in adding up the compression artefacts, unwanted loss of data and
slower processing. Yield list of paths to the jpeg files instead of numpy arrays 
in the adapter.

Feature: Option to specify jpeg encode quality from the adapter. Define a function 
`jpeg_encode_quality(self)` and return an integer in range (0,100]. It is backward 
compatible because the `AbstractDatasetAdapter` class has a pre-defined value of 90.

# v0.0.4

Bugfix: `gulpio2.utils.burst_video_into_frames` extracted frames with the naming
format `%04d.jpg`, so if more than 1000 frames were extracted they would not be
gulped correctly. This has now been changed to `%010d.jpg` which will handle 60
FPS video a duration of 316 years correctly!
