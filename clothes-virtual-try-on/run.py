from PIL import Image
import os
import sys

# absolute_path = os.getcwd() + os.sep
absolute_path = sys.argv[1].strip()


# running the preprocessing

def resize_img(path):
    im = Image.open(path)
    im = im.resize((768, 1024))
    im.save(path)


for path in os.listdir(f'{absolute_path}inputs/test/cloth/'):
    resize_img(f'{absolute_path}inputs/test/cloth/{path}')

os.chdir(f'{absolute_path}clothes-virtual-try-on')
os.system(f"rm -rf {absolute_path}inputs/test/cloth/.ipynb_checkpoints")
os.system(f"python cloth-mask.py {absolute_path}")
os.chdir(f'{absolute_path[:-1]}')
os.system(f"python {absolute_path}clothes-virtual-try-on/remove_bg.py {absolute_path}")
model = os.path.join(absolute_path, "Self-Correction-Human-Parsing/checkpoints/final.pth")
input_dir = os.path.join(absolute_path, "inputs/test/image")
out_dir = os.path.join(absolute_path, "inputs/test/image-parse")
os.system(
    f"python {absolute_path}Self-Correction-Human-Parsing/simple_extractor.py --dataset lip --model-restore {model} --input-dir {input_dir} --output-dir {out_dir}")

os.chdir(f'{absolute_path[:-1]}')
json_dir = os.path.join(absolute_path, "inputs/test/openpose-json/")
image_dir = os.path.join(absolute_path, "inputs/test/openpose-img/")
open_bin = os.path.join(absolute_path, "openpose/build/examples/openpose/openpose.bin")
os.system(
    f"{open_bin} --image_dir {input_dir} --write_json {json_dir} --display 0 --render_pose 0 --hand")
os.system(
    f"{open_bin} --image_dir {input_dir} --display 0 --write_images {image_dir} --hand --render_pose 1 --disable_blending true")

model_image = os.listdir(f'{absolute_path}inputs/test/image')
cloth_image = os.listdir(f'{absolute_path}inputs/test/cloth')
pairs = zip(model_image, cloth_image)

with open(f'{absolute_path}inputs/test_pairs.txt', 'w') as file:
    for model, cloth in pairs:
        file.write(f"{model} {cloth}")

# making predictions
os.system(
    f"python {absolute_path}clothes-virtual-try-on/test.py --name output --dataset_dir {absolute_path}inputs --checkpoint_dir {absolute_path}clothes-virtual-try-on/checkpoints --save_dir {absolute_path}")
# os.system(f"rm -rf {absolute_path}inputs")
os.system(f"rm -rf {absolute_path}output/.ipynb_checkpoints")
