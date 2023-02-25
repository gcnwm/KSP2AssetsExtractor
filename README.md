# KSP2AssetsExtractor

## Intro

A script build with [*UnityPy*](https://github.com/K0lb3/UnityPy) intended to extract Texture2D and Mesh files form KSP2 asset bundles.


## Usage

**Python 3.6.0 or higher is required**


### Install UnityPy

via pypi

```cmd
pip install UnityPy
```

from source

```cmd
git clone https://github.com/K0lb3/UnityPy.git
cd UnityPy
python -m pip install .
```


### Get assets bundles

Assets bundles are located in `SteamLibrary\steamapps\common\Kerbal Space Program 2\KSP2_x64_Data\StreamingAssets\aa\StandaloneWindows64`.

All parts resource files are encapsulated in a separate bundle, starting with `parts-base_assets_`.


### Extract Texture2D and Mesh

Create a new folder named `input` in the same directory as `extractor.py`.

```
.
├── input
│   └── xxxxxx.bundle
└── extractor.py
```

Then simply run

```cmd
python ./extractor.py
```

Though you can process multiple bundles at once, it is not recommended.
Because the resource files will all be extracted into the `output` folder.
You may need to spend more time sorting them out.