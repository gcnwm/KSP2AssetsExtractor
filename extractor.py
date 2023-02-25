import os
import logging
import UnityPy
from UnityPy.classes import Mesh

# set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# set up constants
INPUT_DIR = os.path.join(os.path.dirname(__file__), 'input')
EXTRACT_DIR = os.path.join(os.path.dirname(__file__), 'output')

# create directories
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)


def unpack_assets(source_folder: str, destination_folder: str):
    # iterate over all files in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            # generate file_path
            file_path = os.path.join(root, file_name)
            # load that file via UnityPy.load
            env = UnityPy.load(file_path)

            # iterate over internal objects
            for obj in env.objects:
                # process specific object types
                if obj.type.name in ["Texture2D", "Sprite"]:
                    # parse the object data
                    data = obj.read()

                    # create destination path
                    dest = os.path.join(destination_folder, data.name)

                    # make sure that the extension is correct
                    # you probably only want to do so with images/textures
                    dest, ext = os.path.splitext(dest)
                    dest = dest + ".png"

                    img = data.image
                    img.save(dest)
                elif obj.type.name == "Mesh":
                    # parse mesh
                    mesh: Mesh = obj.read()
                    dest = os.path.join(destination_folder, mesh.name + ".obj")
                    with open(dest, "wt", newline="") as f:
                        f.write(mesh.export())
                else:
                    # print the object type
                    logger.info(f"Object type {obj.type.name} not handled")


if __name__ == '__main__':
    unpack_assets(INPUT_DIR, EXTRACT_DIR)