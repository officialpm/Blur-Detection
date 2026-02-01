# Blur Detection (OpenCV)

A tiny Python script that detects whether an image is **blurry** using the classic **Variance of Laplacian** focus measure.

It prints the result and opens a window showing the image with an overlaid label and score.

## How it works

- Converts the image to grayscale
- Computes `Laplacian(gray).var()`
- Compares against a threshold (currently `100.0` in `app.py`)

## Requirements

- Python 3
- OpenCV (`opencv-python`)
- `imutils` (imported in the script)

## Usage

```bash
python app.py --image path/to/image.jpg
```

## Customize

- Tune the blur threshold in `app.py`:

```python
threshold = 100.0
```

## Repo contents

- `app.py` — main script
- `avatar.png`, `avatar-blur.png` — sample images
- `results/` — output examples

## License

No license specified.
